import boto3
client = boto3.client('ec2')
response = client.describe_instances()
instances = response.get('Reservations')[0].get('Instances')
new_variable = response.get('Reservations')
for instance in new_variable:
    state = instance.get('Instances')[0].get('State').get('Name')
    instance_id = instance.get('Instances')[0].get('InstanceId')
    if state == 'running':
        client.stop_instances(InstanceIds=[instance_id])
        print('The machine has been stopped' + instance_id)
    else:
        client.start_instances(InstanceIds=[instance_id])
        print('Starting the machine ' + instance_id)