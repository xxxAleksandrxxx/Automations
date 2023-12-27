from flask import Flask, request, jsonify, send_file
import requests
import process_text
import tts
import asyncio

# create Flask app object
app = Flask(__name__)

# apply decorator 
@app.route('/clear', methods=['POST'])
def api():
    data = request.json
    if 'text' not in data:
        return jsonify({'error' : 'Missing "text" field'}), 400
    input_text = data['text']
    result = process_text.clean_text(input_text)
    return jsonify({'result' : result})

@app.route('/tts', method=['POST'])
def api():
    # data = request.json
    # if 'text' not in data:
    #     return jsonify({'error' : 'Missing "text" field'}), 400
    # file_name = request.form['file_name']
    TEXT = "Hello World!"
    VOICE = "en-GB-SoniaNeural"
    OUTPUT_FILE = "test.mp3"
    tts.run(TEXT, VOICE, OUTPUT_FILE)
    # await tts.run(TEXT, VOICE, OUTPUT_FILE)  # 'await' outside async function


# run the web app
if __name__ == '__main__':
    app.run(debug=True)
