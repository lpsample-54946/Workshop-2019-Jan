"""
Copyright (c) 2018 Cisco and/or its affiliates.
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
We will be using the requests package for HTTP requests and the
csv package to generate an inventory file
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
    # Insert code here.  Assign the token to a variable named 'dnatoken'

    """
    For repeatability, set the headers we'll use
    """
    headers = {'Content-type': 'application/json',
               'x-auth-token': dnatoken
               }

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
    # Replace the values below with what we expect to see in the JSON response...
    # csvheader = [hostname, serial, platform, MAC, version]

    """
    Begin iterating over the inventory returned from Cisco DNA center.
    """
    while True:
        # Find the correct URL and modify the below variable accordingly.
        # url = "{0}/".format(baseurl, start, end)

        # Task: send the correct request to the URL.  Convert to JSON, and show the response.
        # r = requests.

        """
        Remember, if the response is an empty list, we're at the end and can break.
        If the response isn't empty, do something!
        """
        if r != []:
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

                # Task: iterate over the values of 'csvheader' - if a value is found for each
                # of those keys, EXTEND the 'fields' list.
                #
                # for ...
                    # Dynamically get values for each CSV header field
                    # Task: Replace '...var...' with a valid value:

                    # fields.extend( ...var...)

                # Task: Append the 'fields' list to the 'devices' list
                # ...append...

            """
            We've iterated over the first (step) devices in the inventory.  Now
            increment the start and end values by (step) in preparation of the
            next iteration.
            """
            # Task: increment the start and end variables by the value of 'step':
            # start += ...var...
            # end += ...var...
        else:
            """
            Empty list encountered in the HTTP response.  Exit the loop and create
            a CSV file
            """
            break
    """
    Open a new file handle for writing named 'invfile'
    We will write the CSV header first, followed by each row of the 'devices' list
    which contains the final inventory:
    """

    with open(inventoryfile, 'w') as invfile:
        # Instantiate a new csv 'writer' to the destination file 'invfile'
        wr = csv.writer(invfile)
        wr.writerow(csvheader)

        """
        Iterate over each row in the 'devices' list, writing a new line for
        each row.
        """
        # Task: iterate over the 'devices' variable and put a new row in the CSV:
        # for ...
            # Write a row to the CSV...


    # Task: Now that we've seen to open a file for writing, open the file for
    # reading and print each line of the CSV.
    # Hint: argument 'w' was used in the open statement above to open the file
    # for WRITING.  Argument 'r' will be needed to open for READING.

    # 1. Open the file for reading.
    # ...
        # 2. Iterate over each line of the CSV and print the result.
        #    HINT: to remove any extra new lines, use the 'rstrip' method
        #    to remove the newline, represented as '\n'


