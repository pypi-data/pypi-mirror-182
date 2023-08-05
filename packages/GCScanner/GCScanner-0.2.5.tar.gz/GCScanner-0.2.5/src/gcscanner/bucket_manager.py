# Imports the Google Cloud client library
from google.cloud import storage

from typing import List


def list_buckets(project: str) -> List:
    """Lists all buckets from a project."""
    # Instantiates a client
    storage_client = storage.Client(project=project)
    buckets = storage_client.list_buckets()
    return buckets


def get_bucket(project: str, bucket: str) -> storage.Bucket:
    """Lists all buckets."""
    # Instantiates a client
    storage_client = storage.Client(project=project)
    bucket = storage_client.get_bucket(bucket)
    return bucket
