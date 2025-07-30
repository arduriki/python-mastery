import csv

# f is an alias of the file
# it automatically closes the file once it's done.
with open("week2/netflix_titles.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[2])
