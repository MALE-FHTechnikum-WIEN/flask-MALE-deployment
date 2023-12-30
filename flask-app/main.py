from flask import Flask, request, jsonify, render_template
from model import run_model

app = Flask(__name__)


'''
    A url/info endpoint that could be used as an API call, for example to a model
'''
@app.route('/info', methods=['GET'])
def info():
    return jsonify({'This app was created by:': ['Ernesto', 'Baptiste']})


'''
    We defined the root route the site, located at http://localhost:5000/
'''
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html', response="") # we return the HTML templates using the template located in the templates directory


    if request.method == 'POST':

        # Sepal_length and width are the names we gave our input in the html form, the name has to be given to retrieve the correct data
        sepal_length = request.form.get('sepal_length', '')
        sepal_width = request.form.get('sepal_width', '')

        # The answer variable is the variable which is the return of our function run_model in which we passed our prediction variable defined earlier
        answer = run_model(sepal_length, sepal_width)

        # In this template we passed our variable answer which will be now called 'response' in our HTML template
        return render_template('index.html', response=answer)


if __name__ == '__main__':
#For those who are not familiar with python or oriented-object, it's just the part of the code that execute everything
    app.run(host='0.0.0.0', debug=True)
