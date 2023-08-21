#!/usr/bin/python3

from models.base_model import BaseModel

from models import storage

all_objs = storage.all()

print("-- Reloaded objects --")

for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()

my_model.my_number = 89

my_model.name = "ALX SE SCHOOL"

my_model.save()
print(my_model)
