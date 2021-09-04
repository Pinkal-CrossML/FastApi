from fastapi import FastAPI
from fastapi.params import Body
# from pydantic import

app = FastAPI()

class Blog():
      title:str
      
      body:

@app.post('/blog')

def create(request: Blog):

      return request