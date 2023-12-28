# Shakespeare's plays

This repository contains HTML and CSV versions of all Shakespeare's plays.

The downloaded HTML files: [html](html). They are downloaded from [https://shakespeare.mit.edu/ ](https://shakespeare.mit.edu/)

The exported CSV files: [csv](csv).

All exported plays as a single CSV file can be found in [csv/all.csv](csv/all.csv)

The CSV files have the following header: 

    Title,Chapter,Player,Line,Line ID,Stage Direction

The script [bin/generate_csv.py](bin/generate_csv.py) is used to generate the CSV files.

The script [bin/fetch_html.py](bin/fetch_html.py) is used to fetch the HTML files from MIT.

