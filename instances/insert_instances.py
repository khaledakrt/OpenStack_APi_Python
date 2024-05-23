import requests
import mysql.connector

# Configuration de la base de données
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Mettez votre mot de passe MySQL ici
    'database': 'openstack'
}

# Connexion à la base de données
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Configuration de l'API OpenStack
auth_token = 'your token here'
api_url = 'http://192.168.XXX.XXX:XXXX/v2.1/servers'

# Récupération des instances depuis l'API
response = requests.get(api_url, headers={'X-Auth-Token': auth_token})
servers = response.json()['servers']

# Insertion des données dans la table de la base de données
for server in servers:
    server_id = server['id']
    server_name = server['name']
    
    # Récupération des détails de l'instance
    details_url = f"{api_url}/{server_id}"
    details_response = requests.get(details_url, headers={'X-Auth-Token': auth_token})
    server_details = details_response.json()['server']
    addresses = server_details.get('addresses', {})
    
    # Extraction des adresses IP privées et flottantes
    private_ips = []
    floating_ips = []
    for network_name, network_info in addresses.items():
        for info in network_info:
            if info['OS-EXT-IPS:type'] == 'fixed':
                private_ips.append(info.get('addr'))
            elif info['OS-EXT-IPS:type'] == 'floating':
                floating_ips.append(info.get('addr'))
    
    private_ip_str = ', '.join(private_ips) if private_ips else None
    floating_ip_str = ', '.join(floating_ips) if floating_ips else None
    status = server_details.get('status', 'Unknown')
    
    # Requête SQL pour l'insertion des données
    query = """
    INSERT INTO instances (server_id, server_name, private_ips, floating_ips, status)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (server_id, server_name, private_ip_str, floating_ip_str, status)
    cursor.execute(query, values)

# Valider les modifications et fermer la connexion
conn.commit()
cursor.close()
conn.close()
