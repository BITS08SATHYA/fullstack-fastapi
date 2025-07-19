from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello World'}

# class BlogType(str, Enum):
#     short: 'short'
#     story: 'story'
#     howto: 'howto'
# @app.get('/blog/type/{type}')
# def get_blog_type(type: BlogType):
#     return {'message': f'Blog type: {type.value}'}

@app.get('/blog/all')
def get_all_blog():
    return {'message': 'All blogs provided'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {"message": f"Blog type: {type.value}"}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message' : f'Blog with id: {id}'}


# @app.get('/blog/all')
# def get_all_blogs(page=1, page_size=10):
#     return {'message': f'All {page_size} blogs on page {page}'}


#
# @app.get('/blog/{id}')
# def get_blog(id: int):
#     return {'message': f'Blog with id {id}'}