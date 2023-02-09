from flask import Flask, render_template, url_for, request
import pickle
import joblib
import string
import re 
from costum import process_text as pt
import __main__
__main__.process_text = process_text

#Import process_text
app = Flask(__name__)

@app.before_first_request
def load_models():
	# from utils import tokenize

	global tfidf_model
	tfidf_model = joblib.load(open('trained_model.pkl','rb'))

@app.route('/')
def home():
	# return "ok"
	return render_template('index.php')

@app.route('/predict', methods=['GET', 'POST'])
def predict_fun():
	print('do a prediction')
	if request.method == 'POST':

		message = request.form['message']
		data = [message]
		pre = tfidf_model.predict(data)
	return render_template('result.html',prediction = pre[0], message = message)

if __name__ == '__main__':
	# print("HELLO")
	# print(pt)
	app.run(debug=True)
