import os, json
from flask import Flask, Markup, request, render_template
import utils

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	data = utils.fetch_all()
	return json.dumps(data)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)