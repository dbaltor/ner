from flask import Flask, render_template, request
import json
import spacy
from ner_client import NamedEntityClient

app = Flask(__name__)

nlp = spacy.load('en_core_web_sm')
ner = NamedEntityClient(nlp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ner', methods=['POST'])
def get_named_ents():
    data = request.get_json()
    result = ner.get_ents(data['sentence'])
    response = { 'entities': result.get('ents') }
    return json.dumps(response)


if __name__ == '__main__':
    app.run(debug=True)
