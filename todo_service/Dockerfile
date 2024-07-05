FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY ../requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire todo_service directory into the container
COPY . .

# Expose port 8000 for the FastAPI app to run on
EXPOSE 8000

# Command to run the FastAPI app using uvicorn
CMD ["uvicorn", "todo_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
