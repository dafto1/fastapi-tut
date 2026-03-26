from pydantic import BaseModel 

class PoseCreate(BaseModel)  :
    title : str 
    content : str 
    
class PostResponse(BaseModel) : 
    title : str 
    content : str 