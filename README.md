## Setup

```
virtualenv env -p=python3.12
source env/bin/activate
pip install pytest flask selenium webdriver-manager spacy==3.7.2 
python -m spacy download en_core_web_sm
```

Configure the project: see [setup.py](./setup.py)  
Then install the project as an editable package:  
```
pip install -e .
```

## SpaCy
SpaCy usage:
```
>>> import spacy
>>> nlp = spacy.load('en_core_web_sm')
>>> doc2 = nlp('Madison is a city in Wisconsin')
>>> doc2.ents
(Madison, Wisconsin)
>>> [(ent.text, ent.label_) for ent in doc2.ents]
[('Madison', 'PERSON'), ('Wisconsin', 'GPE')]
```

## Run
How to run:
```
python app.py
```
Open your browser at `http://localhost:5000`

## References
- [https://www.datacamp.com/blog/what-is-named-entity-recognition-ner](https://www.datacamp.com/blog/what-is-named-entity-recognition-ner)
- [https://www.youtube.com/watch?v=eAPmXQ0dC7Q](https://www.youtube.com/watch?v=eAPmXQ0dC7Q)
- [https://github.com/wesdoyle/flask-ner/tree/main](https://github.com/wesdoyle/flask-ner/tree/main)
