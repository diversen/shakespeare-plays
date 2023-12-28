import csv

csv_file = "./csv/shakespeare.csv"

# Csv has the following columns:
# "Dataline","Play","PlayerLinenumber","ActSceneLine","Player","PlayerLine"

# Fetch all lines where the play is "Hamlet"

# Open the file
with open(csv_file, "r") as f:
    # Read the file
    csv_reader = csv.reader(f)
    # Skip the header
    next(csv_reader)
    # Iterate over the lines
    for line in csv_reader:
        # If the play is "Hamlet"
        if line[1] == "Hamlet":

            # Is "ActSceneLine" is empty then it is a stage direction
            if line[3] == "":
                player = line[4]
                print(f"{player}. Stage: {line[5]}")
            else:
                print(f"{player}. Speak: {line[5]}")
            # Print the line
            # print(line)