from sqlalchemy import Column, Integer, String

from db import Base

class Mediafile(Base):
    __tablename__ = "mediafiles"

    id = Column(Integer, primary_key=True)
    path = Column(String, nullable=False)
    abs_path = Column(String, nullable=False)
    size = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<{self.id}, {self.abs_path}, {self.size}>"
