import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')

    # Get all instances with the 'Auto-Stop' tag
    auto_stop_instances = ec2_client.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Arpit-Auto-Stop']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    # Get all instances with the 'Auto-Start' tag
    auto_start_instances = ec2_client.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Arpit-Auto-Start']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    # Stop the instances with the tag 'Auto-Stop'
    stop_instance_ids = [instance['InstanceId'] 
                         for reservation in auto_stop_instances['Reservations']
                         for instance in reservation['Instances']]
    
    if stop_instance_ids:
        ec2_client.stop_instances(InstanceIds=stop_instance_ids)
        print(f'Stopped instances: {stop_instance_ids}')
    else:
        print('No running instances with Auto-Stop Tag to stop.')

    # Start the instances with the tag 'Auto-Start'
    start_instance_ids = [instance['InstanceId'] 
                          for reservation in auto_start_instances['Reservations']
                          for instance in reservation['Instances']]

    if start_instance_ids:
        ec2_client.start_instances(InstanceIds=start_instance_ids)
        print(f'Started instances: {start_instance_ids}')
    else:
        print('No stopped instances with Auto-Start Tag to start.')

    return {
        'statusCode': 200,
        'body': ' Automated Instance Management is completed'
    }
