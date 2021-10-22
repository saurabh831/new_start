import json
import random
import csv

with open("German.json") as file:
    data = json.load(file)

def get_response(s, t):
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern == s:
                for tg in intent["tag"]:
                    for q in t:
                        if tg == q:
                            a = intent["responses"]
                            return random.choice(a)
    return "wrong pattern"


def get_contxt(s, t):
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern == s:
                for tg in intent["tag"]:
                    for q in t:
                        if tg == q:
                            b = intent["context_set"]
                            return b


def get_tag(s, t):
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern == s:
                for tg in intent["tag"]:
                    for q in t:
                        if tg == q:
                            return q


def convrt_json():
    with open('Conversation.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = {"intent": []}
        for row in reader:
            print(row)
            data["intent"].append({"pattern": row[0], "response": row[1]})

    with open("new_intent.json", "w") as file:
        json.dump(data, file, indent=4)




