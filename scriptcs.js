document.addEventListener("DOMContentLoaded", () => {
    const taskForm = document.getElementById("task-form");
    const tasksContainer = document.getElementById("tasks");

    const fetchTasks = async () => {
        const response = await fetch("/tasks");
        const tasks = await response.json();
        tasksContainer.innerHTML = tasks.map(task => `
            <div class="task">
                <h3>${task.title}</h3>
                <p>${task.description || "No description"}</p>
                <p>Status: ${task.status}</p>
                <button onclick="deleteTask(${task.id})">Delete</button>
            </div>
        `).join("");
    };

    const addTask = async (event) => {
        event.preventDefault();
        const title = document.getElementById("title").value;
        const description = document.getElementById("description").value;
        await fetch("/tasks", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, description }),
        });
        taskForm.reset();
        fetchTasks();
    };

    window.deleteTask = async (id) => {
        await fetch(`/tasks/${id}`, { method: "DELETE" });
        fetchTasks();
    };

    taskForm.addEventListener("submit", addTask);
    fetchTasks();
});
