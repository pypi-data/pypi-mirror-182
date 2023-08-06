import os
from random import randint
from subprocess import Popen, PIPE


class GetS3Handler:
    """Returns an object with methods to interact with aws S3 storage service.
    
    This module allows the user to interact with S3 storage service.

    The module contains the following functions:

    - `get_buckets()` - Returns List of all S3 buckets of an aws account.
    - `list_bucket()` - Returns List of all the objects in the bucket/bucket_path recursively.
    - `upload_to_s3()` - Upload files/folders to s3 bucket.
    - `download_from_s3()` - Download files/folders from s3 bucket.
    
    Example : 
        ```
        >> from satsure_cloud_utils import GetS3Handler
        >> s3_handler = GetS3Handler( 
                            access_key_id = "",
                            secret_access_key="",
                            session_token="" 
                            )
        >> output = s3_handler.get_buckets()
        >> print(output)
        ```

    """
    AWS_PROFILE_NAME = ""
    def __init__(self, 
                 access_key_id: str, 
                 secret_access_key: str, 
                 session_token: str, 
                 region: str ="ap-south-1"):
        
        self.AWS_PROFILE_NAME = f"""user_{randint(999,9999)}"""
        
        command = f"""aws configure set default.region {region} --profile {self.AWS_PROFILE_NAME}; aws configure set aws_access_key_id '{access_key_id}' --profile {self.AWS_PROFILE_NAME}; aws configure set aws_secret_access_key '{secret_access_key}' --profile {self.AWS_PROFILE_NAME}; aws configure set aws_session_token '{session_token} ' --profile {self.AWS_PROFILE_NAME};"""
        
        process = Popen(command,shell=True,stdout=PIPE)
        stdout, _ = process.communicate()
    
        self._get_connection_details()
        
    def _get_connection_details(self):
        command = f"aws sts get-caller-identity --profile {self.AWS_PROFILE_NAME} --output json"

        process = Popen(command,shell=True,stdout=PIPE)
        stdout, _ = process.communicate()
        print(stdout.decode("utf-8"))
        
    
    def get_buckets(self):
        """Lists all s3 buckets of an aws account
          
        Returns:
            string: output/error string
        """
        command = f"aws s3api list-buckets --profile {self.AWS_PROFILE_NAME} --output json"

        process = Popen(command,shell=True,stdout=PIPE)
        stdout, _ = process.communicate()
        return stdout.decode("utf-8")

    def list_bucket(self,
                    bucket_name: str,
                    files_path: str =""):
        
        """Lists all the objects in the bucket/bucket_path recursively

        Args:
            bucket_name (string): Name of the bucket
            files_path (string): Path of files in bucket (Default: '')
        Returns:
            string: output/error string
        """
        command = f"aws s3api list-objects --bucket {bucket_name} --prefix '{files_path}' --profile {self.AWS_PROFILE_NAME} --output json"
        
        process = Popen(command,shell=True,stdout=PIPE)
        stdout, _ = process.communicate()
        return stdout.decode("utf-8")
    
    def upload_to_s3(self,
                     bucket_name: str,
                     s3_path: str,
                     local_path: str =".",
                     exclude: str ="",
                     include: str ="*",
                     content_type: str =""):
        """Upload files/folders to s3 bucket
        
        Args:
            bucket_name (string): Name of bucket
            s3_path (string): Path on s3 bucket
            local_path (string): Local path on your machine (Default : '.')
            exclude (string): file patterns to exclude (Default: '')
            include (string): file patterns to include (Default: '*')
            content-type (string): content-type of files (Default: '')
            
        Returns:
            string: output/error string
        """
        
        if os.path.isdir(local_path):
            command = f"""aws s3 cp "{local_path}" "s3://{bucket_name}/{s3_path}" --recursive --exclude "{exclude}" --include "{include}"  --profile {self.AWS_PROFILE_NAME} --output json"""
        else:
            command = f"""aws s3 cp "{local_path}" "s3://{bucket_name}/{s3_path}" --exclude "{exclude}" --include "{include}"  --content-type "{content_type}" --profile {self.AWS_PROFILE_NAME} --output json"""
        
        process = Popen(command,shell=True,stdout=PIPE)
        stdout, _ = process.communicate()
        return stdout.decode("utf-8")
        

    def download_from_s3(self,
                         bucket_name: str,
                         s3_path: str ,
                         local_path: str =".",
                         exclude: str ="",
                         include:str ="*"):
        """Download files/folders from s3 bucket
        
        Args:
            bucket_name (string): Name of bucket
            s3_path (string): path on s3 bucket
            local_path (string): Path on your machine (Default : '.')
            exclude (string): file patterns to exclude (Default: '')
            include (string): file patterns to include (Default: '*')
            
        Returns:
            string: output/error string
        """
        if os.path.isdir(local_path):
            command = f"""aws s3 cp "s3://{bucket_name}/{s3_path}" "{local_path}" --recursive --exclude "{exclude}" --include "{include}" --profile {self.AWS_PROFILE_NAME} --output json"""
        else:
            command = f"""aws s3 cp "s3://{bucket_name}/{s3_path}" "{local_path}" --exclude "{exclude}" --include "{include}" --profile {self.AWS_PROFILE_NAME} --output json"""
            
        process = Popen(command,shell=True,stdout=PIPE)
        stdout, _ = process.communicate()
        return stdout.decode("utf-8")
