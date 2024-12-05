import os
import dask_geopandas as dg
import tqdm
from botocore.exceptions import ClientError


def get_s3_keys(bucket_name, prefix, client):
    """
    This function returns all the S3 keys associated with a country_code
    from the Google Open Building Dataset on Source Cooperative. This function
    only lists the files in GeoParquet format.
    For more information about the dataset, visit 
    https://source.coop/repositories/cholmes/google-open-buildings/description/
    
    
    Inputs:
    --------
    country_code : string 
        A sting indicating the country of target. Country code is the Alpha-2 code based on ISO 3166 standard.
    client : boto3 client object 
        A s3 client returned by boto3.client
    
    
    Returns:
    --------
    keys: list
        List of all keys that match the country_code
    """

    keys = []    

    response = client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    for obj in response['Contents']:
        keys.append(obj['Key'])

    return keys  

                  
def get_google_microsoft_bldgs(country_code, s3_client, local_path, blocksize="256M"):
    """
    This function download geoparquet files from the Google Microsoft Building Footprint - Combined by VIDA dataset hosted on Source Cooperative (https://source.coop/repositories/vida/google-microsoft-open-buildings/description). 
    
    Inputs:
    --------
    country_code: string
        Target country's name in ISO Alpha-3 format
    s3_client: boto3 resource client
        A boto3 resource client configured with AWS credentials and the endpoint_url for Source Cooperative
    local_path: string
        Path to a local directory for downloading the geoparquet file(s)
    blocksize: string
        Blocksize used to load the geoparquet with Dask DataFrame. Default is 256M.

    Returns:
    --------
    bldg_ddf: Dask-Geopandas GeoDataFrame
        Buildings footprint dataset in a Dask-Geopandas GeoDataFrame with lazy loading. 
        
    """
    
    bucket_name = 'vida'
    prefix = "google-microsoft-open-buildings/geoparquet/by_country/country_iso="
    country_prefix = f"{prefix}{country_code}"
    keys = get_s3_keys(bucket_name, country_prefix, s3_client)

    for key in keys:
        local_fname = f"{local_path}/{key.split("/")[-1]}"
        if not os.path.exists(local_path):
            os.mkdir(local_path)
            
        if not os.path.exists(local_fname):
            print(f"File not found locally. Downloading from s3...")
            
            try:
                s3_client.download_file(Bucket = bucket_name,
                                        Key = key,
                                        Filename = f"./data/{key.split("/")[-1]}"
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

    bldg_ddf = dg.read_parquet(f"./data/{country_code}*.parquet", gather_spatial_partitions=False, blocksize = blocksize)

    return bldg_ddf
