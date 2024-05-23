import mysql.connector
import requests

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Nom d'utilisateur MySQL
    password="",  # Mot de passe MySQL
    database="openstack"
)
cursor = conn.cursor()

# Récupération des données depuis l'API
res = requests.get('http://192.168.XXX.XXX:XXXX/v2/images',
                   headers={'content-type': 'application/json',
                            'X-Auth-Token': 'your token here'
                            },
                   )
data = res.json()['images']

# Insertion des données dans la base de données
for image in data:
    query = """
    INSERT INTO images (name, disk_format, container_format, visibility, size, status)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (image['name'], image['disk_format'], image['container_format'], image['visibility'], image['size'], image['status'])
    cursor.execute(query, values)

# Valider les modifications et fermer la connexion
conn.commit()
cursor.close()
conn.close()
