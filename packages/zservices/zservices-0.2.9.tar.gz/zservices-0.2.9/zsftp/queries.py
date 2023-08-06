from zsftp.sftp import SFTP
from zsftp import logger


# todo retry for each query


class SFTPQueries:
    def __init__(self, connection_params=None):
        logger.info('[SFTP]: Initiating SFTPQueries Class')
        self.connection_params = connection_params
        self.client = SFTP(self.connection_params).connection

    def upload_file(self, local_path, sftp_path):
        try:
            response = self.client.put(local_path, sftp_path)
            logger.info(f'[SFTP]: File uploaded {sftp_path}')
            return response
        except Exception as e:
            logger.warning(f'[SFTP]: Unable to upload file={local_path} on sftp server at ={sftp_path}, e= {e}')
            raise e

    def make_directory(self, directory_name):
        try:
            self.client.mkdir(directory_name)
            logger.info(f'[SFTP]: Directory Created {directory_name}')
        except Exception as e:
            logger.warning(f'[SFTP]: Unable to create directory = {directory_name}, e= {e}')
            raise e

    def list_directory(self, path="."):
        try:
            dir_list = self.client.listdir(path=path)
            return dir_list
        except Exception as e:
            logger.warning(f'[SFTP]: Unable to list directory {path}, e= {e}')
            raise e

    def upload_file_from_memory_bytes(self, io_bytes, sftp_path, **kwargs):
        try:
            response = self.client.putfo(io_bytes, sftp_path)
            logger.info(f'[SFTP]: File uploaded {sftp_path}')
            return response
        except Exception as e:
            logger.warning(f'[SFTP]: Unable to upload file from memory on sftp server at ={sftp_path}, e= {e}')
            raise e
