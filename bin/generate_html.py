"""
Script that generates html files from the csv files
These are saved to docs/

"""
import json
import os

# read plays_meta.json
markdown_index = ""
with open("./plays_meta.json", "r") as f:
    plays_meta = json.load(f)

    for play_meta in plays_meta:
        name = play_meta["name"]
        file_name = play_meta["file_name"]

        # Generate a h3 link to the play
        markdown_index += f"[{name}](./{file_name}.html)  \n\n" 
        
        command = f'pandoc -s md/{file_name}.md -o docs/{file_name}.html --toc --metadata title="{name}" --template=template-play.html'
        os.system(command)

    # create md/all.md
    with open("./md/all.md", "w") as f:
        f.write(markdown_index)

    command = f'pandoc -s md/all.md -o docs/index.html --metadata title="All the plays by William Shakespeare" --template=template-index.html'
    os.system(command)
