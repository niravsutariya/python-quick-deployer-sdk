from typing import Dict, Any, Optional
from .client import QuickDeployerClient
from .exceptions import QuickDeployerError

class Project:
    """Handler for Project-related API operations."""
    
    def __init__(self, client: QuickDeployerClient):
        """
        Initialize Project handler.
        
        Args:
            client (QuickDeployerClient): API client instance.
        """
        self.client = client
    
    def list(self, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        List all projects.
        
        Args:
            params (Dict, optional): Query parameters.
        
        Returns:
            Dict containing list of projects.
        """
        return self.client.request('GET', 'projects', params=params)
    
    def get(self, project_id: str) -> Dict[str, Any]:
        """
        Get a specific project.
        
        Args:
            project_id (str): ID of the project.
        
        Returns:
            Dict containing project details.
        """
        return self.client.request('GET', f'projects/{project_id}')
    
    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new project.
        
        Args:
            data (Dict): Project creation payload.
        
        Returns:
            Dict containing created project details.
        """
        return self.client.request('POST', 'projects', data=data)
    
    def update(self, project_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a project.
        
        Args:
            project_id (str): ID of the project.
            data (Dict): Project update payload.
        
        Returns:
            Dict containing updated project details.
        """
        return self.client.request('PUT', f'projects/{project_id}', data=data)
    
    def delete(self, project_id: str) -> Dict[str, Any]:
        """
        Delete a project.
        
        Args:
            project_id (str): ID of the project.
        
        Returns:
            Dict containing response data.
        """
        return self.client.request('DELETE', f'projects/{project_id}')