Quick Deployer Python SDK
A Python SDK for interacting with the Quick Deployer API to manage projects and servers.
Installation
pip install quick-deployer-sdk

Usage
from quick_deployer_sdk import QuickDeployerClient

# Initialize the client
client = QuickDeployerClient(base_url='https://quickdeployer.com/api', api_key='your-api-key')

# Check API health
health = client.check_health()
print(health)

# List projects
projects = client.projects().list()
print(projects)

# Create a project
new_project = client.projects().create({'name': 'My Project'})
print(new_project)

# List servers for a project
servers = client.servers(project_id='project-id').list()
print(servers)

# Check server status
status = client.servers(project_id='project-id').check_status(server_id='server-id')
print(status)

Requirements

Python 3.7+
requests library

License
MIT License
