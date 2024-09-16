# CRUD Operation API with FastAPI

This project is a simple REST API for performing CRUD (Create, Read, Update, Delete) operations on student data using **FastAPI**. The API allows clients to manage student records by performing the following actions:
- Add new students
- View all students
- View a specific student's information
- Update an existing student's information
- Delete a student from the database

## Project Structure

- `app.py`: The main file that contains the FastAPI application and routes for handling CRUD operations.
- `data_model.py`: A file that defines the Pydantic models (`NewStudent` and `UpdateStudents`) used for input validation.

## How to Run the Project

### Prerequisites

- **Python 3.7+** installed on your machine.
- **FastAPI** and **Uvicorn** packages installed.

You can install the required packages by running:
```bash
pip install fastapi uvicorn pydantic
```

### Running the FastAPI Application

Use the following command to start the FastAPI server:
```bash
uvicorn app:app --reload
```
- The API will run on `http://127.0.0.1:8000`.
- The `--reload` option is used for development purposes to automatically reload the server upon code changes.

### API Endpoints

#### 1. **Welcome Endpoint**
   - **URL**: `/`
   - **Method**: `GET`
   - **Description**: Displays a welcome message.
   - **Response**: `"Welcome to the API: CRUD Operations"`

#### 2. **Get All Students**
   - **URL**: `/students`
   - **Method**: `GET`
   - **Description**: Retrieves all student records.
   - **Response**: Returns a dictionary of students.

#### 3. **Get a Single Student**
   - **URL**: `/students/{stu_id}`
   - **Method**: `GET`
   - **Description**: Fetches the information for a specific student by `stu_id`.
   - **Response**: Returns the details of the student if found; otherwise, an error message.

#### 4. **Add a New Student**
   - **URL**: `/add_students`
   - **Method**: `POST`
   - **Description**: Adds a new student record.
   - **Request Body**: Requires `NewStudent` model, which consists of:
     - `name` (string)
     - `age` (integer)
   - **Response**: Returns the newly added student record.

#### 5. **Update a Student**
   - **URL**: `/update-student/{stu_id}`
   - **Method**: `PUT`
   - **Description**: Updates an existing student's name or age based on the provided data.
   - **Request Body**: Accepts the `UpdateStudents` model, which allows for partial updates (name and/or age).
   - **Response**: Returns the updated student record or an error message if the student does not exist.

#### 6. **Delete a Student**
   - **URL**: `/delete-student/{stu_id}`
   - **Method**: `DELETE`
   - **Description**: Deletes a student record from the database by `stu_id`.
   - **Response**: Confirmation message or an error message if the student does not exist.

## Data Model

The data models are defined using **Pydantic**, which ensures input validation.

- `NewStudent`: Used when adding a new student. It has the following fields:
  - `name`: `str` (required)
  - `age`: `int` (required)

- `UpdateStudents`: Used when updating an existing student. It has the following optional fields:
  - `name`: `str` (optional)
  - `age`: `int` (optional)

These models are found in the `data_model.py` file and imported into the main application file.

---