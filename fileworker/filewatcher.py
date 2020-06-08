import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from db import get_session
from db.models import Mediafile
from fileworker.filechecker import check


class FileObserver:
    path = None
    recursive = True
    observer = Observer()

    def __init__(self, path, recursive=True):
        self.path = path if isinstance(path, str) else os.getcwd()
        self.recursive = recursive

    def start_observer(self):
        self.observer.schedule(Handler(), self.path, recursive=self.recursive)
        self.observer.start()

    def stop_observer(self):
        self.observer.stop()


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        dbsess = get_session()
        root = f"{os.path.sep}".join(event.src_path.split(os.path.sep)[:-1])
        file = event.src_path.split(os.path.sep).pop()
        if check(file):
            mf = Mediafile()
            mf.path = root
            mf.filename = file
            mf.file_ext = file.split(".").pop()
            mf.size = os.path.getsize(os.path.join(root, file))
            dbsess.add(mf)
            dbsess.commit()
            dbsess.close()

    def on_deleted(self, event):
        dbsess = get_session()
        root = f"{os.path.sep}".join(event.src_path.split(os.path.sep)[:-1])
        file = event.src_path.split(os.path.sep).pop()

    def on_modified(self, event):
        dbsess = get_session()
        root = f"{os.path.sep}".join(event.src_path.split(os.path.sep)[:-1])
        file = event.src_path.split(os.path.sep).pop()

    def on_moved(self, event):
        dbsess = get_session()
        root = f"{os.path.sep}".join(event.src_path.split(os.path.sep)[:-1])
        file = event.src_path.split(os.path.sep).pop()
