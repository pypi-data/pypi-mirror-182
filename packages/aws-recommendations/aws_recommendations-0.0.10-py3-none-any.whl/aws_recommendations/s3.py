from botocore.exceptions import ClientError

from aws_recommendations.utils import *


# Generate the recommendation for enable s3 bucket keys
def enable_s3_bucket_keys(self) -> list:
    """
    :param self:
    :return:
    """
    logger.info(" ---Inside s3 :: enable_s3_bucket_keys()")

    recommendation = []

    client = self.session.client('s3')

    response = client.list_buckets()

    for bucket in response['Buckets']:
        try:
            res = client.get_bucket_encryption(
                Bucket=bucket['Name']
            )
        except ClientError as e:
            continue
        for rule in res['ServerSideEncryptionConfiguration']['Rules']:
            if rule['ApplyServerSideEncryptionByDefault']['SSEAlgorithm'] == 'aws:kms' and rule['BucketKeyEnabled']:
                temp = {
                    'Service Name': 'S3',
                    'Id': bucket['Name'],
                    'Recommendation': 'Enable s3 bucket keys',
                    'Description': 'Enable s3 bucket keys instead of KMS keys to optimize the aws cost',
                    'Metadata':{

                    },
                    'Recommendation Reason': {
                        # 'Average CPU Datapoints(7 days)': [float('{:.2f}'.format(x)) for x in tmp_lst_cpu]
                        'reason': 'KMS keys are used for encryption'
                    }
                }
                recommendation.append(temp)

    return recommendation


