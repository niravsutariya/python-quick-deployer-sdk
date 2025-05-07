# Python QuickDeployer SDK

The QuickDeployer SDK is a Python library for interacting with the QuickDeployer API, enabling developers to manage projects and servers programmatically. Designed for simplicity and modularity, it provides a clean interface for listing, creating, updating, and deleting projects and servers, with robust error handling and support for testing.

## Features
- Manage projects (list, get, create, update, delete).
- Manage servers within projects (list, get, create, update, delete, check status).
- Easy integration with Python applications, including Flask and Django.
- Comprehensive unit tests using pytest.
- Built with `requests` library for reliable API communication.

## Requirements
- Python 3.7+
- `requests` library (`requests>=2.25.0`)
- `pytest` (for running tests)

## Installation

Install the SDK via pip:

```bash
pip install quick-deployer-sdk
```

If the SDK is not yet published, you can install it from a Git repository by adding it to your `requirements.txt` or using pip directly:

```bash
pip install git+https://github.com/niravsutariya/python-quick-deployer-sdk.git@main
```

Or include it in your `requirements.txt`:

```
git+https://github.com/niravsutariya/python-quick-deployer-sdk.git@main
```

Then run:

```bash
pip install -r requirements.txt
```

## Usage

### Initializing the Client

Create a `QuickDeployerClient` instance with your API key and base URL:

```python
from quick_deployer_sdk.client import QuickDeployerClient

api_key = "your-api-token"
base_url = "https://staging.quickdeployer.com/api"
client = QuickDeployerClient(base_url, api_key)
```

The base URL defaults to `https://staging.quickdeployer.com/api` if not specified.

### Managing Projects

#### List Projects

Retrieve a list of projects:

```python
projects = client.projects().list()
for project in projects:
    print(f"Project ID: {project['id']}, Name: {project['name']}")
```

#### Get a Project

Fetch details for a specific project:

```python
project = client.projects().get("project-123")
print(f"Project Name: {project['name']}")
```

#### Create a Project

Create a new project:

```python
new_project = client.projects().create({
    "name": "New Project",
    "description": "A test project"
})
print(f"Created Project ID: {new_project['id']}")
```

#### Update a Project

Update an existing project:

```python
updated_project = client.projects().update("project-123", {
    "name": "Updated Project"
})
print(f"Updated Project Name: {updated_project['name']}")
```

#### Delete a Project

Delete a project:

```python
client.projects().delete("project-123")
print("Project deleted successfully")
```

### Managing Servers

#### List Servers

Retrieve servers for a specific project:

```python
servers = client.servers("project-123").list()
for server in servers["servers"]:
    print(f"Server ID: {server['id']}, Name: {server['name']}")
```

#### Get a Server

Fetch details for a specific server:

```python
server = client.servers("project-123").get("server-456")
print(f"Server Name: {server['name']}")
```

#### Create a Server

Create a new server:

```python
new_server = client.servers("project-123").create({
    "name": "New Server",
    "type": "web"
})
print(f"Created Server ID: {new_server['id']}")
```

#### Update a Server

Update an existing server:

```python
updated_server = client.servers("project-123").update("server-456", {
    "name": "Updated Server"
})
print(f"Updated Server Name: {updated_server['name']}")
```

#### Delete a Server

Delete a server:

```python
client.servers("project-123").delete("server-456")
print("Server deleted successfully")
```

#### Check Server Status

Check the status of a server:

```python
status = client.servers("project-123").check_status("server-456")
print(f"Server Status: {status['status']}")
```

### Error Handling

All methods raise a `QuickDeployerError` on API failures. Use try-except blocks to handle errors:

```python
from quick_deployer_sdk.exceptions import QuickDeployerError

try:
    projects = client.projects().list()
except QuickDeployerError as e:
    print(f"Error: {str(e)}")
```

### Health Check

Check the API's health status:

```python
health = client.check_health()
print(f"API Status: {health['status']}")
```

## Configuration

- **API Key**: Obtain your API key from the QuickDeployer dashboard.
- **Base URL**: Override the default `https://staging.quickdeployer.com/api` if using a different environment (e.g., production).

## Testing

The SDK includes unit tests for the `Project` and `Server` resources using pytest.

### Running Tests

1. Install dependencies:

```bash
pip install pytest requests
```

2. Run tests:

```bash
pytest
```

Tests are located in the `tests/` directory (e.g., `test_project.py`, `test_server.py`) and use `unittest.mock` to simulate API responses.

## Flask/Django Integration

To use the SDK in a Flask or Django project:

1. Install the SDK as a pip package (see [Installation](#installation)).
2. Create a service class to wrap SDK usage:

```python
# app/services/deployment_service.py
from quick_deployer_sdk.client import QuickDeployerClient

class DeploymentService:
    def __init__(self):
        self.client = QuickDeployerClient(
            base_url="https://staging.quickdeployer.com/api",
            api_key="your-api-token"
        )

    def get_projects(self):
        return self.client.projects().list()
```

3. For Django, configure the API key in `settings.py` and inject it into the service.
4. For Flask, use app configuration or environment variables to manage the API key.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please include tests for new features and follow PEP 8 coding standards.

## License

This SDK is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For issues or questions, open an issue on the [GitHub repository](https://github.com/niravsutariya/python-quick-deployer-sdk) or contact support@quickdeployer.com.