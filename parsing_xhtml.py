"""
Author: Mehakpreet Kaur
Date: October 16, 2024
Description: Challenge 9A - Revision control
"""
from html.parser import HTMLParser
import urllib.request

class IPParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ip_address = None

    def handle_data(self, data):
        # The unique piece of information preceding the IP address is 'Current IP Address: '
        if 'Current IP Address' in data:
            # Split the string and extract the IP address part
            self.ip_address = data.split(': ')[1]

# Create an instance of the parser
parser = IPParser()

# Fetch the webpage that contains the IP address
with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
    html = response.read().decode()

# Feed the HTML content to the parser
parser.feed(html)

# Print the extracted IP address (without any extra spaces or newlines)
if parser.ip_address:
    print(parser.ip_address.strip())
