import spacy

nlp = spacy.load("en_core_web_sm")

"""
paragraph = "I love studying NLP. It's amazing! I can't wait to build my own projects."

doc = nlp(paragraph)

for word in doc:
    print(word.text)

for s in doc.sents:
    print(s.text)
"""

paragraph = "My name is Shehroz. This is a paragraph. i dont don't know what i am writing but i am writing it anyway."

doc = nlp(paragraph)

temp1 = []
temp2 = []

for word in doc:
    temp1.append(word.text)

for sent in doc.sents:
    temp2.append(sent.text)

print(temp1)
print()
print(temp2)