"""
Script for fetching all links pointing to Shakespeare plays 
Fetched from the MIT website.
They are saved to html files in the html folder.
"""

import requests
import ssl
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from bs4 import BeautifulSoup
import json


class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.set_ciphers("DEFAULT@SECLEVEL=1")
        kwargs["ssl_context"] = ctx
        return super(MyAdapter, self).init_poolmanager(*args, **kwargs)


# URL to parse
url = "https://shakespeare.mit.edu"

# Create a requests session
session = requests.Session()
session.mount("https://", MyAdapter())

# Fetch the HTML content from the URL using the adjusted session
response = session.get(url)
html_content = response.text

# Fetch all 'a' inside the 2. table and iterate over them
soup = BeautifulSoup(html_content, "html5lib")

"""
Inside the 2. table there are links to all plays. 
These links are only inside the first 3 columns of the table.
The links are in a tags inside td tags.
"""
plays_meta = []

table = soup.find_all("table")[1]
for row in table.find_all("tr"):
    for column in row.find_all("td")[:3]:
        for link in column.find_all("a"):
            play_meta = {}

            # Get the link
            link_url = link.get("href")

            # split link url by '/' and get the first element
            # this is the play's path
            link_url = "/" + link_url.split("/")[0] + "/full.html"

            # Get the play name
            play_name = link.text.strip()

            # change new lines to spaces
            play_name = play_name.replace("\n", " ")

            # change spaces to underscores
            play_name_file = play_name.replace(" ", "_")

            # to lowercase
            play_name_file = play_name_file.lower()

            # remove any non alphanumeric characters except underscores
            play_name_file = "".join(
                c for c in play_name_file if c.isalnum() or c == "_"
            )
            
            play_name_html = f"{play_name_file}.html"
            play_name_csv = f"{play_name_file}.csv"

            play_file = f"./html/{play_name_html}"

            play_meta["name"] = play_name
            play_meta["file_name_html"] = play_name_html
            play_meta["file_name_csv"] = play_name_csv

            # Fetch the HTML content from the URL using the adjusted session
            response = session.get(url + link_url)
            html_content = response.text

            # Save the HTML content to a file
            with open(play_file, "w") as f:
                f.write(html_content)

            plays_meta.append(play_meta)

            # write the play meta to a json file
            with open("./plays_meta.json", "w") as f:
                json.dump(plays_meta, f, indent=4)
