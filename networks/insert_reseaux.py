import requests
import mysql.connector

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Remplacez par votre nom d'utilisateur MySQL
    password="",  # Remplacez par votre mot de passe MySQL
    database="openstack"
)
cursor = conn.cursor()

# URL de l'API OpenStack pour récupérer les réseaux
api_url = "http://192.168.XXX.XXX:XXXX/v2.0/networks"

# Token d'authentification
auth_token = 'your token here'

# Entête de la requête avec le token d'authentification
headers = {'X-Auth-Token': auth_token}

# Récupération des réseaux depuis l'API OpenStack
response = requests.get(api_url, headers=headers)
networks_data = response.json()

# Vérification de la réussite de la requête
if response.status_code == 200:
    networks = networks_data.get('networks', [])
    for network in networks:
        # Parcours des sous-réseaux de ce réseau
        for subnet_id in network['subnets']:
            # URL de l'API OpenStack pour récupérer les informations sur le sous-réseau
            subnet_url = f"http://192.168.122.100:9696/v2.0/subnets/{subnet_id}"
            # Récupération des informations sur le sous-réseau depuis l'API OpenStack
            subnet_response = requests.get(subnet_url, headers=headers)
            subnet_data = subnet_response.json()
            if subnet_response.status_code == 200:
                subnet_info = subnet_data.get('subnet', {})
                # Insérer les données sur le sous-réseau dans la table networks
                cursor.execute("INSERT INTO networks (id_reseau, name, status, subnet_name, subnet_ipv4) VALUES (%s, %s, %s, %s, %s)", 
                               (network['id'], network['name'], network['status'], subnet_info.get('name'), subnet_info.get('cidr')))
            else:
                print("Erreur lors de la récupération des informations sur le sous-réseau:", subnet_response.text)

    # Valider les changements dans la base de données
    conn.commit()
    print("Données insérées avec succès dans la table networks.")

else:
    print("Erreur lors de la récupération des réseaux:", response.text)

# Fermer le curseur et la connexion à la base de données
cursor.close()
conn.close()
