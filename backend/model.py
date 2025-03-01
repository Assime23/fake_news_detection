from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

import os

MODEL_PATH = os.path.abspath("../model/checkpoint-126")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)


# Charger le modèle et le tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

def analyze_text(texte):
    inputs = tokenizer(texte, return_tensors="pt")
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    confidence = torch.softmax(outputs.logits, dim=1).max().item()
    return prediction, confidence