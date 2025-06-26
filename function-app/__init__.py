import logging
import os
from io import BytesIO
from PIL import Image
import azure.functions as func
from azure.storage.blob import BlobServiceClient

# Get connection string and container names from environment variables
connection_string = os.getenv("AzureWebJobsStorage")
output_container = os.getenv("OUTPUT_CONTAINER", "output")

def main(myblob: func.InputStream):
    logging.info(f"Processing blob \n Name: {myblob.name}\n Size: {myblob.length} bytes")

    try:
        # Connect to Blob Service
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Read image from input blob
        image_stream = BytesIO(myblob.read())
        image = Image.open(image_stream)

        # Resize image
        max_size = (800, 800)
        image.thumbnail(max_size)

        # Save resized image to bytes buffer
        output_stream = BytesIO()
        image.save(output_stream, format=image.format)
        output_stream.seek(0)

        # Upload resized image to output container
        output_blob_client = blob_service_client.get_blob_client(container=output_container, blob=myblob.name.split('/')[-1])
        output_blob_client.upload_blob(output_stream, overwrite=True)

        logging.info(f"Resized image uploaded to container '{output_container}' with name '{myblob.name.split('/')[-1]}'")

    except Exception as e:
        logging.error(f"Error processing blob: {e}")
