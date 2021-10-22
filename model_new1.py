import nltk
from nltk.stem.lancaster import LancasterStemmer
from tensorflow.python.framework import ops
import numpy
import tflearn
from nltk.corpus import stopwords
import tensorflow
import random
import json

stemmer = LancasterStemmer()

stopwords = set(stopwords.words('german'))
stopwords.add("?")

with open("new_german.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []


def remove_(msg):
    resul = [i for i in msg if not i in stopwords]
    return resul


for intent in data["intents"]:
    for pattern in intent["patterns"]:
        b = stemmer.stem(pattern.lower())
        wrds = nltk.word_tokenize(b)
        a = remove_(wrds)
        print(a)
        words.extend(a)
        print(words)
        docs_x.append(a)
        print(docs_x)
        docs_y.append(intent["tag"])
        print(docs_y)

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)


training = numpy.array(training)
output = numpy.array(output)

ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(training, output, n_epoch=5000, batch_size=10, show_metric=True)
model.save("model.tflearn")


