from pydantic import BaseModel
from sqlalchemy import MetaData

metadata = MetaData()



class CourseDE(BaseModel):
    """This class is used to represent a course."""
    name: str
    description: str
    price: float
