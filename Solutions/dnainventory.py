"""
Import required packages
"""
import requests
import csv

"""
Set global variables
"""
dna_host = ""
dna_port = "443"
dna_username = ""
dna_password = ""

baseurl = "https://{0}:{1}".format( dna_host, dna_port)

inventoryfile = "inventory.csv"

"""
Connect to Cisco DNA Center and get a token
"""
url = "{0}/dna/system/api/v1/auth/token".format( baseurl)
r = requests.post( url, auth=(dna_username, dna_password))
r = r.json()
dnatoken = r['Token']

print( dnatoken)

"""
For simplicity, set the headers we'll use
"""
headers = { 'Content-type': 'application/json',
            'x-auth-token': dnatoken
            }

"""
We don't want to be overwhelmed with data, so let's process
100 devices at a time.  There's an API call which allows us to
get a pagination range of devices... we need a start index and
an end index for each request.  When we hit the end, the response
should contain an empty list aka []
"""
start = 1
end = 100

"""
Iterate over the requests until response is empty
"""
# Create loop...
if __name__ == "__main__":
    devices = list()
    csvheader = ['hostname', 'serialNumber', 'platformId', 'macAddress', 'softwareVersion']
    devices.append(csvheader)


    while True:
        url = "{0}/dna/intent/api/v1/network-device/{1}/{2}".format(baseurl, start, end)
        r = requests.get( url, headers=headers)
        r = r.json()
        r = r['response']
        # inventory = getInventory( url)
        if r != []:
            print( r)
            for device in r:
                row = [ device['hostname'], device['serialNumber'], device['platformId'],
                        device['macAddress'], device['softwareVersion'] ]
                devices.append( row)
            start += 100
            end += 100
            url = "{0}/dna/intent/api/v1/network-device/{1}/{2}".format(baseurl, start, end)
        else:
            break

    with open( inventoryfile, 'w') as invfile:
        wr = csv.writer( invfile)
        for row in devices:
            wr.writerow( row)
