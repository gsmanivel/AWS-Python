import boto3

class ClientLocator:
    def __init__(self, client):
        self.client = boto3.client(client, region_name='ap-south-1')

    def get_client(self):
        return self.client