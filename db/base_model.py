import datetime
from nanoid import generate
from sqlalchemy import Column,String,DateTime
from db.base_class import Base

class BaseModel(Base):
    __abstract__ = True

    id = Column(String(length=12), primary_key=True, default=lambda: generate(size=12)) # type: ignore
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.datetime.now(datetime.timezone.utc),
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    def as_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys(): # type: ignore
            dict_[key] = getattr(self, key)
        return dict_