import urllib
import boto3

class S3Event:

    def __init__(self, bucket_id, file_name, response_object) -> None:
        self.bucket_id = bucket_id
        self.file_name = file_name
        self.response_object = response_object


def extract_s3_event(event) -> S3Event:
    # parse out the bucket id, this is the name of the bucket.
    s3_event = event['Records'][0]['s3']
    bucket_id = s3_event['bucket']['name']

    print(f"Bucket: {bucket_id}")

    # Extract the file name from the event. It is stored in Records.s3.object.key
    file_name = urllib.parse.unquote_plus(s3_event['object']['key'], encoding='utf-8')

    # Fetch the file from s3
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_id, Key=file_name)

    return S3Event(bucket_id=bucket_id, file_name=file_name, response_object=response)
