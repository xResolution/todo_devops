import pytest

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_task(client):
    """Test adding a new task"""
    response = client.post('/tasks', json={'description': 'Test task'})
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['description'] == 'Test task'
    assert not data['completed']

def test_get_tasks(client):
    """Test getting all tasks"""
    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_complete_task(client):
    """Test marking a task as completed"""
    # Add a task
    response = client.post('/tasks', json={'description': 'Test task'})
    task_id = response.get_json()['id']
    
    # Mark as completed
    response = client.put(f'/tasks/{task_id}', json={'completed': True})
    assert response.status_code == 200
    data = response.get_json()
    assert data['completed']

def test_delete_task(client):
    """Test deleting a task"""
    # Add a task
    response = client.post('/tasks', json={'description': 'Test task'})
    task_id = response.get_json()['id']
    
    # Delete the task
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 204

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
