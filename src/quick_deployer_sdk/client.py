import requests
from typing import Dict, Any, Optional
from .exceptions import QuickDeployerError

class QuickDeployerClient:
    """Client for interacting with the Quick Deployer API."""
    
    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the client with base URL and API key.
        
        Args:
            base_url (str): Base URL of the API (e.g., 'https://api.example.com/api')
            api_key (str): API key for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        })
    
    def check_health(self) -> Dict[str, Any]:
        """
        Check API health via GET /up.
        
        Returns:
            Dict containing health status.
        
        Raises:
            QuickDeployerError: If the request fails.
        """
        try:
            response = self.session.get(f'{self.base_url}/up')
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise QuickDeployerError(f"Health check failed: {str(e)}")
    
    def projects(self) -> 'Project':
        """
        Get Project resource handler.
        
        Returns:
            Project instance.
        """
        from .project import Project  # Lazy import to avoid circular dependency
        return Project(self)
    
    def servers(self, project_id: str) -> 'Server':
        """
        Get Server resource handler for a specific project.
        
        Args:
            project_id (str): ID of the project.
        
        Returns:
            Server instance.
        """
        from .server import Server  # Lazy import to avoid circular dependency
        return Server(self, project_id)
    
    def request(self, method: str, endpoint: str, data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Generic method to make API requests.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE).
            endpoint (str): API endpoint (relative to base_url).
            data (Dict, optional): JSON payload for POST/PUT.
            params (Dict, optional): Query parameters.
        
        Returns:
            Dict Containing response data.
        
        Raises:
            QuickDeployerError: If the request fails.
        """
        try:
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            response = self.session.request(method, url, json=data, params=params)
            response.raise_for_status()
            return response.json() if response.content else {}
        except requests.RequestException as e:
            raise QuickDeployerError(f"API request failed: {str(e)}")