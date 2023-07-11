"""This script is used to transform data gotten from the mysql data"""

import pandas as pd
from prefect import task
from pathlib import Path

@task(retries = 3, tags = ["transform data"])
def transform_data(df: pd.DataFrame) -> Path:
    df = df[['payment_method', 'delivery_status', 'amount']]

    con_df = pd.DataFrame()
    for method in df['payment_method'].unique():
        ext_df = df[df['payment_method'] == method].groupby('delivery_status').sum()
        ext_df = ext_df.rename(columns={'total_amount': method})
        con_df = pd.concat([con_df, ext_df], axis=1)

    con_df.to_csv('./data.csv')
    path = Path('./data.csv')
    return path

if __name__ == '__main__':
    test_dict = {'payment_method': ['Cash', 'POS'], 'delivery_status': ['Pickup', 'Delivery'], 'amount': [3000, 5000]}
    df = pd.DataFrame(test_dict)
    print(df)
    transform_data(df)
