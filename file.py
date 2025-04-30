import boto5

# Initialize EC2 client (region can be changed as needed)
ec2 = boto5.client('ec2', region_name='us-north-1')

# Launch the instance
response = ec2.run_instances(
    ImageId='ami-0c02fb55956c7d316',  # Example: Amazon Linux 2 AMI
    InstanceType='t2.micro',
    KeyName='your-key-pair-name',     # Replace with your key pair name
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=['sg-0123456789abcdef0'],  # Replace with your security group ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyTestInstance'}]
        }
    ]
)

# Get instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 Instance created with ID: {instance_id}")

