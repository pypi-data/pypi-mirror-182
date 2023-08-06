import boto3

# Set the AWS credentials
aws_access_key_id = 'AKIAYWD4BDNSS4EU4M53'
aws_secret_access_key = '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'

# Create a client for the STS service
sts_client = boto3.client(
    'sts',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# Call the get_caller_identity method to get the caller's identity
identity = sts_client.get_caller_identity()

# Print the caller's identity
print(identity)

