"""This script is used to load data into the postgres database"""

from os.path import realpath, dirname, join
import pandas as pd
from sqlalchemy import create_engine

def read_data(file_locator: str) -> None:
    '''Load data into the transactions table of a postgres datbase
       Input: File Directory''' 

    engine = create_engine('postgresql://root:root@localhost:5432/root')
    df = pd.read_csv(file_locator)
    df = df[1:]
    df.to_sql('transactions', engine, if_exists='replace', index=False)
    print('Loaded Data into DB!')

if __name__ == '__main__':
    locator = realpath(dirname('__file__'))
    file_location = join(locator, 'records.csv')
    read_data(file_location)

        