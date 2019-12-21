from flask import Flask, render_template, request
import unicodedata
from PIL import Image
import re
app = Flask(__name__)


@app.route('/')
def hello_world():
    return(render_template("index.html"))


@app.route('/api/test', methods=['POST'])
def test():
    project = request.get_json()
    projectpath = project['data']
    unicodedata.normalize('NFKD', projectpath).encode('ascii', 'ignore')
    print(projectpath)
    im = Image.open(projectpath)
    im.show()
    ## put in the model code here mam
    return("Sucess")

if __name__ == '__main__':
    app.run(debug=True)
