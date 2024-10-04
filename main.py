import sys
import os
from google.cloud import storage
from datetime import datetime, timedelta

def process_file(request):
    # Generate filename for the previous day
    yesterday = datetime.now() - timedelta(days=1)
    filename = f"export_attachment_dm_alerts_{yesterday.strftime('%Y%m%d')}.csv"

    # Set up GCS client
    storage_client = storage.Client()
    bucket_name = 'bucket-id'
    source_bucket = storage_client.bucket(bucket_name)

    # Copy from bucket to /tmp/
    source_blob = source_bucket.blob(filename)
    temp_file_path = f'/tmp/{filename}'
    source_blob.download_to_filename(temp_file_path)

    # Zip the file
    zip_filename = f"{os.path.splitext(filename)[0]}.tar.gz"
    os.system(f"tar -czvf /tmp/{zip_filename} -C /tmp {filename}")

    # Copy zipped file back to bucket
    destination_blob = source_bucket.blob(zip_filename)
    destination_blob.upload_from_filename(f'/tmp/{zip_filename}')

    # Clean up temporary files
    os.remove(temp_file_path)
    os.remove(f'/tmp/{zip_filename}')

    return f"Processed {filename} successfully"