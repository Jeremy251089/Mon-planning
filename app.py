import streamlit as st
import pandas as pd
from datetime import time, datetime

# Configuration de la page
st.set_page_config(page_title="BricoPlan - Weldom", layout="wide")

# --- STYLE PERSONNALISÉ ---
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { background-color: #008D36; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIMULATION DE BASE DE DONNÉES ---
if 'employees' not in st.session_state:
    st.session_state.employees = ["Jean-Marc", "Sophie", "Lucas", "Amandine", "Thomas"]
if 'sectors' not in st.session_state:
    st.session_state.sectors = ["Bâti / Matériaux", "Décoration / Peinture", "Outillage", "Jardin", "Caisse / Accueil"]

# --- SIDEBAR (Navigation) ---
st.sidebar.title("🛠️ BricoPlan v1.0")
page = st.sidebar.radio("Navigation", ["Vue d'ensemble", "Éditeur de Planning", "Paramètres"])

# --- PAGE : ÉDITEUR DE PLANNING ---
if page == "Éditeur de Planning":
    st.header("📅 Gestion des plannings hebdomadaires")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.subheader("Nouvelle Entrée")
        emp = st.selectbox("Collaborateur", st.session_state.employees)
        sector = st.selectbox("Rayon / Zone", st.session_state.sectors)
        date_plan = st.date_input("Date")
        h_start = st.time_input("Heure de début", time(9, 0))
        h_end = st.time_input("Heure de fin", time(18, 0))
        
        if st.button("Ajouter au planning"):
            st.success(f"Planning mis à jour pour {emp}")

    with col2:
        st.subheader("Visualisation")
        # Simulation d'un tableau de données
        data = {
            "Employé": ["Sophie", "Lucas", "Jean-Marc"],
            "Zone": ["Caisse", "Bâti", "Outillage"],
            "Début": ["08:30", "10:00", "09:00"],
            "Fin": ["16:30", "19:00", "18:00"]
        }
        df = pd.DataFrame(data)
        st.table(df)

# --- PAGE : VUE D'ENSEMBLE ---
elif page == "Vue d'ensemble":
    st.header("📊 État du magasin - Aujourd'hui")
    
    metrics = st.columns(4)
    metrics[0].metric("Présents", "8 / 12")
    metrics[1].metric("Ouverture Caisse", "3")
    metrics[2].metric("Zone Bâti", "Occupée")
    metrics[3].metric("Alertes pauses", "1")

    st.subheader("Répartition par rayon")
    chart_data = pd.DataFrame({
        'Rayon': st.session_state.sectors,
        'Effectif': [2, 3, 2, 4, 1]
    })
    st.bar_chart(chart_data.set_index('Rayon'))
