import json

# read plays_meta.json
with open("./plays_meta.json", "r") as f:
    plays_meta = json.load(f)

# iterate through the plays_meta
for play_meta in plays_meta:
    # get the file name
    file_name = play_meta["file_name"]
    # print the file name
    print(file_name)
    # open the file
    with open(f"./html/{file_name}", "r") as f:
        # read the file
        html_content = f.read()
        # print the file
        print(html_content)
        # break
        break