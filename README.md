# Employee Management App

This application allows you to perform CRUD (Create, Read, Update, and Delete) operations on an employee database using MongoDB.

## Prerequisites

- Python 3.8+
- MongoDB

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jeermuce/crud_mongo.git
   cd crud_mongo
2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```
3. **Run the application:**

```bash
python app.py
```

4. **Pyinstall the application** !!NOT RECOMMENDED!!
```bash
pyinstaller --onefile app.py
```
    the executable will be in the dist folder
## Usage
Fill in the employee details in the form and click "Create Employee" to add a new employee.

Enter an employee name and click "Read Employee" to view details.

Update the employee details and click "Update Employee" to modify existing data, the key is the EmpNo, other fields are optional.

Enter an employee number and click "Delete Employee" to remove an employee.



## Notes
Ensure MongoDB is running and accessible at mongodb://localhost.

Adjust MongoDB connection settings in app.py if necessary.