import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from db import get_session
from db.models.mediafile import Mediafile


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
        with dbsess:
            mf = Mediafile()
            mf.path = root
            mf.filename = file
            mf.file_ext = file.split(".").pop()
            mf.size = os.path.getsize(os.path.join(root, file))
            dbsess.add(mf)
            dbsess.commit()

    def on_deleted(self, event):
        print(event.is_directory)
        print(event.src_path)

    def on_modified(self, event):
        print(event.is_directory)
        print(event.src_path)

    def on_moved(self, event):
        print(event.is_directory)
        print(event.src_path)