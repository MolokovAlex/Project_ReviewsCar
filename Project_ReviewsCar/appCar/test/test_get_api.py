import requests
import os
from pathlib import Path

url = [
    'http://localhost:8000/api/country/', 
    'http://localhost:8000/api/manuf/',
    'http://localhost:8000/api/car/',
    'http://localhost:8000/api/comment/'
    ]
TEST_DIR = "test\\"
NAME_OUTPUT_FILE = "out.txt"
BAS_DIR = Path(__file__).resolve().parent.parent
absDirTestFile = os.path.join(BAS_DIR, TEST_DIR)
asbPathTestFile = os.path.join(absDirTestFile, NAME_OUTPUT_FILE )


with open(asbPathTestFile, 'w') as file:
    for item_url in url:
        responseJSON = requests.get(item_url)
        responsePython = responseJSON.json()
        file.write(str(item_url)+"\n")
        for item in responsePython:
            for key, value in item.items():
                file.write(str(key)+": ")
                file.write(str(value)+"\n")
            file.write("\n")
        file.write("\n")
