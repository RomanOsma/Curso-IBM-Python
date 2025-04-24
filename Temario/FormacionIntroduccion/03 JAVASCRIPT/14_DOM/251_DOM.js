document.addEventListener('DOMContentLoaded', () => {
    const addButton = document.getElementById('add-task');
    const newTaskInput = document.getElementById('new-task');
    const taskList = document.getElementById('task-list');

    addButton.addEventListener('click', () => {
        const taskText = newTaskInput.value.trim();
        if (taskText !== '') {
            addTask(taskText);
            newTaskInput.value = '';
        }
    });

    newTaskInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            addButton.click();
        }
    });

    taskList.addEventListener('click', (e) => {
        if (e.target.classList.contains('task-item')) {
            toggleTaskCompletion(e.target);
        } else if (e.target.classList.contains('delete-button')) {
            deleteTask(e.target.parentElement);
        }
    });

    function addTask(text) {
        const li = document.createElement('li');
        li.textContent = text;
        li.className = 'task-item';
        li.innerHTML += '<span class="delete-button"> X</span>';
        taskList.appendChild(li);
    }

    function toggleTaskCompletion(taskItem) {
        taskItem.classList.toggle('completed');
    }

    function deleteTask(taskItem) {
        taskList.removeChild(taskItem);
    }
});
