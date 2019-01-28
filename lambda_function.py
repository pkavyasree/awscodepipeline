import boto3

session = boto3.Session(region_name="us-east-1")

ec2 = session.resource('ec2')

def running():

    print("The Running instances are")

    rinstances = ec2.instances.filter(

        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    for instance in rinstances:

        print(instance.id, instance.instance_type)

def stopped():

    print("The Stopped instances are")

    sinstances = ec2.instances.filter(

        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

    for instance1 in sinstances:

        print(instance1.id, instance1.instance_type)

running()

stopped()

