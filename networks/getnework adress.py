import requests

# URL de l'API OpenStack pour récupérer les réseaux
api_url = "http://192.168.XXXX.XXX:XXXX/v2.0/networks"

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
        print("Réseau:", network['name'])
        print("ID:", network['id'])
        print("Statut:", network['status'])
        print("Subnets:")
        # Parcours des sous-réseaux de ce réseau
        for subnet_id in network['subnets']:
            # URL de l'API OpenStack pour récupérer les informations sur le sous-réseau
            subnet_url = f"http://192.168.122.100:9696/v2.0/subnets/{subnet_id}"
            # Récupération des informations sur le sous-réseau depuis l'API OpenStack
            subnet_response = requests.get(subnet_url, headers=headers)
            subnet_data = subnet_response.json()
            if subnet_response.status_code == 200:
                subnet_info = subnet_data.get('subnet', {})
                print("  - Sous-réseau:", subnet_info.get('name'))
                print("    Adresse IP:", subnet_info.get('cidr'))
            else:
                print("Erreur lors de la récupération des informations sur le sous-réseau:", subnet_response.text)
else:
    print("Erreur lors de la récupération des réseaux:", response.text)
