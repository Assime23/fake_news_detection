from flask import Flask, request, jsonify
from model import analyze_text
from db import save_analysis

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    texte = data.get("texte", "")
    if not texte:
        return jsonify({"error": "Texte requis"}), 400
    
    prediction, confidence = analyze_text(texte)
    save_analysis(texte, prediction, confidence)
    
    return jsonify({
        "texte": texte,
        "prediction": prediction,
        "confidence": f"{confidence * 100:.2f}%"
    })

if __name__ == "__main__":
    app.run(debug=True)