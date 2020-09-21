import boto3

ssm_client = boto3.client("ssm", region_name='sa-east-1')
response = ssm_client.get_parameter(Name="telegramLinarestoken", WithDecryption=True)
TELEGRAM_TOKEN = response["Parameter"]["Value"]

# AKIA2U5JANGQPRYLC3GE
# E7eiI0n+dUvBYaNxX7BsndzaqQmT+wrsJ/U0Rrva