// Function to display the task list
async function displayTasks() {
    try {
        const response = await fetch('/tasks');
        const tasks = await response.json();
        
        const tasksList = document.getElementById('tasksList');
        tasksList.innerHTML = '';
        
        tasks.forEach(task => {
            const taskElement = document.createElement('div');
            taskElement.className = 'task-item';
            
            const taskText = document.createElement('div');
            taskText.className = 'task-text';
            taskText.textContent = task.description;
            if (task.completed) {
                taskText.className += ' task-completed';
            }
            
            const taskActions = document.createElement('div');
            taskActions.className = 'task-actions';
            
            const completeBtn = document.createElement('button');
            completeBtn.textContent = task.completed ? 'Undo' : 'Complete';
            completeBtn.className = 'complete-btn';
            completeBtn.onclick = () => completeTask(task.id);
            
            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Delete';
            deleteBtn.className = 'delete-btn';
            deleteBtn.onclick = () => deleteTask(task.id);
            
            taskActions.appendChild(completeBtn);
            taskActions.appendChild(deleteBtn);
            
            taskElement.appendChild(taskText);
            taskElement.appendChild(taskActions);
            
            tasksList.appendChild(taskElement);
        });
    } catch (error) {
        console.error('Error loading tasks:', error);
    }
}

// Function to add a new task
async function addTask() {
    const taskInput = document.getElementById('taskInput');
    const description = taskInput.value.trim();
    
    if (description) {
        try {
            const response = await fetch('/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ description }),
            });
            
            if (response.ok) {
                taskInput.value = '';
                displayTasks();
            }
        } catch (error) {
            console.error('Error adding task:', error);
        }
    }
}

// Function to mark a task as completed
async function completeTask(taskId) {
    try {
        const response = await fetch(`/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ completed: true }),
        });
        
        if (response.ok) {
            displayTasks();
        }
    } catch (error) {
        console.error('Error updating task:', error);
    }
}

// Function to delete a task
async function deleteTask(taskId) {
    if (confirm('Are you sure you want to delete this task?')) {
        try {
            const response = await fetch(`/tasks/${taskId}`, {
                method: 'DELETE',
            });
            
            if (response.ok) {
                displayTasks();
            }
        } catch (error) {
            console.error('Error deleting task:', error);
        }
    }
}

// Initialization
window.onload = displayTasks;
