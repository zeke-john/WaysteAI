import sagemaker
import boto3

sm_boto3 = boto3.client("sagemaker")
sess = sagemaker.Session()
region = sess.boto_session.region_name

bucket = 'mobbucketsagemakertest'
print(bucket)