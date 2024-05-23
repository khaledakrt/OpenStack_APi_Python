from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Nom d'utilisateur MySQL
    password="",  # Mot de passe MySQL
    database="openstack"
)
cursor = conn.cursor()

@app.route('/')
def index():
    # Récupération des données depuis la base de données
    cursor.execute("SELECT * FROM images")
    data = cursor.fetchall()
    # Fermer la connexion à la base de données
    cursor.close()
    conn.close()
    # Rendre la page HTML et transmettre les données au modèle
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
