from bs4 import BeautifulSoup
import csv
import os


def html_to_csv(path):
    
    # e.g.: ./html/hamlet.html
    with open(path, "r") as f:
        html_content = f.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html5lib")

    # Create a data dictionary
    def get_data_dict():
        return {
            "Chapter": "",
            "Player": "",
            "Line": "",
            "Line ID": "",
            "Stage Direction": "",
        }

    play_data = []

    # Set a entry in the data play_data list
    def set_play_data(dict_values):
        data_dict = get_data_dict()
        for key, value in dict_values.items():
            
            # trim the value
            value = value.strip()
            data_dict[key] = value

        play_data.append(data_dict)

    # Iterate through the HTML elements
    for element in soup.body:
        
        # Check for chapter (scene) headlines
        if element.name == "h3":
            current_chapter = element.get_text()
            set_play_data({"Chapter": current_chapter})

        # Check for player
        elif element.name == "a" and element.b:
            current_player = element.b.get_text()
            set_play_data({"Player": current_player})

        # Check for line and line ID
        elif element.name == "blockquote":

            # find all a or i elements
            lines = element.find_all(["a", "i"])

            # iterate through the lines
            for line in lines:
                # if "a"
                if line.name == "a":
                    # get the line id
                    line_id = line["name"]
                    # get the line text
                    line_text = line.get_text()
                    set_play_data({"Line": line_text, "Line ID": line_id})

                # if "i"
                elif line.name == "i":
                    # get the stage direction
                    stage_direction = line.get_text()
                    set_play_data({"Stage Direction": stage_direction})

        # Check for stage directions
        elif element.name == "i":
            stage_direction = element.get_text()
            set_play_data({"Stage Direction": stage_direction})

    # Write the data to a CSV file
    play_name = path.split("/")[-1].split(".")[0]

    with open(f"./csv/{play_name}.csv", "w", newline="") as f:
        
        # Create the writer object
        writer = csv.DictWriter(
            f, fieldnames=["Chapter", "Player", "Line", "Line ID", "Stage Direction"]
        )

        # Write the header row
        writer.writeheader()

        # Write the data row by row
        writer.writerows(play_data)


# get all files in ./html directory
html_files = os.listdir("./html")

# iterate through the files
for html_file in html_files:
    html_to_csv(f"./html/{html_file}")
