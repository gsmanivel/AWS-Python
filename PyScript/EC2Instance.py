import boto3

#client = boto3.client('ec2')
client = boto3.resource('ec2', region_name='ap-south-1')
resp = client.create_instances(
      ImageId='ami-0470e33cd681b2476',
      InstanceType='t2.micro',
      MinCount=1,
      MaxCount=1)


print(resp)

