{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["u"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["u"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":3}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":[" "],"id":4}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":[" "],"id":5},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["i"]}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":6}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["d"],"id":7}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["d"],"id":8}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":23},"end":{"row":14,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1562178737080,"hash":"31d5367a6c5c98f33e880da6100c9bae4bceee78"}