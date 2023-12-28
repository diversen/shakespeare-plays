import csv

csv_file = "./csv/hamlet.csv"
                
# Header is Chapter,Player,Line,Line ID,Stage Direction
with open(csv_file, "r") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for line in csv_reader:
        print(line)
