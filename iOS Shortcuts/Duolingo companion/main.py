from flask import Flask, request, jsonify
import requests
import process_text


# create Flask app object
app = Flask(__name__)

# apply decorator 
@app.route('/', methods=['POST'])
def api():
    data = request.json
    if 'text' not in data:
        return jsonify({'error' : 'Missing "text" field'}), 400
    input_text = data['text']
    result = process_text.clean_text(input_text)
    return jsonify({'result' : result})




# run the web app
if __name__ == '__main__':
    app.run(debug=True)
