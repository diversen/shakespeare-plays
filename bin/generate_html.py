"""
Script that generates html files from the csv files
These are saved to docs/

"""
import json
import os

# read plays_meta.json
with open("./plays_meta.json", "r") as f:
    plays_meta = json.load(f)

    for play_meta in plays_meta:
        name = play_meta["name"]
        file_name = play_meta["file_name"]

        if file_name != "hamlet":
            continue
        
        command = f'pandoc -s md/{file_name}.md -o docs/{file_name}.html --toc --metadata title="{name}" --template=template.html'

        os.system(command)
        # exit()

# print(plays_meta)
