from  flask import Flask

from fileworker import filescanner
from db import create_db

app = Flask(__name__)

if __name__ == "__main__":
    create_db()
    scanner = filescanner.Scanner(["Y:\\Serien"])
    scanner.scan()
