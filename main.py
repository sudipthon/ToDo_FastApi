from fastapi import FastAPI
from models import Todo
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

todos=[]
# get all to dos
@app.get("/todos")
async def get_todos():
    return {"todos":todos}



# create todo
@app.post("/todos")
async def create_todo(todo_obj:Todo):
      #todo variable is gonna be of type Todo which has been defined in models.py
    todos.append(todo_obj)
    return {"message":"Todo Created Successfully"}

#get single todo
@app.get("/todos/{todo_id}")
async def get_single_todo(todo_id:int):
    if len(todos)>todo_id:
        return todos[todo_id]
    return {"message":"Todo Not Found"}



# update todo
@app.put("/todos/{todo_id}")
async def update_todo_by_id(todo_id:int,todo_obj:Todo):
    if len(todos)>todo_id:
        todos[todo_id-1]=todo_obj
        return {"message":"Todo Updated Successfully"}
    return {"message":"Todo Not Found"}

# delete todo
@app.delete("/todos/{todo_id}") 
async def delete_todo_by_id(todo_id:int):
    todos.pop(todo_id-1)
    return {"message":"Todo Deleted Successfully"}
