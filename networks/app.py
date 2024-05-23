from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Remplacez par votre nom d'utilisateur MySQL
    password="",  # Remplacez par votre mot de passe MySQL
    database="openstack"
)
cursor = conn.cursor()

@app.route('/')
def index():
    # Récupération des données depuis la table networks
    cursor.execute("SELECT * FROM networks")
    networks_data = cursor.fetchall()
    # Fermer la connexion à la base de données
    cursor.close()
    conn.close()
    # Rendre la page HTML et transmettre les données au modèle
    return render_template('index.html', networks=networks_data)

if __name__ == '__main__':
    app.run(debug=True)
