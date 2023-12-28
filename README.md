# Shakespeare scraper

This repository contains 

- A script that scrape the [Shakespeare](http://shakespeare.mit.edu/) website and save the plays in CSV files.
- A script that parses the html files and saves the plays in CSV format.

The CSV files have the following header: 

    Chapter,Player,Line,Line ID,Stage Direction

[bin/fetch_html.py](bin/fetch_html.py) is the script used to fetch the html files from MIT.

[bin/generate_csv.py](bin/generate_csv.py) is used to generate a CSV file per play and a file containinger all plays.

Inside [html](html) there are the HTML files for each play.

Inside [csv](csv) there are the CSV files for each play.

Full CSV file: [csv/all.csv](csv/all.csv)
