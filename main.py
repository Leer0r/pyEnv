import os
import re

def env(location:str =".", error:bool=False,output="dict",warning=False):
    r"""
    Environnement function to get variable and value from a .env file
    
        -location (str) : Specify a path (relative or absolute) to the .env file
        -error (bool) : Display error
        -warning (bool) : Display warning
        -output (str) : output format
    """
    if not os.path.exists(os.path.join(location,".env")) or output not in ["dict","obj"]:
        return None
    if(output != "obj"): 
        if(warning): print("Youre using the object mod, witch is a little buggy with modern ide (check ... to more information)")
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
    return Env(content,count) if output == "dict" else Env_obj(content,count)

def exist(obj:dict,key:any):
    try:
        obj[key]
        return True
    except KeyError:
        return False

class Env(object):
    def __init__(self,content,count):
        self.count = count
        self.content = content
        self.environ = {}
        self.add_content()
    
    def add_content(self):
        for key, value in os.environ.items():
            self.environ[key] = value

class Env_obj(object):
    def __init__(self,content,count):
        self.count = count
        self.compile(content)
    
    def compile(self,content):
        for key,value in content.items():
            setattr(self,key,value)
        for key, value in os.environ.items():
            setattr(self,key,value)
