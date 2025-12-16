import json
import csv

def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def read_csv(file_path):
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)
