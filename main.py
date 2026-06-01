from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class MenuItem(BaseModel):
        id: int
        name: str
        price : int

Menu: List[MenuItem] = []


@app.get("/")
def read_root():
     return {"Message": "Welcome to our Restaurant"}

@app.get("/Menu")
def get_Menu():
    return Menu


@app.post("/Menu")
def add_Menu_item(item: MenuItem):
    Menu.append(item)
    return {
         "message" : "Item added",
         "item" : item
    }

@app.get("/Items/{item_id}")
def get_Menu_item(item_id: int):
    for item in Menu:
        if item.id == item_id:
            return item
    return {"error": "item not found"}



@app.delete("/Menu/{item_id}")
def delete_Menu_item(item_id: int):
    for index, item in enumerate(Menu):
        if item.id == item_id:
            deleted_item = Menu.pop(index)
            return {
                 "message" : "item deleted",
                 "deleted_item": deleted_item
            }
    
@app.get("/Menu/Search")
def Search_Menu(name : str):
     result = []

     for item in Menu:
          if name.lower() in item.name.lower():
               result.append(item)

          return result
