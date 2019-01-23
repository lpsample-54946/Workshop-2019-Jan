"""
Copyright (c) 2019 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

"""
Import required packages
"""
import requests
import csv

"""
Set global variables
"""
# Cisco DNA Center connection variables:
dna_host = ""
dna_port = "443"
dna_username = ""
dna_password = "!"

# Set the base URL for API calls
baseurl = "https://{0}:{1}".format(dna_host, dna_port)

# Name of the CSV file for the inventory output
inventoryfile = "inventory.csv"



if __name__ == "__main__":
    """
    Connect to Cisco DNA Center and get a token
    """
    url = "{0}/dna/system/api/v1/auth/token".format(baseurl)
    print("Sending POST request to {}".format(url))
    r = requests.post(url, auth=(dna_username, dna_password))
    r = r.json()
    print("Received response: {}\n".format(r))
    dnatoken = r['Token']

    """
    For repeatability, set the headers we'll use
    """
    headers = {'Content-type': 'application/json',
               'x-auth-token': dnatoken
               }
    print("Headers initialized:\n{}\n".format(headers))

    """
    We don't want to be overwhelmed with data, so let's process
    100 devices at a time (we can change this number using the 'step'
    variable defined below).  There's an API call which allows us to
    get a pagination range of devices... we need a start index and
    an end index for each request.  When we hit the end, the response
    should contain an empty list aka []
    """
    step = 100
    start = 1
    end = step

    """
    Initialize an empty list to hold the device information.  Each row
    in this list will contain information for a single device.
    """
    devices = list()
    """
    The CSV file will contain a header.  The header fields will match the
    JSON keys for the information we're looking for.  The field names were
    obtained initially by looking at the output from a Postman call
    """
    csvheader = ['hostname', 'serialNumber', 'platformId', 'macAddress', 'softwareVersion']
    # Print the CSV headers without brackets:
    print("The CSV headers will be:\n{}\n".format(str(csvheader).strip('[]')))

    """
    Begin iterating over the inventory returned from Cisco DNA center.
    """
    while True:
        url = "{0}/dna/intent/api/v1/network-device/{1}/{2}".format(baseurl, start, end)
        print("Sending GET request to: {}".format(url))
        r = requests.get(url, headers=headers)
        r = r.json()
        r = r['response']
        print("Received response: {}\n".format(r))

        """
        Remember, if the response is an empty list, we're at the end and can break.
        If the response isn't empty, do something!
        """
        if r != []:
            print("Data in response!  Processing...")
            for device in r:
                """
                Initialize an empty list.  We will begin populating rows for the
                'devices' list initialized earlier.
                The idea here is that we can change which values we want to put in
                the CSV file based on the 'csvheader' fields.
                To accomplish this, we will EXTEND the 'fields' list with each value
                found from the 'csvheaders' variable.  Once we're iterated over all
                the headers, APPEND the 'devices' master list with the 'fields' list
                created here.  That will add a new row to our CSV file.
                """
                fields = list()
                for head in csvheader:
                    print("\tKey {0} has value {1} - adding to the 'fields' list".format(head,device[head]))
                    # Dynamically get values for each CSV header field
                    fields.extend( [device[head]])
                # Append the 'fields' list to the 'devices' list
                print("Appending '{0}' to the devices list...\n".format(fields))
                devices.append(fields)
            """
            We've iterated over the first (step) devices in the inventory.  Now
            increment the start and end values by (step) in preparation of the
            next iteration.
            """
            print("All devices processed.  Incrementing the start and end values by {}".format(step))
            start += step
            end += step
        else:
            """
            Empty list encountered in the HTTP response.  Exit the loop and create
            a CSV file
            """
            print("Empty list received - no more data to process!\n")
            break
    """
    Open a new file handle for writing named 'invfile'
    We will write the CSV header first, followed by each row of the 'devices' list
    which contains the final inventory:
    """
    print("Opening file '{}' for writing:".format(inventoryfile))
    with open(inventoryfile, 'w') as invfile:
        # Instantiate a new csv 'writer' to the destination file 'invfile'
        wr = csv.writer(invfile)
        print("New CSV writer initialized...")
        # Write the CSV Header row to the destination file
        print("Writing row to CSV:\n\t{}".format(csvheader))
        wr.writerow(csvheader)
        """
        Iterate over each row in the 'devices' list, writing a new line for
        each row.
        """
        for row in devices:
            print("Writing row to CSV:\n\t{}".format(row))
            wr.writerow(row)
    print("Closing CSV file...")

    print("VERIFY - open '{}' for reading".format(inventoryfile))
    with open(inventoryfile, 'r') as invfile:
        print("Contents of '{}':\n".format(inventoryfile))
        for row in invfile:
            # Print each line, removing any newline characters
            print(row.rstrip('\n'))

