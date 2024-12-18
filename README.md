# TodoList-App

# Todo List Application

This is a simple Todo List application built with Django. It allows users to create, view, complete, and delete tasks.

## Features

- Add new tasks
- Mark tasks as completed
- Delete tasks
- Simple and clean user interface

## Technologies Used

- Django 5.1
- Python 3.x
- SQLite (default database)
- HTML/CSS/JS for frontend

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/todo_app.git
   cd todo_app
   ```
   
2. **Create a virtual environment:** 

    ```bash
    python -m venv venv
    source venv/bin/activate                    
    
    #Windows use 
    venv\Scripts\activate
    ```

3. **Install the required packages:**
```
pip install -r requirements.txt
```

4. **Run migrations:**
```
    python manage.py run migrations
```

5.**Run the development server:**
```
python manage.py runserver
```

6. **Open your browser and go to: **
```
http://127.0.0.1:8000/
```


## Usage
- To add a new task, enter the task title in the input field and click "Add".
- To mark a task as completed, click the checkbox next to the task.
- To delete a task, click the "×" button next to the task.
- Change from light mode to dark mode and vice versa.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Django documentation for guidance on building web applications.
- Inspiration from various Todo applications.
 
```

### Notes:
- Replace `https://github.com/yourusername/todo_app.git` with the actual URL of your repository.
- You may want to create a `requirements.txt` file that lists the dependencies for your project. You can generate it using `pip freeze > requirements.txt` after installing the necessary packages.
- Adjust any sections as needed to better fit your project specifics.
```
