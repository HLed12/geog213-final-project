import os
import dask_geopandas as dg
import tqdm
from botocore.exceptions import ClientError


def get_s3_keys_all(bucket_name, prefix, client):
    """
    This function returns all the S3 keys associated with the entire
    USA Structures Dataset by Oak Ridge National Laboratory on Source Cooperative. This function
    only lists the files in GeoParquet format.
    For more information about the dataset, visit 
    (https://source.coop/repositories/wherobots/usa-structures/description).


    Inputs:
    --------
    bucket_name : string 
        A sting indicating the Source Cooperative user that uploaded the dataset.
    prefix : string
        A string that contains the prefix for each parquet file name that the dataset offers.
    client : boto3 client object 
        A s3 client returned by boto3.client.


    Returns:
    --------
    keys: list
        List of all keys in the dataset.
    """
    keys = []

    response = client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    for obj in response['Contents']:
        keys.append(obj['Key'])

    return keys

def get_US_structures_all(s3_client, local_path, blocksize="256M"):
    """
    This function downloads geoparquet files from the USA Structures Dataset by Oak Ridge National Laboratory on Source Cooperative
    (https://source.coop/repositories/wherobots/usa-structures/description). 

    Inputs:
    --------
    s3_client: boto3 resource client
        A boto3 resource client configured with AWS credentials and the endpoint_url for Source Cooperative
    local_path: string
        Path to a local directory for downloading the geoparquet file(s) (example: "./data/")
    blocksize: string
        Blocksize used to load the geoparquet with Dask DataFrame. Default is 256M.

    Returns:
    --------
    bldg_ddf: Dask-Geopandas GeoDataFrame
        Structures footprint dataset in a Dask-Geopandas GeoDataFrame with lazy loading. 
 
    """
    bucket_name = 'wherobots'  # (Bucket name is the account that posted the dataset on source.coop)
    prefix = "usa-structures/geoparquet/part-"

    # Since I updated get_s3_keys to handle a list of links, we do not need to worry about iterating through 'links' here.
    keys = get_s3_keys_all(bucket_name, prefix, s3_client)


    for key in keys:
        local_fname = f"{local_path}/{key.split('/')[-1]}"  # May need to change
        if not os.path.exists(local_path):
            os.mkdir(local_path)

        if not os.path.exists(local_fname):
            print(f"File not found locally. Downloading from s3...")
            
            try:
                s3_client.download_file(Bucket = bucket_name,
                                        Key = key,
                                        Filename = f"./data/{key.split('/')[-1]}"  # May need to change
                                    )
                print("Download complete.")
            except ClientError as error:
                if error.response["Error"]["Code"] == "404":
                    print("The specified key does not exist in the bucket.")
                else:
                    print(f"An error occurred: {error}")
            except Exception as error:
                print(f"An unexpected error occurred: {error}")
        else:
            print("File already exists locally. No download needed.")


    # UPDATE, Reading documentation file explains it needs to be a list of file paths so we should copy the format for Hamed's example but for each "link"
    # that we add to this variable.
    local_file_names = [f"{local_path}/{key.split('/')[-1]}" for key in keys] # Now, it will be "(local_path)/part-(specified-number)-(ending)"

    structures_ddf = dg.read_parquet(local_file_names, gather_spatial_partitions=False, blocksize = blocksize)

    return structures_ddf



def get_s3_keys_specified(bucket_name, prefix_list, client):
    """
    This function returns all the S3 keys associated with the entire
    USA Structures Dataset by Oak Ridge National Laboratory on Source Cooperative. This function
    only lists the files in GeoParquet format.
    For more information about the dataset, visit 
    (https://source.coop/repositories/wherobots/usa-structures/description).


    Inputs:
    --------
    bucket_name : string 
        A sting indicating the Source Cooperative user that uploaded the dataset.
    prefix_list : list of strings
        A list of strings that contains each of the parquet file names that the dataset offers.
    client : boto3 client object 
        A s3 client returned by boto3.client.


    Returns:
    --------
    keys: list
        List of all keys in the dataset.
    """
    keys = []

    for i in prefix_list:
        response = client.list_objects_v2(Bucket=bucket_name, Prefix=i)
        for obj in response['Contents']:
            keys.append(obj['Key'])

    return keys


def get_US_structures_specified(bucket_name, link_list, s3_client, local_path, blocksize="256M"):
    """
    This function downloads geoparquet files from the USA Structures Dataset by Oak Ridge National Laboratory on Source Cooperative
    (https://source.coop/repositories/wherobots/usa-structures/description). 

    Inputs:
    --------
    s3_client: boto3 resource client
        A boto3 resource client configured with AWS credentials and the endpoint_url for Source Cooperative
    local_path: string
        Path to a local directory for downloading the geoparquet file(s) (example: "./data/")
    blocksize: string
        Blocksize used to load the geoparquet with Dask DataFrame. Default is 256M.

    Returns:
    --------
    bldg_ddf: Dask-Geopandas GeoDataFrame
        Structures footprint dataset in a Dask-Geopandas GeoDataFrame with lazy loading. 
 
    """

    # Since I updated get_s3_keys to handle a list of links, we do not need to worry about iterating through 'links' here.
    keys = get_s3_keys_specified(bucket_name, link_list, s3_client)


    for key in keys:
        local_fname = f"{local_path}/{key.split('/')[-1]}"  # May need to change
        if not os.path.exists(local_path):
            os.mkdir(local_path)

        if not os.path.exists(local_fname):
            print(f"File not found locally. Downloading from s3...")
            
            try:
                s3_client.download_file(Bucket = bucket_name,
                                        Key = key,
                                        Filename = f"./data/{key.split('/')[-1]}"  # May need to change
                                    )
                print("Download complete.")
            except ClientError as error:
                if error.response["Error"]["Code"] == "404":
                    print("The specified key does not exist in the bucket.")
                else:
                    print(f"An error occurred: {error}")
            except Exception as error:
                print(f"An unexpected error occurred: {error}")
        else:
            print("File already exists locally. No download needed.")


    # UPDATE, Reading documentation file explains it needs to be a list of file paths so we should copy the format for Hamed's example but for each "link"
    # that we add to this variable.
    local_file_names = [f"{local_path}/{key.split('/')[-1]}" for key in keys] # Now, it will be "(local_path)/part-(specified-number)-(ending)"

    structures_ddf = dg.read_parquet(local_file_names, gather_spatial_partitions=False, blocksize = blocksize)

    return structures_ddf
