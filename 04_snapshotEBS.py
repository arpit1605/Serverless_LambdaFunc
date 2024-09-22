import boto3
import datetime

# Initialize EC2 client
ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    # Specify the EBS volume ID to back up
    volume_id = 'vol-0d5bb3b09f6109756'
    
    # Create a snapshot of the specified EBS volume
    response = ec2_client.create_snapshot(
        VolumeId=volume_id,
        Description=f'Snapshot of volume {volume_id} on {datetime.date.today()}'
    )
    snapshot_id = response['SnapshotId']
    print(f'Created snapshot: {snapshot_id}')
    
    # Set the retention period to 7 days
    retention_days = 7
    deletion_date = datetime.datetime.now() - datetime.timedelta(days=retention_days)
    
    # Find and delete snapshots older than the retention period
    snapshots = ec2_client.describe_snapshots(
        Filters=[{'Name': 'volume-id', 'Values': [volume_id]}],
        OwnerIds=['self']  # Owned by the current account
    )
    
    for snapshot in snapshots['Snapshots']:
        snapshot_date = snapshot['StartTime'].replace(tzinfo=None)
        if snapshot_date < deletion_date:
            snapshot_id = snapshot['SnapshotId']
            ec2_client.delete_snapshot(SnapshotId=snapshot_id)
            print(f'Deleted old snapshot: {snapshot_id}')
    
    return {
        'statusCode': 200,
        'body': f'New Snapshot created and old snapshots has been cleaned up for the volume {volume_id}.'
    }
