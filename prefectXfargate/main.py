from prefect import flow
from ingestion.ingestion import ingestion_from_db
from transform.transform import transform_data
from loader.source import load_into_s3

@flow
def main(table_name: str) -> None:
    df = ingestion_from_db(table_name)
    path = transform_data(df)
    load_into_s3(path)
    print('Done!')

if __name__ == '__main__':
    db_table = 'transactions'
    main(db_table)