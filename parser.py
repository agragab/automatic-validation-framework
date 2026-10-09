import json
import sys

def read_json():
    
    try:
        with open (sys.argv[1], "r") as file:
            json_reader = json.load(file)
            return json_reader
    except FileNotFoundError as e:
        print("File not found in directory, please check again")    
    except json.JSONDecodeError as e:
        print("JSON Decode Error Detected:")
        print(f"Error Line: {e.lineno}")
        print(f"Error Character: {e.pos}")
