class SimpleClassifier:
    def __init__(self, tags):
        self.tags = tags
        self.patterns = {}

    def train(self, xy):
        for words, tag in xy:
            key = " ".join(words)
            self.patterns[key] = tag

    def predict(self, words):
        for key in self.patterns:
            if all(w in key for w in words):
                return self.tags.index(self.patterns[key])
        return -1
