from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base


class Mediafile(Base):
    __tablename__ = "mediafiles"

    id = Column(Integer, primary_key=True)
    path = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    filename = Column(String, nullable=False)
    file_ext = Column(String, nullable=False)
    file_metadata = relationship("MediaMetadata", uselist=False, back_populates="mediafiles")

    def __repr__(self):
        return f"<{self.id}, {self.abs_path}, {self.size}, {self.file_ext}>"


class MediaMetadata(Base):
    __tablename__ = "mediametadata"

    id = Column(Integer, primary_key=True)
    codec = Column(String, nullable=True)
    resolution_w = Column(Integer, nullable=True)
    resolution_h = Column(Integer, nullable=True)
    mediafile = relationship("Mediafile", back_populates="mediametadata")
