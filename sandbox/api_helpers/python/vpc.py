import boto3

def create_vpc():
    ec2 = boto3.client("ec2")  # uses AFT region automatically

    response = ec2.create_vpc(
        CidrBlock="10.0.0.0/16"
    )

    vpc_id = response["Vpc"]["VpcId"]
    print(f"VPC Created: {vpc_id}")

    # Add Name tag
    ec2.create_tags(
        Resources=[vpc_id],
        Tags=[{"Key": "Name", "Value": "aft-test-vpc"}]
    )

    print("Tag added")

if __name__ == "__main__":
    create_vpc()