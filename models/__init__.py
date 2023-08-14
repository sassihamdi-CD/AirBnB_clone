#!/usr/bin/python3
<<<<<<< HEAD
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
=======
'''
initializing the entire package
'''

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
>>>>>>> 87e3dca232c6629341b82e462ebfba8b212b6cdd
storage.reload()
