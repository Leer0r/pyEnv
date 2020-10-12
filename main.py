import os
import re

def env(location=".", error=False):
    if not os.path.exists(os.path.join(location,".env")):
        if error:
            print(f"File .env not fount at {location}")
        return None
    path = os.path.join(location,".env")
    content = {}
    count = 0
    options = re.findall(r"([\w\.-]+)=([\w\.-]+)", open(path,"r").read())
    if options:
        for option in options:
            content[option[0]] = option[1]
            count += 1
        return Env(content, count)
    return None
    

class Env(object):
    def __init__(self,content,count):
        self.content = content
        self.count = count