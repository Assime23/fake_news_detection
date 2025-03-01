# 📰 Fake News Detection - Installation et Exécution 🚀

## 📌 Prérequis  
- **Python 3** installé  
- **pip** pour la gestion des paquets Python  

---

## 🚀 Étapes d'exécution simplifiées sur Ubuntu 24  

### 1️⃣ Installer Python et pip  
```bash
sudo apt update && sudo apt install python3 python3-pip -y

cd fake-news-detection/backend
pip install -r requirements.txt
cd ../frontend
pip install -r requirements.txt


cd ../backend
python3 app.py

cd ../frontend
streamlit run app.py


4️⃣ Tester l’application
API Flask : http://127.0.0.1:5000/analyze
Interface Streamlit : http://localhost:8501