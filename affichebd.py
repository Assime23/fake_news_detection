import sqlite3

# Demander à l'utilisateur le chemin de la base de données
db_path = "backend/fake_news.db"

try:
    # Connexion à la base de données
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Récupérer les tables de la base de données
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if not tables:
        print("❌ Aucune table trouvée dans la base de données.")
    else:
        print("\n📌 Tables disponibles :")
        for i, table in enumerate(tables, 1):
            print(f"{i}. {table[0]}")
        
        # Sélectionner une table
        table_name = "analyses"
        
        # Vérifier si la table existe
        if (table_name,) in tables:
            # Récupérer les colonnes de la table
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            print("\n📊 Informations sur la table :", table_name)
            print("📌 Colonnes disponibles :")
            for col in columns:
                print(f"- {col[1]} (Type: {col[2]})")
            
            # Lire les premières données
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 40;")
            rows = cursor.fetchall()
            
            print("\n🔍 Aperçu des 10 premières lignes :")
            for row in rows:
                print(row)
        
        else:
            print("❌ La table sélectionnée n'existe pas.")

except sqlite3.Error as e:
    print(f"❌ Erreur SQLite : {e}")

finally:
    if 'conn' in locals():
        conn.close()
