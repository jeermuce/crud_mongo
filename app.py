import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Optional, Dict, Any


MONGO_URI:str= 'mongodb://localhost';


def instert_base_data() -> list[dict[str, object]]:
     empleados = [
        {
            "empno": 7369,
            "ename": "SMITH",
            "job": "CLERK",
            "sal": 800,
            "departamento": {
                "deptno": 20,
                "dname": "RESEARCH",
                "loc": "DALLAS"
            }
        },
        {
            "empno": 7499,
            "ename": "ALLEN",
            "job": "SALESMAN",
            "sal": 1600,
            "departamento": {
                "deptno": 30,
                "dname": "SALES",
                "loc": "CHICAGO"
            }
        },
        {
            "empno": 7521,
            "ename": "WARD",
            "job": "SALESMAN",
            "sal": 1250,
            "departamento": {
                "deptno": 30,
                "dname": "SALES",
                "loc": "CHICAGO"
            }
        },
        {
            "empno": 7566,
            "ename": "JONES",
            "job": "MANAGER",
            "sal": 2975,
            "departamento": {
                "deptno": 20,
                "dname": "RESEARCH",
                "loc": "DALLAS"
            }
        },
        {
            "empno": 7654,
            "ename": "MARTIN",
            "job": "SALESMAN",
            "sal": 1250,
            "departamento": {
                "deptno": 30,
                "dname": "SALES",
                "loc": "CHICAGO"
            }
        },
        {
            "empno": 7698,
            "ename": "BLAKE",
            "job": "MANAGER",
            "sal": 2850,
            "departamento": {
                "deptno": 30,
                "dname": "SALES",
                "loc": "CHICAGO"
            }
        },
        {
            "empno": 7782,
            "ename": "CLARK",
            "job": "MANAGER",
            "sal": 2450,
            "departamento": {
                "deptno": 10,
                "dname": "ACCOUNTING",
                "loc": "NEW YORK"
            }
        },
        {
            "empno": 7788,
            "ename": "SCOTT",
            "job": "ANALYST",
            "sal": 3000,
            "departamento": {
                "deptno": 20,
                "dname": "RESEARCH",
                "loc": "DALLAS"
            }
        },
        {
            "empno": 7839,
            "ename": "KING",
            "job": "PRESIDENT",
            "sal": 5000,
            "departamento": {
                "deptno": 10,
                "dname": "ACCOUNTING",
                "loc": "NEW YORK"
            }
        },
        {
            "empno": 7844,
            "ename": "TURNER",
            "job": "SALESMAN",
            "sal": 1500,
            "departamento": {
                "deptno": 30,
                "dname": "SALES",
                "loc": "CHICAGO"
            }
        },
        {
            "empno": 7876,
            "ename": "ADAMS",
            "job": "CLERK",
            "sal": 1100,
            "departamento": {
                "deptno": 20,
                "dname": "RESEARCH",
                "loc": "DALLAS"
            }
        },
        {
            "empno": 7900,
            "ename": "JAMES",
            "job": "CLERK",
            "sal": 950,
            "departamento": {
                "deptno": 30,
                "dname": "SALES",
                "loc": "CHICAGO"
            }
        },
        {
            "empno": 7902,
            "ename": "FORD",
            "job": "ANALYST",
            "sal": 3000,
            "departamento": {
                "deptno": 20,
                "dname": "RESEARCH",
                "loc": "DALLAS"
            }
        },
        {
            "empno": 7934,
            "ename": "MILLER",
            "job": "CLERK",
            "sal": 1300,
            "departamento": {
                "deptno": 10,
                "dname": "ACCOUNTING",
                "loc": "NEW YORK"
            }
        }
    ]
     return empleados;

def connect_to_mongo() -> Collection[dict[str, object]]:
    try:
        client: MongoClient = MongoClient(MONGO_URI)
        db = client['empleados']
        collection = db['rh']

        if collection.count_documents({}) == 0:
            empleados = instert_base_data()
            print("Base de datos vacía, insertando datos...")
            collection.insert_many(empleados)
            print("Datos insertados correctamente")
            del empleados
        else:
            print("La colección ya tiene datos")
            empleados = list(collection.find())
    except Exception:
        print("Error al conectarse a la base de datos: {}".format(Exception))
    finally:
        print("Conexión exitosa")
        return collection;





def list_empno_ename_loc(collection: Collection[dict[str, object]]) -> list[dict[str, object]]:
    empleados = list(collection.find({}, {"empno": 1, "ename": 1, "_id": 0}))
    for empleado in empleados:
        print(empleado)
    return empleados

#crud
#create
def create_employee(collection: Collection[dict[str, object]], empno: int, ename: str, job: str, sal: float, deptno: int, dname: str, loc: str) -> dict[str, object] | None:
    try:
        collection.insert_one({
            "empno": empno,
            "ename": ename,
            "job": job,
            "sal": sal,
            "departamento": {
                "deptno": deptno,
                "dname": dname,
                "loc": loc
            }
        })
        print("Empleado insertado correctamente")
    except Exception:
        print("Error al insertar empleado: {}".format(Exception))
    finally:
        return collection.find_one({"empno": empno})

#read
def read_employee(collection: Collection[dict[str, object]], ename: str) -> dict[str, object] | None:
    try:
        empleado = collection.find_one({"ename": ename}, {"_id": 0})
        if empleado:
            print("Empleado encontrado");
        else:
            print("Empleado no encontrado")
    except Exception:
        print("Error al leer empleado: {}".format(Exception))
    finally:
        return empleado

from typing import Optional, Dict, Any
from pymongo.collection import Collection

def update_employee(collection: Collection[dict[str, Any]], empno: int, ename: Optional[str] = None, 
                    job: Optional[str] = None, sal: Optional[float] = None, deptno: Optional[int] = None, 
                    dname: Optional[str] = None, loc: Optional[str] = None) -> Dict[str, Any] | None:
    update_fields: Dict[str, Any] = {}

    if ename is not None:
        update_fields["ename"] = ename
    if job is not None:
        update_fields["job"] = job
    if sal is not None:
        update_fields["sal"] = sal
    if any([deptno, dname, loc]):
        update_fields["departamento"] = {}
        if deptno is not None:
            update_fields["departamento"]["deptno"] = deptno
        if dname is not None:
            update_fields["departamento"]["dname"] = dname
        if loc is not None:
            update_fields["departamento"]["loc"] = loc

    try:
        if update_fields:
            collection.update_one({"empno": empno}, {"$set": update_fields})
            print("Empleado actualizado correctamente")
        else:
            print("No fields to update")
    except Exception as e:
        print("Error al actualizar empleado: {}".format(e))
    finally:
        return collection.find_one({"empno": empno}, {"empno": 1, "ename": 1, "job": 1, "sal": 1, "departamento": 1, "_id": 0})


#delete
def delete_employee(collection: Collection[dict[str, Any]], empno: int) -> bool:
    try:
        collection.delete_many({"empno": empno})
        print("Empleado eliminado correctamente")
    except Exception as e:
        print("Error al eliminar empleado: {}".format(e))
    finally:
        return not bool(collection.find_one({"empno": empno}))

##############################
#veindo si funciona

collectt =connect_to_mongo()
list_empno_ename_loc(collectt);

new_employee = create_employee(collectt, empno=8000, ename="JUAN", job="DEVOPS", sal=4000.30, deptno=10, dname="DESARROLLO", loc="CHIHUAHUA")
print("Nuevo empleado: ", new_employee)
newest_employee = read_employee(collectt, ename="JUAN")
print("Empleado leído: ", newest_employee)
updated_employee = update_employee(collectt, empno=8000, ename="ARTURO", loc="PARRAl")
print(updated_employee)

list_empno_ename_loc(collectt);

deleted = delete_employee(collectt, empno=8000)
print("Empleado eliminado: ", deleted)

list_empno_ename_loc(collectt);

##############################
# GUI
##############################
def create_employee_gui():
    empno = int(entry_empno.get())
    ename = entry_ename.get()
    job = entry_job.get()
    sal = float(entry_sal.get())
    deptno = int(entry_deptno.get())
    dname = entry_dname.get()
    loc = entry_loc.get()
    new_emp = create_employee(collectt, empno, ename, job, sal, deptno, dname, loc)
    if new_emp:
        messagebox.showinfo("Éxito:", "Empleado creado correctamente")
    else:
        messagebox.showerror("Error:", "Falló la creación del empleado")

def read_employee_gui():
    ename = entry_ename.get()
    emp = read_employee(collectt, ename)
    if emp:
        messagebox.showinfo("Detalles del Empleado", f"{emp}")
    else:
        messagebox.showerror("Error:", "No se encontró el empleado")

def update_employee_gui():
    empno = int(entry_empno.get())
    ename = entry_ename.get() if entry_ename.get() else None
    job = entry_job.get() if entry_job.get() else None
    sal = float(entry_sal.get()) if entry_sal.get() else None
    deptno = int(entry_deptno.get()) if entry_deptno.get() else None
    dname = entry_dname.get() if entry_dname.get() else None
    loc = entry_loc.get() if entry_loc.get() else None
    exists = bool(collectt.find_one({"empno": empno}))
    if not exists:
        messagebox.showerror("Error:", "No se encontró el empleado")
    elif exists:
        updated_emp = update_employee(collectt, empno, ename, job, sal, deptno, dname, loc)
    if updated_emp:
        messagebox.showinfo("Éxito:", "Empleado actualizado correctamente")
    else:
        messagebox.showerror("Error:", "Falló la actualización del empleado")

def delete_employee_gui():
    empno = int(entry_empno.get())
    exists: bool = bool(collectt.find_one({"empno": empno}))
    deleted = delete_employee(collectt, empno)
    if deleted and exists:
        messagebox.showinfo("Éxito:", "Empleado eliminado correctamente")
    elif not exists:
        messagebox.showerror("Error:", "No se encontró el empleado")
    else:
        messagebox.showerror("Error:", "Falló la eliminación del empleado")
        




def check_fields(*args): 
    if entry_empno.get() and entry_ename.get() and entry_job.get() and entry_sal.get() and entry_deptno.get() and entry_dname.get() and entry_loc.get(): 
        create_button.config(state=tk.NORMAL) 
    else: 
        create_button.config(state=tk.DISABLED) 

root = tk.Tk()
root.title("Recursos Humanos")

tk.Label(root, text="Emp No:").grid(row=0, column=0)
entry_empno = tk.Entry(root)
entry_empno.grid(row=0, column=1)
entry_empno.bind("<KeyRelease>", check_fields) 

tk.Label(root, text="Name:").grid(row=1, column=0)
entry_ename = tk.Entry(root)
entry_ename.grid(row=1, column=1)
entry_ename.bind("<KeyRelease>", check_fields) 

tk.Label(root, text="Job:").grid(row=2, column=0)
entry_job = tk.Entry(root)
entry_job.grid(row=2, column=1)
entry_job.bind("<KeyRelease>", check_fields) 

tk.Label(root, text="Salary:").grid(row=3, column=0)
entry_sal = tk.Entry(root)
entry_sal.grid(row=3, column=1)
entry_sal.bind("<KeyRelease>", check_fields) 

tk.Label(root, text="Dept No:").grid(row=4, column=0)
entry_deptno = tk.Entry(root)
entry_deptno.grid(row=4, column=1)
entry_deptno.bind("<KeyRelease>", check_fields) 

tk.Label(root, text="Dept Name:").grid(row=5, column=0)
entry_dname = tk.Entry(root)
entry_dname.grid(row=5, column=1)
entry_dname.bind("<KeyRelease>", check_fields) 

tk.Label(root, text="Location:").grid(row=6, column=0)
entry_loc = tk.Entry(root)
entry_loc.grid(row=6, column=1)
entry_loc.bind("<KeyRelease>", check_fields) 

create_button = tk.Button(root, text="Create Employee", command=create_employee_gui, state=tk.DISABLED) 
create_button.grid(row=7, column=0)

tk.Button(root, text="Read Employee", command=read_employee_gui).grid(row=7, column=1)
tk.Button(root, text="Update Employee", command=update_employee_gui).grid(row=8, column=0)
tk.Button(root, text="Delete Employee", command=delete_employee_gui).grid(row=8, column=1)

collectt = connect_to_mongo()
root.mainloop()
