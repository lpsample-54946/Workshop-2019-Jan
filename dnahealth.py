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
"""
# import ...

"""
Set global variables
"""
dna_host = ""
dna_port = ""
dna_username = ""
dna_password = ""

"""
Connect to Cisco DNA Center and get a token
"""
#...

"""
For simplicity, set the headers we'll use
"""
# headers = ...

"""
Create a timestamp for the health query
"""
# timestamp = ...

"""
We need to update some headers to get health synchronously.
Create a copy of the headers so we don't modify the original
for future requests and add the new fields
"""
# newheaders = ...

"""
Send a request to Cisco DNA Center and get the health data
"""
# Send the HTTP request

# Get the response

# Convert the response to JSON

"""
Now let's see what the response contains.  Maybe there's something
interesting here...
"""
# Print the response data

"""
Iterate over the response and get some health data.  We'll start
by printing a hierarchy of all site health data
"""
# Process the response and print health data