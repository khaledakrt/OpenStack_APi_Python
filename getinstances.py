import requests
import json
from tabulate import tabulate

# Configuration
auth_token = 'here_your_token'
api_url = 'http://192.168.XXX.XXX:XXXX/v2.1/servers'

# Récupération des instances
response = requests.get(api_url, headers={'X-Auth-Token': auth_token})
servers = response.json()['servers']

# Préparation des données pour l'affichage
table_data = []
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
    
    private_ip_str = ', '.join(private_ips) if private_ips else 'No private IPs'
    floating_ip_str = ', '.join(floating_ips) if floating_ips else 'No floating IPs'
    status = server_details.get('status', 'Unknown')
    
    table_data.append([server_id, server_name, private_ip_str, floating_ip_str, status])

# Affichage des résultats
headers = ["ID", "Name", "Private IP Addresses", "Floating IP Addresses", "Status"]
print(tabulate(table_data, headers, tablefmt="grid"))
