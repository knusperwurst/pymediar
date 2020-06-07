import os
from fileworker import filechecker
from db import get_session
from db.models.mediafile import Mediafile


class Scanner:
    filepaths = []
    dbsession = None

    def __init__(self, filepaths):
        self.filepaths = filepaths
        self.dbsession = get_session()

    def scan(self):
        for path in self.filepaths:
            for root, _, files in os.walk(path):
                for file in files:
                    if filechecker.check(file):
                        mf = Mediafile()
                        mf.path = root
                        mf.filename = file
                        mf.file_ext = file.split(".").pop()
                        mf.size = os.path.getsize(os.path.join(root, file))
                        self.dbsession.add(mf)
        self.dbsession.commit()
