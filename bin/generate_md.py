""""
Script that generates markdown files from the csv files
"""

import json
import csv

# read plays_meta.json
with open("./plays_meta.json", "r") as f:
    plays_meta = json.load(f)


def convert_to_md(play_meta):
    # read csv
    with open(f"./csv/{play_meta['file_name']}.csv", "r") as f:
        reader = csv.DictReader(f)
        play_data = list(reader)

    markdown = ""

    # Iterate through the play data
    # Title,Chapter,Player,Line,Line ID,Stage Direction
    #
    # Title is a h1
    # Chapter is a h3
    # Player is bold
    # Line is a blockquote (Line ID is a attr on the Line blockquote)
    # If there is a Line then there is a Line ID
    # Stage Direction is a blockquote with italic text
    #
    # Iterate through the play data
    for row in play_data:
        # Title,Chapter,Player,Line,Line ID,Stage Direction
        if row["Title"]:
            markdown += f"# {row['Title']}\n\n"
        if row["Chapter"]:

            # to uppercase
            act_chapter = row["Chapter"].upper() 
            
            if act_chapter.startswith("ACT"):
                markdown += f"## {row['Chapter']}\n\n"
            else:
                markdown += f"### {row['Chapter']}\n\n"

        if row["Player"]:
            markdown += f"**{row['Player']}**\n\n"
        if row["Line"]:
            markdown += f"> {row['Line']}  \n\n"
        if row["Stage Direction"]:
            markdown += f"> *{row['Stage Direction']}*\n\n"

    # save file to ./md directory
    with open(f"./md/{play_meta['file_name']}.md", "w") as f:
        f.write(markdown)

    # pandoc -s md/alls_well_that_ends_well.md -o test.html


# iterate through the plays_meta
for play_meta in plays_meta:
    convert_to_md(play_meta)
    # exit()
