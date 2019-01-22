"""
Import required packages
We will be using the requests package for HTTP requests and the
csv package to generate an inventory file
"""
import requests
import csv

"""
Set global variables
"""
dna_host = ""
dna_port = ""
dna_username = ""
dna_password = ""

baseurl = ""

inventoryfile = "inventory.csv"

"""
Connect to Cisco DNA Center and get a token
"""
# Send a POST request to the proper URL and save the token

"""
For simplicity, set the headers we'll use
"""
# Create a dictionary which contains the Content-Type and x-auth-token
# header values.

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
Each program should use the following to test that we're entering
the actual script:
"""
if __name__ == "__main__":
    """
    Set some initial variables that will be used to collect data
    """
    # Define an empty list for the devices
    devices = list()

    """
    What values do we want for the CSV header?
    """
    csvheader = ["col1", "col2", "col3"]

    """
    Begin the list with the CSV header
    """
    devices.append( csvheader)

    """
    Iterate over a response
    Unless a specific condition is met, loop.  We want to get a URL and check
    the response.  Once we're out of devices, the response should be an empty list.
    At that point, exit the loop.
    As long as data is returned, we'll extract the key pieces and add a new entry
    to the list containing the data we want.
    """

    while True:
        # url = URL
        r = requests.get( url, headers=headers)
        """
        Convert the response to JSON and begin checking the data
        """
        # Convert and parse...

        """
        Test for an empty list.  If it's not empty, let's extract our stuff
        and append to the devices list
        """
        if r != []:
            """
            Iterate through the response and get interesting fields
            """
            row = [ device['field1'], device['field2'], device['...'] ]
            # Append this row to our inventory
            devices.append( row)
            """
            Increment our start page and end page by some value...
            """
            # start ... add 100
            # end ... add 100

            """
            Update the URL we'll access with the new start and end values.
            Nothing left after that, so the loop will iterate
            """
            # url = ...
    else:
        """
        The result is an empty set, so we'll end the loop here
        """
        break

    """
    We're outside the loop now and should have a full inventory.  Let's write it to a CSV!
    """
    # Open the CSV for writing.
    with open( inventoryfile, 'w') as invfile:
        # Instantiate a 'csv writer' instance, output to the opened file
        wr = csv.writer( invfile)
        """
        Iterate over each row in the 'devices' variable.  This should dump the contents to the CSV file
        """
        # Begin for loop
            # Write the inventory to the file

