from typing import Dict, Any, Optional
from .client import QuickDeployerClient
from .exceptions import QuickDeployerError

class Server:
    """Handler for Server-related API operations."""
    
    def __init__(self, client: QuickDeployerClient, project_id: str):
        """
        Initialize Server handler.
        
        Args:
            client (QuickDeployerClient): API client instance.
            project_id (str): ID of the project.
        """
        self.client = client
        self.project_id = project_id
    
    def list(self, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        List all servers for a project.
        
        Args:
            params (Dict, optional): Query parameters.
        
        Returns:
            Dict containing list of servers.
        """
        return self.client.request('GET', f'projects/{self.project_id}/servers', params=params)
    
    def get(self, server_id: str) -> Dict[str, Any]:
        """
        Get a specific server.
        
        Args:
            server_id (str): ID of the server.
        
        Returns:
            Dict containing server details.
        """
        return self.client.request('GET', f'projects/{self.project_id}/servers/{server_id}')
    
    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new server.
        
        Args:
            data (Dict): Server creation payload.
        
        Returns:
            Dict containing created server details.
        """
        return self.client.request('POST', f'projects/{self.project_id}/servers', data=data)
    
    def update(self, server_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a server.
        
        Args:
            server_id (str): ID of the server.
            data (Dict): Server update payload.
        
        Returns:
            Dict containing updated server details.
        """
        return self.client.request('PUT', f'projects/{self.project_id}/servers/{server_id}', data=data)
    
    def delete(self, server_id: str) -> Dict[str, Any]:
        """
        Delete a server.
        
        Args:
            server_id (str): ID of the server.
        
        Returns:
            Dict containing response data.
        """
        return self.client.request('DELETE', f'projects/{self.project_id}/servers/{server_id}')
    
    def check_status(self, server_id: str) -> Dict[str, Any]:
        """
        Check the status of a server.
        
        Args:
            server_id (str): ID of the server.
        
        Returns:
            Dict containing server status.
        """
        return self.client.request('GET', f'projects/{self.project_id}/servers/{server_id}/status')