# Shakespeare scraper

This is a simple script that scrapes the [Shakespeare](http://shakespeare.mit.edu/) website and saves the plays in html files. There is also a script that parses the html files and saves the plays in a CSV files.

The CSV files have the following header: 

    Chapter,Player,Line,Line ID,Stage Direction

[fetch_html.py](fetch_html.py) is the script that scrapes the website and saves the html files.

[generate_csv.py](generate_csv.py) is takes all the html files and generates a CSV file per play.

Inside [html](html) there are the html files for each play.

Inside [csv](csv) there are the CSV files for each play.

Full CSV file: [all.csv](csv/all.csv)
