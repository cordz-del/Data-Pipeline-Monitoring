# cloudwatch_logger.py
import boto3
import time

def send_log_to_cloudwatch(log_group, log_stream, message):
    client = boto3.client('logs', region_name='us-east-1')
    # Create log group and stream if they don't exist
    try:
        client.create_log_group(logGroupName=log_group)
    except client.exceptions.ResourceAlreadyExistsException:
        pass
    try:
        client.create_log_stream(logGroupName=log_group, logStreamName=log_stream)
    except client.exceptions.ResourceAlreadyExistsException:
        pass
    timestamp = int(round(time.time() * 1000))
    response = client.put_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        logEvents=[{'timestamp': timestamp, 'message': message}]
    )
    return response

if __name__ == "__main__":
    response = send_log_to_cloudwatch("MyLogGroup", "MyLogStream", "Test log message from CloudWatch.")
    print("CloudWatch response:", response)
