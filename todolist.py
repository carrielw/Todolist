from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)


# In-memory storage for tasks (resets when server restarts)
tasks = []
task = []

# HTML template (simplified - real projects should use separate template files)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto; /* This centers the content */
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        input[type="text"] {
            flex-grow: 1;
            padding: 8px;
        }
        button {
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: #f9f9f9;
            margin: 5px 0;
            padding: 10px;
            border-radius: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        a {
            color: #ff4444;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <h1>My To-Do List</h1>
    <form action="/add" method="post">
        <input type="text" name="task" placeholder="Enter a task" required>
        <button type="submit">Add</button>
    </form>
    <ul>
        {% for task in tasks %}
        <li>
            <span>{{ task }}</span>
            <a href="/delete/{{ loop.index0 }}">Delete</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# Homepage: Show all tasks
@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

# Add a new task
@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:  # Only add if task is not empty
        tasks.append(task)
    return redirect("/")  # Redirect back to homepage

# Delete a task by its index
@app.route("/delete/<int:task_id>")
def delete(task_id):
    if task_id < len(tasks):  # Check if index is valid
        tasks.pop(task_id)  # Remove the task
    return redirect("/")  # Redirect back to homepage

# if __name__ == "__main__": # only the localhost can see it 
#     # Run the app in debug mode (auto-reloads when code changes)
#     app.run(debug=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # All same wifi user can see it 