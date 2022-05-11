from deletem.config import Config
import deletem.vault as vault
from fybrik_python_logging import init_logger, logger
import boto3

def s3_connection(endpoint, aws_access_key, aws_secret_key):
    try:
        logger.info("Connecting S3 client")
        s3_resource = boto3.resource("s3", endpoint_url=endpoint, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
        s3_client = boto3.client("s3", endpoint_url=endpoint, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    except:
        logger.info("Could not connect to S3 client")
        raise
    else:
        return s3_resource, s3_client

def delete_object(s3_client, bucket_name, object_key):
    try:
        logger.info(f"Deleting object: '{object_key}' from bucket: '{bucket_name}'")
        response = s3_client.delete_object(Bucket=bucket_name, Key=object_key)
    except:
        logger.error("Could not delete object")
        raise
    else:
        return response


if __name__ == "__main__":
    init_logger("TRACE", "7d320bd3-df69-4c66-ba58-f6de26fa1744", 'delete-module')
    logger.info('Delete module initialized')

    conf = Config("/etc/conf/conf.yaml")
    conf_data = conf.values["data"][0]
    dataID = conf_data["name"]
    endpoint = conf_data["connection"]["s3"]["endpoint_url"]
    vault_cred = conf_data["connection"]["s3"]["vault_credentials"]

    access_key, secret_key = vault.get_credentials_from_vault(vault_cred, dataID)

    s3_resource, s3_client = s3_connection(endpoint, access_key, secret_key)

    bucket_name, object_key = conf_data["path"].split("/")
    logger.info("Deleting object")
    delete_object(s3_client, bucket_name, object_key)
    logger.info(f"Object '{object_key}' deleted.")







