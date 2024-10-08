﻿# GCP File Processing Script

This script is designed to run on Google Cloud Platform (GCP) to process files from a Cloud Storage bucket. It downloads a CSV file from the previous day, compresses it, and uploads the compressed file back to the bucket.

## Features

- Automatically generates the filename based on the previous day's date
- Downloads the file from a specified GCS bucket
- Compresses the file using tar and gzip
- Uploads the compressed file back to the same bucket
- Cleans up temporary files after processing

## Requirements

- Python 3.6+
- Google Cloud Storage library (`google-cloud-storage`)

## Setup

1. Ensure you have the necessary permissions to access the GCS bucket.
2. Install the required library: pip install google-cloud-storage


## Usage

This script is designed to be deployed as a Google Cloud Function. The main function is `process_file(request)`, which can be triggered via HTTP request or scheduled to run daily.

## Configuration

- `bucket_name`: Set this to your GCS bucket name 

## Function Details

1. Generates a filename based on yesterday's date in the format: `export_YYYYMMDD.csv`
2. Downloads the file from the specified GCS bucket to a temporary location
3. Compresses the file using tar and gzip
4. Uploads the compressed file (`.tar.gz`) back to the same GCS bucket
5. Cleans up temporary files

## Error Handling

The script does not include explicit error handling. In a production environment, you should add appropriate try/except blocks and logging.

## Deployment

Deploy this script as a Google Cloud Function. Set up a Cloud Scheduler job to trigger this function daily to process the previous day's file.

