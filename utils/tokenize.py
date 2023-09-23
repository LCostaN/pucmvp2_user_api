import os
import jwt

secret = os.environ['SECRET']

def tokenize(username: str):
  return jwt.encode({"username": username}, secret, algorithm="HS256")