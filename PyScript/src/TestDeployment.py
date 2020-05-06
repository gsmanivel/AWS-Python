from src.ec2.vpc import VPC
from src.ClientLocator import ClientLocator


def main():
    ec2_client = ClientLocator( 'ec2' ).get_client()
    vpc_obj = VPC( ec2_client )

    # Create VPC
    vpc_response = vpc_obj.createVPC()

    # Create Tags to the VPC
    vpc_id = vpc_response['Vpc']['VpcId']
    vpc_Name = 'manman-new-VPC'
    vpc_obj.addTags( vpc_id, vpc_Name )

    # Create Internet Gateway
    igwId = vpc_obj.create_InternetGateway()['InternetGateway']['InternetGatewayId']
    vpc_obj.addTags( igwId, "manman_igw" )

    # Attach Internet Gateway
    vpc_obj.attach_IGW(igwId, vpc_id)

    print("Detaching and Deleting the resources")
    vpc_obj.detach_IGW( igwId, vpc_id )
    vpc_obj.delete_IGW( igwId )
    vpc_obj.delete_Vpc( vpc_id )
    print( "Deleted the resources" )


if __name__ == '__main__':
    main()