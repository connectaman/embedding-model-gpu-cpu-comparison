from pydantic import BaseModel
from typing import Optional, List,Tuple

class QueryInput(BaseModel):
    sentence : str