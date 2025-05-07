import unittest
import requests_mock
from quick_deployer_sdk import QuickDeployerClient

class TestQuickDeployerClient(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://quickdeployer.com/api'
        self.api_key = 'test-key'
        self.client = QuickDeployerClient(self.base_url, self.api_key)
    
    @requests_mock.Mocker()
    def test_check_health(self, m):
        m.get(f'{self.base_url}/up', json={'status': 'ok'})
        result = self.client.check_health()
        self.assertEqual(result, {'status': 'ok'})
    
    @requests_mock.Mocker()
    def test_list_projects(self, m):
        m.get(f'{self.base_url}/projects', json=[{'id': '1', 'name': 'Test Project'}])
        result = self.client.projects().list()
        self.assertEqual(result, [{'id': '1', 'name': 'Test Project'}])
    
    @requests_mock.Mocker()
    def test_create_project(self, m):
        m.post(f'{self.base_url}/projects', json={'id': '2', 'name': 'New Project'})
        result = self.client.projects().create({'name': 'New Project'})
        self.assertEqual(result, {'id': '2', 'name': 'New Project'})
    
    @requests_mock.Mocker()
    def test_list_servers(self, m):
        project_id = '1'
        m.get(f'{self.base_url}/projects/{project_id}/servers', json=[{'id': 's1', 'name': 'Server1'}])
        result = self.client.servers(project_id).list()
        self.assertEqual(result, [{'id': 's1', 'name': 'Server1'}])
    
    @requests_mock.Mocker()
    def test_check_server_status(self, m):
        project_id = '1'
        server_id = 's1'
        m.get(f'{self.base_url}/projects/{project_id}/servers/{server_id}/status', json={'status': 'running'})
        result = self.client.servers(project_id).check_status(server_id)
        self.assertEqual(result, {'status': 'running'})

if __name__ == '__main__':
    unittest.main()