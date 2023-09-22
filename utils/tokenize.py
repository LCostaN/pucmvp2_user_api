import os
import jwt

secret = os.environ['SECRET']
secret2 = os.environ['SECRET2']

def tokenize(username: str):
  return jwt.encode({"username": username, "secret": secret2}, secret, algorithm="HS256")