import json
import pickle
from simple_classifier import SimpleClassifier

# Load intents
with open("training_data/intents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_words = []
tags = []
xy = []

# Tokenize and collect patterns
for intent in data["intents"]:
    tag = intent["tag"]
    tags.append(tag)
    for pattern in intent["patterns"]:
        words = pattern.lower().split()
        all_words.extend(words)
        xy.append((words, tag))

all_words = sorted(set(all_words))
tags = sorted(set(tags))

# Train model
model = SimpleClassifier(tags)
model.train(xy)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump((model, all_words, tags, data), f)

print("✅ Model trained and saved as model.pkl")
