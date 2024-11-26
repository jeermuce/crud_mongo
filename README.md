# Employee Management App

This application allows you to perform CRUD (Create, Read, Update, and Delete) operations on an employee database using MongoDB.

## Prerequisites

- Python 3.10+
- MongoDB


## In Windows

If an error `_tkinter.TclError: Can't find a usable init.tcl in the following directories:`
occurs, add these at the top of app.py and replace `<username>` with your Windows username and `<python_version>` with the correct directory in your system

```python
import os
os.environ['TCL_LIBRARY'] = 'C:\\Users\\<username>\\AppData\\Local\\Programs\\Python\\<python_version>\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Users\\<username>\\AppData\\Local\\Programs\\Python\\<python_version>\\tcl\\tk8.6'
```


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