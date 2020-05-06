
class VPC:
    def __init__(self,client):
        self.dr=client;
        """ :type : pyboto3.ec2 """

    def createVPC(self):
        print("Creating VPC")
        response= self.dr.create_vpc(CidrBlock='10.10.0.0/16')
        print("Created VPC")
        return response
        print("------------------------------------------")

    def addTags(self,resources,resource_name):
        print("Adding Tags for the Resource:: " + resources + " And the resource Name is :: "+ resource_name)
        self.dr.create_tags(
                Resources =[resources],
                Tags =  [{
                   'Key': 'Name',
                   'Value' : resource_name
               }]
        )
        print("Added tags for ::" + resources  +" successfully")
        print( "------------------------------------------" )

    def create_InternetGateway(self):
        print("Creating InternetGateWay")
        response= self.dr.create_internet_gateway()
        print("Created IGW")
        print( "------------------------------------------" )
        return response

    def attach_IGW(self,igwId,vpcId):
        self.dr.attach_internet_gateway(InternetGatewayId=igwId,VpcId=vpcId)

    def detach_IGW(self,igwId,vpcId):
        self.dr.detach_internet_gateway(InternetGatewayId=igwId,VpcId=vpcId)

    def delete_IGW(self,igwId):
        self.dr.delete_internet_gateway(InternetGatewayId=igwId)

    def delete_Vpc(self,vpcId):
        self.dr.delete_vpc(VpcId=vpcId)