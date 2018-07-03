from flask import Flask, jsonify

app= Flask(__name__)

@app.route('/')
def index():
	return "hello world"

@app.route('/level/api/login', methods=['GET', 'POST'])
def login():
	pass


@app.route('/level/api/comments', methods=['GET'])
def comments():
	return jsonify({'comments': comments})

if __name__ == '__main__':
		app.run(debug=True)	