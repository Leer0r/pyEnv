import os
import re

def env(location:str =".", error:bool =False):
    if not os.path.exists(os.path.join(location,".env")):
        return None
    path = os.path.join(location,".env")
    content = {}
    count = 0
    p = re.compile(r"([\w\.-]+)=([\w\.-]+)")
    with open(path,"r") as env:
        line = env.readline()
        while line != "":
            res = p.match(line)
            if res:
                _split = res.group().split("=",1)
                if error:
                    if exist(content,_split[0]):
                        print(f"Environement varable {_split[0]} already exist")
                content[_split[0]] = _split[1]
                count += 1
            line = env.readline()
    return Env(content, count)
    
def exist(obj:object,key:str):
    try:
        obj[key]
        return True
    except KeyError:
        return False

class Env(object):
    def __init__(self,content,count):
        self.content = content
        self.count = count

test = env(error=True)
if test:
    print(test.content)