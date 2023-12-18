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

    # # clean text from everything after •
    # if "•" in t:
    #     print('"•" in t')
    # else:
    #     print('"•" NOT in t:')
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
    if t.startswith('5G'): 
        t = t[3:]
    if t.startswith('4G'):
        t = t[3:]

    if t.startswith('5 '):
        t = t[2:]
    if t.startswith('4 '):
        t = t[2:]
    if t.startswith('3'):
        t = t[2:]
    if t.startswith('2'):
        t = t[2:]
    if t.startswith('1'):
        t = t[2:]

    # There could be two types strange symbols: 一===一 and —===—
    # Check for 一===一
    # print('Before 一===一 check')
    # print(t)
    if '一===一' in t:
        t = t.replace('一===一 ', '')
        # print("一===一 is in text")
    # else:
    #     print("一===一 is not in text")
    # print("After 一===一 check")
    # print(t)
    # Check for —===—
    if '—===—' in t:
        t = t.replace('—===— ', '')
    #     print("—===— is in text")
    # else:
    #     print("—===— is not in text")
    # print("After —===— check")
    # print(t)

    
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
