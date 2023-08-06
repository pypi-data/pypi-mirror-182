from os import environ
import sqlalchemy
from sqlalchemy.engine import Engine
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import *
from sqlalchemy.sql.functions import *
from sqlalchemy_utils import functions as sqlalchemy_utils


class Connection:
    engine: Engine

    @classmethod
    def _verify(cls):
        # Check connection works
        with cls.engine.connect() as con:
            pass

    @classmethod
    def _create(cls):
        if not sqlalchemy_utils.database_exists(cls.engine.url):
            sqlalchemy_utils.create_database(cls.engine.url)

    @classmethod
    def _drop(cls):
        if sqlalchemy_utils.database_exists(cls.engine.url):
            sqlalchemy_utils.drop_database(cls.engine.url)

    @classmethod
    def _execute(cls, query: str, params: dict | list[dict] = None, _result: bool = False) -> None | CursorResult:
        """Execute query with params, no result. Privately"""
        with cls.engine.connect() as connection:
            cur = connection.execute(sqlalchemy.text(query), params)

            if _result:
                return cur
            else:
                cur.close()

    def execute_query(self, query: str, params: dict | list[dict] = None) -> None:
        """Execute query with params, no result"""
        return self._execute(query, params)

    def execute_query_result(self, query: str, params: dict | list[dict] = None, return_list: bool = True) -> list[dict] | dict[list]:
        """Execute query with params, with result"""
        result = self._execute(query, params, _result=True)
        keys = list(result.keys())
        values = result.all()

        if return_list:
            return [{keys[i]: value[i] for i in range(len(keys))} for value in values]
        else:
            return {keys[i]: [value[i] for value in values] for i in range(len(keys))}

    def execute_query_result_single(self, query: str, params: dict | list[dict] = None) -> dict:
        """Execute query with params, with single result"""
        result = self._execute(query, params, _result=True)
        keys = list(result.keys())
        values = result.fetchone()

        if not values or result.fetchone():
            raise ValueError("Incorrect number of rows returned")

        result.close()
        return {keys[i]: values[0] for i in range(len(keys))}


if __name__ == "__main__":
    pass
else:
    if not environ.get("DB_CONN"):
        raise ValueError("DB_CONN not set")

    Connection.engine = sqlalchemy.create_engine(environ.get("DB_CONN"), poolclass=QueuePool)
    Connection()
