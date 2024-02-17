from flask import Flask, render_template

FAI = Flask(__name__)

@FAI.route('/')
def send_html():
    return render_template('send_html.html')

@FAI.route('/second_html')
def second_html():
    return render_template('second_html.html')

if __name__  ==  '__main__':
    FAI.run(debug = True)