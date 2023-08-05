from dddmisc import AbstractAsyncUnitOfWork
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.read_concern import ReadConcern
from pymongo.write_concern import WriteConcern
from types import MappingProxyType
from typing import Iterable

from .abstraction import AbstractMongoRepository


class RepositoryWrapperr:
    def __init__(self, repository_class, collections):
        self._repository_class = repository_class
        self._collections = collections

    def __call__(self, connection):
        return self._repository_class(connection=connection, collections=self._collections)


class MongoEngine:
    def __init__(self, address: str, db_name, collections: Iterable[str]):
        self._client = AsyncIOMotorClient(address)
        self._db = self._client[db_name]
        collections_dict = dict()
        for collection in collections:
            collections_dict[collection] = self._db[collection]
        self._collections = MappingProxyType(collections_dict)

    def get_collections(self):
        return self._collections

    async def get_session(self):
        return await self._client.start_session()


class MongoMotorUOW(AbstractAsyncUnitOfWork):

    def __init__(self, engine: MongoEngine, repository_class: AbstractMongoRepository):
        if not issubclass(repository_class, AbstractMongoRepository):
            raise TypeError('Repository class in "MongoMotorUOW" can be subclass of "AbstractMongoRepository"')
        repository_class = RepositoryWrapperr(repository_class, engine.get_collections())
        super().__init__(engine, repository_class)

    async def _begin_transaction(self, mongo_engine: MongoEngine):
        self._mongo_session = await mongo_engine.get_session()
        session_context = await self._mongo_session.__aenter__()
        self._trn_context = session_context.start_transaction()
        await self._trn_context.__aenter__()
        return session_context

    async def _commit_transaction(self, session_context):
        if hasattr(self, '_trn_context'):
            await session_context.commit_transaction()
            await self._trn_context.__aexit__(None, None, None)
            delattr(self, '_trn_context')
            await self._mongo_session.__aexit__(None, None, None)
            delattr(self, '_mongo_session')
        else:
            raise RuntimeError('Database transaction not found')

    async def _rollback_transaction(self, session_context):
        if hasattr(self, '_trn_context'):
            await session_context.abort_transaction()
            trn_context = self._trn_context
            await trn_context.__aexit__(None, None, None)
            delattr(self, '_trn_context')
            await self._mongo_session.__aexit__(None, None, None)
            delattr(self, '_mongo_session')