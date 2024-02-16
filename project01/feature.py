from flask import Flask

FAI = Flask(__name__)

@FAI.route('/stringresponse')
def stringresponse():
    return 'this is my first view'

@FAI.route('/secondstringresponse')
def secondstringresponse():
    return 'this is my second view'

if __name__ == '__main__':
    FAI.run(debug = True)