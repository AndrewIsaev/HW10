from flask import Flask
from utils import *
app = Flask(__name__)

@app.route("/")
def page_main():
    return f"{get_all()}"
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
