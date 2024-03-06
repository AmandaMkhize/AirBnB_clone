#!/usr/bin/python3
"""Initialize engine package."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

