from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from typing import List
from ..Schemas import *
from ..db import get_db
from .. import models

router=APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get('/',response_model=List[PostBase])
def get_posts(db:Session=Depends(get_db)):
    posts=db.query(models.Post).all()
    if posts: 
        return posts
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Posts not found")

# post blogs
@router.post('/',response_model=PostCreate,status_code=status.HTTP_201_CREATED)
def create_posts(post:PostBase,db:Session=Depends(get_db)):
    new_posts= models.Post(**post.dict())
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    return new_posts

# get by id
@router.get('/{id}',response_model=PostBase)
def get_user_by_id(id:int, db:Session=Depends(get_db)):
    posts=db.query(models.Post).filter(models.Post.id==id).first()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not found")
    return posts

# put
@router.put('/{id}',response_model=PostBase)
def create_Posts(updated_post:PostCreate,id:int,db: Session = Depends(get_db)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    new_post=post_query.first()
    if not new_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} cannot be found. Please enter a valid id.")
    else:   
        post_query.update(updated_post.model_dump(), synchronize_session=False) #type: ignore
        db.commit()
        db.refresh(new_post)
    
        return post_query.first()

#delete
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def detlete_post(id:int, db:Session=Depends(get_db)):
    delete_post=db.query(models.Post).filter(models.Post.id==id).first()
    if not delete_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not found")
    db.delete(delete_post)
    db.commit()
    
    