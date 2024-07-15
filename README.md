<h2>Todo App API</h2>

This is a basic API for a Todo app based on microservice architecture. With this API, you can create, read, update, and delete todos as per your convenience. The API provides a pagination feature to retrieve a certain number of todo details at a time.



<h3>Features</h3>

Create Todo: Add new todos.
Read Todos: Retrieve todos with pagination support.
Update Todo: Modify existing todos.
Delete Todo: Remove todos from the list.



<h3>Technologies Used</h3>

FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+.
Uvicorn: A lightning-fast ASGI server for FastAPI.
SQLLite: A relational database management system.
SQLAlchemy: An ORM (Object Relational Mapper) to interact with the database.
Pytest: A framework for unit testing.



<h3>Installation</h3>

To run this API on your local system, ensure that the following are installed:

Python 3.6+
SQLLite


<h3>Step-by-Step Installation</h3>

1.Clone the repository:
git clone [https://github.com/rishi-160323/FastAPI_todo.git]
cd todo-app

2.Install Python packages:
pip install fastapi
pip install sqlalchemy
pip install -U pydantic

3.Install SQLLite Shell:
sudo apt-get install sqlite3



<h3>Running the Application</h3>

1.Start the SQLLite service:
Ensure SQLLite server is running and accessible.

2.Run the FastAPI application with Docker container:
docker-compose up --build
uvicorn main:app --reload
This command starts the FastAPI server with auto-reload enabled.



<h3>Running Tests</h3>
Unit tests are written using Pytest. Before running the tests, make sure to drop the old database if it exists, as the tests create and drop a temporary database.

pytest
This command runs all the test cases.



<h3>Contributing</h3>
Contributions are welcome! Please feel free to submit a Pull Request.


<h3>License</h3>
This project is licensed under the MIT License.


By following this guide, you should be able to set up and run the Todo app API on your local machine. Enjoy coding!

Feel free to adjust the URLs, repository links, or any specific details according to your actual project settings.
