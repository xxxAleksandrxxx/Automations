from flask import Flask, request, jsonify, send_file
import requests
import process_text
import tts
import asyncio
from zipfile import ZipFile

# create Flask app object
app = Flask(__name__)

# apply decorators 
@app.route('/clear', methods=['POST'])
def clear_text():
    # expecting there was text key in json we got from request
    data = request.json
    if 'text' not in data:
        return jsonify({'error' : 'Missing "text" field'}), 400
    input_text = data['text']
    result = process_text.clean_text(input_text)
    return jsonify({'result' : result})

@app.route('/tts', methods=['POST'])
def text_to_sound():
    # expecting there were text,  key in json we got from request
    data = request.json
    print(data)
    # if 'text' not in data:
    #     return jsonify({'error' : 'Missing "text" field'}), 400
    # file_name = request.form['file_name']
    
    # TEXT_1 = data['text'][0]
    # VOICE_1 = data['voice'][0]
    # OUTPUT_FILE_1 = data['file_name'][0]
    # asyncio.run(tts.run(TEXT_1, VOICE_1, OUTPUT_FILE_1))

    
    FILE_0 = data['file_name'][0]
    FILE_1 = data['file_name'][1]
    asyncio.gather(
        tts.run(data['text'][0], data['voice'][0], FILE_0),
        tts.run(data['text'][1], data['voice'][1], FILE_1)
    )
    OUTPUT_FILE = 'audios.zip'
    with ZipFile(OUTPUT_FILE, 'w') as z:
        z.write(FILE_0)
        z.write(FILE_1)
    
    return send_file(OUTPUT_FILE, as_attachment=True)



# run the web app
if __name__ == '__main__':
    app.run(debug=True)
