"""
Author: Mehakpreet Kaur
Date: October 16, 2024
Description: Challenge 7B - Web Scraping
"""
from html.parser import HTMLParser
import requests

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.colors = {}  # Dictionary to store color names and hex values
        self.current_color = False  # Flag to identify if we're reading a color name
        self.current_hex = False  # Flag to identify if we're reading a hex value
        self.td_count = 0  # Counter to keep track of <td> elements

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.td_count = 0  # Reset counter for each new row

        if tag == "td":
            self.td_count += 1  # Increment the counter for each <td>

            # Set flags based on the position of the <td>
            if self.td_count == 1:  # First <td> is the color name
                self.current_color = True
            elif self.td_count == 2:  # Second <td> is the hex value
                self.current_hex = True

    def handle_data(self, data):
        # Store color name
        if self.current_color:
            color_name = data.strip()
            self.colors[color_name] = None  # Initialize color in the dict
            self.current_color = False  # Reset after storing

        # Store hex value
        if self.current_hex:
            hex_value = data.strip()
            last_color = list(self.colors.keys())[-1]  # Get the last inserted color name
            self.colors[last_color] = hex_value  # Assign hex value to the color name
            self.current_hex = False  # Reset after storing

# Fetch the webpage content
url = "https://www.colorhexa.com/color-names"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    myparser = MyHTMLParser()
    myparser.feed(response.text)

    # Output the results in the desired format
    for color_name, hex_code in myparser.colors.items():
        print(f"{color_name} {hex_code}")

    # Print the total number of colors found
    print(f"\nTotal colors: {len(myparser.colors)}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
