import streamlit as st
import requests
from streamlit_extras.colored_header import colored_header

# Configuration de la page
st.set_page_config(
    page_title="NewsCheck BF",
    page_icon="✅",
    layout="centered"
)

# Style CSS personnalisé
st.markdown("""
<style>
    .stTextArea [data-baseweb=base-input] {
        background-color: #f9f9f9;
        border-radius: 10px;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        font-size: 1.1em;
    }
    .fake-news {
        background-color: #ffebee;
        color: #c62828;
        border: 2px solid #ef9a9a;
    }
    .true-news {
        background-color: #e8f5e9;
        color: #2e7d32;
        border: 2px solid #a5d6a7;
    }
</style>
""", unsafe_allow_html=True)

# En-tête
colored_header(
    label="📰 NewsCheck Burkina Faso",
    description="Vérifiez la crédibilité des informations sur la sécurité",
    color_name="blue-70"
)

# Zone de texte pour l'entrée utilisateur
texte_input = st.text_area(
    "Entrez le contenu à vérifier :",
    placeholder="Exemple : 'Une attaque terroriste a été signalée à Ouagadougou...'",
    height=150
)

# Bouton d'analyse
if st.button("🔍 Analyser la crédibilité", type="primary", use_container_width=True):
    if texte_input:
        with st.spinner("Analyse en cours..."):
            try:
                response = requests.post("http://127.0.0.1:5000/analyze", json={"texte": texte_input})
                
                if response.status_code == 200:
                    result = response.json()
                    confidence = round(float(result['confidence'].replace('%', '')), 1)
                    
                    # Affichage des résultats
                    if result['prediction'] == 0:  # Fake News
                        st.markdown(f"""
                        <div class="result-box fake-news">
                            <h3>🚨 Information potentiellement fausse</h3>
                            <p>Confiance : {confidence}%</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:  # True News
                        st.markdown(f"""
                        <div class="result-box true-news">
                            <h3>✅ Information probablement fiable</h3>
                            <p>Confiance : {confidence}%</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Barre de progression
                    st.progress(confidence / 100, text=f"Niveau de confiance : {confidence}%")
                else:
                    st.error("Erreur lors de l'analyse. Veuillez réessayer.")
            except Exception as e:
                st.error(f"Erreur de connexion : {str(e)}")
    else:
        st.warning("Veuillez entrer un texte à analyser.")

# Section d'information
with st.expander("ℹ️ Comment ça marche ?"):
    st.markdown("""
    - **Analyse linguistique** : Utilisation de modèles IA avancés.
    - **Base de données** : Comparaison avec des faits vérifiés.
    - **Détection** : Identification des marqueurs de désinformation.
    """)

# Avertissement légal
st.caption("⚠️ Cet outil fournit une indication automatisée. Vérifiez toujours avec des sources officielles.")