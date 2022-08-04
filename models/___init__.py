#!/usr/bin/python3
"""Package maker"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
