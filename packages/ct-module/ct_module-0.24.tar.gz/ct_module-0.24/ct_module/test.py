import boto3
import csv
session = boto3.session.Session('ASIA54R2F7JLDHVYCJQS','xalxUj5ib1HfxcWa+xCIAo200VuQY0NyB3R67VrU','IQoJb3JpZ2luX2VjEFEaCXVzLWVhc3QtMSJGMEQCIE7O9bw1Pygf0ADTuDTLZzXotIMbfq/D5bvi6UaCdobFAiAIzUrUYOd02Y7BFy+9cXNGcxQ4hiMbMjf91UdWy5QxoSquAwiK//////////8BEAIaDDk1NDY3ODUwODExOCIMOIWEY7HIVxy469gfKoIDOXawuXT1SA569H8dGYjI/FfZ4vvoVjKN+Se08ymw11T4dO5SNFpasOfKv8OWVi2yaMcgkkTABT17sWDQ8+l4rgIFlh6T0u8EcgKnwU1X8NB40aryStxfU0eone2rB6I7bjYiUVZZD9kHHe/qo2Cmn/Iz6RaFNlb3hKBwR0H0ZGlcq3cez+xhA2zaXoefVTeJWJ1RbvOFp8coP4ne0HN++e7XkFgpt1Nt+kZ3KOUz8m4tYjYOjnGCqPHxmGLs0R+jR2m/ALwoh7bnCcV++zbJ12UY3zyX0KilhouCNzUtd2lDiAzz6m9tNS1azBD8AGFVboR5AZSN+KYBQ3euxBdunfFbPP/nUtXtefzFiFiFJB6EfGoTynaCJAFXL2Bw0gREdMtIruVt5QRyGNBQdgkaKwT1UzLq6bbv0uaGg9POCQ5Jr54cIpScU/QeOOAfqqNocbpTGFWN7xy+bcI9Hd9wApdjnm14fGLBaWGv/mG/IzYEA0G1fuauN01ArtuiON1P00kw0YaLnQY6pwGRRRqrgb6pJIKsA8OREboyqLC8OsbWhGa8L+yv/huAHqKx+ZFjozgx6a88Q0otulUMxXtKCeOnxLSO4ZETrr0EbbR7JqNw6nEi7KeDgj+vw4YkEIl99nRJlpUVLFtR7AEtG6n0UmCJ9Qr4Q452IIaoEkwaYkFDvaH17p5pRU1d4zNbPRsG74sPjDzSnzQwv/laNPd3RTnjQktbJCHaMDbJfzncVVBByg==')

client = session.client('ec2')
response = client.describe_nat_gateways()

header = ['NatGatewayId','State', 'Allocation_Id', 'Network_Interface_Id','Private_IP','Public_IP']
with open('NatGatewaydata.csv','w', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        gateways = response['NatGateways']
        for i in gateways:
            gatewayAddressess = i['NatGatewayAddresses']
            state = i['State']
            Allocation_id = gatewayAddressess[0]['AllocationId']
            NetworkInterfaceId = gatewayAddressess[0]['NetworkInterfaceId']
            Private_Ip = gatewayAddressess[0]['PrivateIp']
            Public_Ip = gatewayAddressess[0]['PublicIp']
            natgatewayid = i['NatGatewayId']
            data=[natgatewayid,state,Allocation_id,NetworkInterfaceId,Private_Ip,Public_Ip]
            print(data)
            writer.writerow(data)
