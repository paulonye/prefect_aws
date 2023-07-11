"""This script is used to initialize all ingestion logic"""

import pandas as pd
from prefect import task
from prefect_sqlalchemy import SqlAlchemyConnector

@task(retries = 3, tags = ["extract from postgres database"])
def ingestion_from_db(table_name: str) -> pd.DataFrame:
    """This function is used to import data from postgres db"""
    database_block = SqlAlchemyConnector.load("mysql-connector")
    with database_block.get_connection(begin=False) as engine:
        df = pd.read_sql(f"SELECT * from {table_name}", con = engine)
        return df

if __name__ == '__main__':
    table_name = 'transactions'
    ingestion_from_db(table_name)
