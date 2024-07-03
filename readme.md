Todo App API

This is a basic API for a Todo app based on microservice architecture. With this API, you can create, read, update, and delete todos as per your convenience. The API provides a pagination feature to retrieve a certain number of todo details at a time.



Features

Create Todo: Add new todos.
Read Todos: Retrieve todos with pagination support.
Update Todo: Modify existing todos.
Delete Todo: Remove todos from the list.



Technologies Used

FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+.
Uvicorn: A lightning-fast ASGI server for FastAPI.
MySQL: A relational database management system.
SQLAlchemy: An ORM (Object Relational Mapper) to interact with the database.
Pytest: A framework for unit testing.



Installation

To run this API on your local system, ensure that the following are installed:

Python 3.6+
MySQL


Step-by-Step Installation

1.Clone the repository:
git clone https://github.com/yourusername/todo-app.git
cd todo-app

2.Install Python packages:
pip install fastapi
pip install sqlalchemy
pip install -U pydantic
pip install mysql-connector-python

3.Install MySQL Shell:
sudo apt-get install mysql-shell



Running the Application

1.Start the MySQL service:
Ensure MySQL server is running and accessible.

2.Run the FastAPI application:
uvicorn main:app --reload
This command starts the FastAPI server with auto-reload enabled.



Running Tests
Unit tests are written using Pytest. Before running the tests, make sure to drop the old database if it exists, as the tests create and drop a temporary database.

pytest
This command runs all the test cases.



Contributing
Contributions are welcome! Please feel free to submit a Pull Request.


License
This project is licensed under the MIT License.


By following this guide, you should be able to set up and run the Todo app API on your local machine. Enjoy coding!

Feel free to adjust the URLs, repository links, or any specific details according to your actual project settings.
