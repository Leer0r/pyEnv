import os
import re

def env(location:str =".", error:bool=False,output="dict"):
    if not os.path.exists(os.path.join(location,".env")) or output not in ["dict","obj"]:
        return None
    path = os.path.join(location,".env")
    content = {}
    count = 0
    p = re.compile(r"([\w\.\-\_\:\/\\]+)=([\w\.\-\_\:\/\\]+)")
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
    return Env_dict(content,count) if output == "dict" else Env_obj(content,count)
    
def exist(obj:object,key:str):
    try:
        obj[key]
        return True
    except KeyError:
        return False

class Env(object):
    pass

class Env_dict(object):
    def __init__(self,content,count):
        self.count = count
        self.content = content

class Env_obj(object):
    def __init__(self,content,count):
        self.count = count
        self.compile(content)
    
    def compile(self,content):
        for key,value in content.items():
            setattr(self,key,value)

