from flask import Flask, request, jsonify, send_file
import requests
import process_text
import tts
#import tts2
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
async def text_to_sound():
    # check the request content type
    if not request.json:
        return jsonify({'error': 'Invalid content type. Application/JSON expected.'}), 400
     
    data = request.json

    # check required fields 
    if 'text' not in data or 'voice' not in data or 'file_name' not in data:
        return jsonify({'error': 'Missing required fields: text, voice, file_name'}), 400

    print("data:", data)
    # if 'text' not in data:
    #     return jsonify({'error' : 'Missing "text" field'}), 400
    # file_name = request.form['file_name']
    
    # TEXT_1 = data['text'][0]
    # VOICE_1 = data['voice'][0]
    # OUTPUT_FILE_1 = data['file_name'][0]
    # asyncio.run(tts.run(TEXT_1, VOICE_1, OUTPUT_FILE_1))

    TEXTS = data['text'].split(':::')
    VOICES = data['voice'].split(':::')
    FILES = data['file_name'].split(':::')
    if 'rate' in data and data['rate']:
        RATE = data['rate']
    else:
        RATE = "+0%"
    if 'pitch' in data and data['pitch']:
        PITCH = data['pitch']
    else:
        PITCH = "+0Hz"

    print("TEXTS: ", TEXTS)
    print("VOICES:", VOICES)
    print("FILES: ", FILES)
    print("RATE:  ", RATE)
    print("PITCH: ", PITCH)
    
    tasks = [tts.run(t, v, RATE, PITCH, f) for t, v, f in zip(TEXTS, VOICES, FILES)]
    #tasks = [tts2.run(t, v, RATE, f) for t, v, f in zip(TEXTS, VOICES, FILES)]
    print('tasks:', tasks)
    
    await asyncio.gather(*tasks)
    
    OUTPUT_FILE = 'audios.zip'
    with ZipFile(OUTPUT_FILE, 'w') as z:
        for f in FILES:
            z.write(f)
    
    return send_file(OUTPUT_FILE, as_attachment=True)



# run the web app
if __name__ == '__main__':
    app.run(debug=True)
