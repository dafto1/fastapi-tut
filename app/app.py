from fastapi import FastAPI , HTTPException, File ,UploadFile , Form, Depends 
from app.schemas import PoseCreate , PostResponse 
from app.db import Post, create_db_and_tables, create_async_engine , get_async_session 
from contextlib import asynccontextmanager  



@asynccontextmanager 
async def lifespan(app :FastAPI) : 
    await create_db_and_tables() ; 
    yield  
    
app = FastAPI(lifespan=lifespan) ; 

@app.post("/upload") 
async def upload_file(file : UploadFile = File(...) , 
                      caption : str = Form(""), 
                      session : AsyncSession  = Depends(get_async_session)) :  
    post = Post(
        caption = caption , 
        url = "dummy url" , 
        file_type = "photo" , 
        file_name =  "dummy_name" 
    ) 
    session.add(post) ; 
    await session.commit() ; 
    await session.refresh(post) ; 