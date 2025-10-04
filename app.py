from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

#A list to store tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_name = request.form.get('task')
    deadline = request.form.get('deadline')

    if task_name and deadline:
        tasks.append({
            'name': task_name,
            'deadline': deadline  # save deadline as string
        })
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
