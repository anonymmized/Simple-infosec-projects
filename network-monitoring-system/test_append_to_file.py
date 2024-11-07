import os

filename = "data.txt"

def save_data(data):
    with open(filename, "a+") as file:
        file.seek(0)
        file.write(data + "\n")
data = ["Some text"]
for item in data:
    save_data(item)
