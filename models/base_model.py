import uuid
from datetime import datetime

"""class base model that defines
all common attributes and classes"""

tf = "%Y-%m-%dT%H:%M:%S.%f" # time format...

class BaseModel:
    """I am the base"""
    def __init__(self, *args, **kwargs):
        """Initialize"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    self.k = v
            if type(kwargs['created_at']) and\
                        type(kwargs['updated_at']) == str:
                self.created_at = datetime.strptime(kwargs['created_at'], tf)
                self.updated_at = datetime.strptime(kwargs['updated_at'], tf)
            else:
                self.created_at = datetime.utcnow()
                self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow().strftime(tf)
            self.updated_at = self.created_at
    def __str__(self):
        """Informal str rep"""
        return ("[BaseModel] ({:s}) {}"\
                .format(self.id, self.__dict__))

    def save(self):
        """updates the public instance
        attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now().strftime(tf)


    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__
        of the instance"""
        nw_dict = self.__dict__.copy()
        nw_dict["__class__"] = self.__class__.__name__
        return nw_dict
