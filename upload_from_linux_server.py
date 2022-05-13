#code_testing

from google.cloud import storage         
storage_client = storage.Client.from_service_account_json("key.json")
bucket = storage_client.get_bucket("rit_sample_bucket-1")
filename = "%s" % ("sample_data.txt")
blob = bucket.blob(filename)


# Uploading string of text
#blob.upload_from_string('this is test content!')
"""
# Uploading from a local file using open()
with open('photo.jpg', 'rb') as photo:
    blob.upload_from_file(photo)
"""
# Uploading from local file without open()
source_file_name="sample_data.txt"
blob.upload_from_filename(source_file_name)
