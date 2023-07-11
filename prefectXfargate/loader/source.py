from prefect import task
from prefect_aws.s3 import S3Bucket
from pathlib import Path

@task(retries = 3, tags = ['Loading Data into S3'])
def load_into_s3(path: Path) -> None:
    """This is used to Upload a directory from a given local path to the configured S3 bucket"""
    s3_bucket_block = S3Bucket.load("test-bucket")
    
    s3_bucket_block.upload_from_path(from_path=path, to_path=path)



