from transformers import AutoTokenizer
from gliner import GLiNER

def extract_entities(text):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased", use_fast=False, max_length=512, truncation=True)
    model = GLiNER.from_pretrained("urchade/gliner_mediumv2.1")
    labels = ["Name", "Location", "Emergency"]
    entities = model.predict_entities(text, labels, threshold=0.5)

    results = {label: [] for label in labels}
    for entity in entities:
        results[entity["label"]].append(entity["text"])
    return results
