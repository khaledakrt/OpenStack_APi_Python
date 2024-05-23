# OpenStack_APi_Python
Python scripts designed to display information about images, instances, and networks from an OpenStack

# OpenStack Data Viewer

This project contains Python scripts designed to display information about images, instances, and networks from an OpenStack database in a simple web interface.

## Features

- Display information about images, instances, and networks in separate tables on a web interface.
- Use Flask to create the user interface.
- Integration with a MySQL database to retrieve data.

## Usage

1. Clone the GitHub repository:

```bash
git clone https://github.com/khaledakrt/OpenStack_APi_Python

- Install the necessary dependencies with: pip install flask mysql-connector-python requests.

- cd Openstack_get_informations
- In the files: getFlavorRef.py, getImageRef.py, getNetworkId.py, get_token.py, getinstances.py: try to change the parameters: URL of your server, and your server's token.
- Start by retrieving the authentication token from OpenStack using the file: get_token.py. Try to input your personal information such as username, password, and project name.

Then start by executing the files "getFlavorRef.py, getImageRef.py, getNetworkId.py, getinstances.py" to display the results in JSON format or create a database "openstack" with tables "images", "instances", and "networks" with these column names. Try inserting the data from OpenStack into the database and displaying it on a web interface.



