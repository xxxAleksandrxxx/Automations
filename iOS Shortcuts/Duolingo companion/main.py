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

@app.route('/tts', methods=['POST'])
def api_2():
    # data = request.json
    print('request.json:', request.json)
    print('request.form:', request.form)
    # if 'text' not in data:
    #     return jsonify({'error' : 'Missing "text" field'}), 400
    # file_name = request.form['file_name']
    # TEXT = "Hello World!"
    TEXT = request.form['text']
    VOICE = "en-GB-SoniaNeural"
    # OUTPUT_FILE = "test.mp3"
    OUTPUT_FILE = request.form['file_name']
    # tts.run(TEXT, VOICE, OUTPUT_FILE)
    # await tts.run(TEXT, VOICE, OUTPUT_FILE)  # 'await' outside async function
    asyncio.run(tts.run(TEXT, VOICE, OUTPUT_FILE))
    return send_file(OUTPUT_FILE, as_attachment=True)



# run the web app
if __name__ == '__main__':
    app.run(debug=True)
