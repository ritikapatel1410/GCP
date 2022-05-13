from google.cloud import storage

def implicit():
    from google.cloud import storage
    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client.from_service_account_json("graphic-option-349209-d8eae329bb5a.json")
    dest_bucket = storage_client.get_bucket("rit_sample_bucket-1")
    source_bucket = storage_client.get_bucket("rit_sample_bucket")
    source_blob = source_bucket.blob("sample.txt")
    destination_blob_name="sample1.txt"
    blob_copy = source_bucket.copy_blob(
        source_blob, dest_bucket, destination_blob_name
    )

    #print(buckets)
implicit()
