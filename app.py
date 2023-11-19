from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

def process_string(input_str):
    # Add prefix and suffix, remove spaces and specified words
    result_str = f".mx{re.sub(r'\s+', '.', input_str)}watch."
    result_str = re.sub(r'\b(?:NF|AMZN|WEBDL|WEBRIP)\b', '', result_str)

    return result_str

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        input_text = request.form['input_text']
        result = process_string(input_text)

    return render_template_string('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
