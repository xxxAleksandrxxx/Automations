from flask import Flask, request, jsonify
import requests
import re

# # function to process the text
# def process_text(input_text):
#     return input_text.upper()

branch = 'main'
# branch = 'test'
# branch = 'test_2'


def process_text(input_text):
    # clean trash before
    t = input_text.replace('\n', ' ')
    patterns_before = requests.get(f'https://raw.githubusercontent.com/xxxAleksandrxxx/Automations/{branch}/iOS%20Shortcuts/Duolingo%20companion/dict_before.json').json()
    for k, v in patterns_before.items():  
        if k[1:] in t:
            pattern = f'{v}(.+)'
            t = re.search(pattern, t).group(1)

    # clean trash after
    patterns_after = requests.get(f'https://raw.githubusercontent.com/xxxAleksandrxxx/Automations/{branch}/iOS%20Shortcuts/Duolingo%20companion/dict_after.json').json()
    for k, v in patterns_after.items():
        if k[1:] in t:
            pattern = f'(.+){v}'
            t = re.search(pattern, t).group(1)

    # clean text from everything after •
    while "•" in t:
        pattern = r'(.+[.?!]) {1,3}[•]'
        t = re.search(pattern, t).group(1)

    # if after .?! symbols we have small letter - it means that it's trash; clean it
    pattern = r'(.+[.?!]) {1,3}[a-z]'
    match = re.search(pattern, t)
    if match:
        t = match.group(1)

    # if after cleaning the text starts with 5G or 4G, clean it more
    #pattern = r'^(5G |4G )(.+)'
    #match = re.findall(pattern, t)
    #if match:
    #    t = match[0][1]
    print("Here is text before check for startswith 5G or 4G")
    print(t)
    if t.startswith('5G '): t = t[3:]
    if t.startswith('4G '): t = t[3:]
    print("Text after check for 5G or 4G")
    print(t)
    print("\n\n")

    print('This is what we have before check for 一===一')
    print(t)
    if '一===一' in t:
        t = t.replace('一===一 ', '')
    print("It's after the check for 一===一")
    print(t)
    
    return t


# create Flask app object
app = Flask(__name__)

# apply decorator 
@app.route('/', methods=['POST'])
def api():
    data = request.json
    if 'text' not in data:
        return jsonify({'error' : 'Missing "text" field'}), 400
    input_text = data['text']
    result = process_text(input_text)
    return jsonify({'result' : result})




# run the web app
if __name__ == '__main__':
    app.run(debug=True)
