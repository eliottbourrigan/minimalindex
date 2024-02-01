import spacy

texts = [
    "Ceci est une phrase d'exemple.",
    "Je n'ai pas d'idées pour un autre exemple"
]

nlp = spacy.load("fr_core_news_sm")
for doc in nlp.pipe(texts, disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]):
    # Do something with the doc here
    print([(ent.text, ent.label_) for ent in doc.ents])