# pyEnv

Adaptation of the js module environ in python

## How to use :
```python
from pyEnv import env

env:Env = env()
```

## env's structure : 
There are 2 different structures : in dictionnary or in object :
* Dictionnary (Env class) contain two variable : 
  * content : An object who contain all couple <key,value> match by the algorithm 
  * environ : An another object who contain all environnement variable avariable
  * count : Number of couple match in .env file
* Object (Env_obj class) contain :
  * count : Number of couple match
  * an attribute for each match variable in the .env file
    * Exemple : if .env contain aaa=bbb, env.aaa contain bbb (String type)

  Note : Env_obj is in beta because he is buggy : in fact, most of IDE give an error because all attribute (except count) is create dynamiquely. I try to search an optional method to fix that

Dev note : Soon, the algorithm will inculde integer conversion

## Return value
* None : No .env file was found and/or output value not correct
* Env structure
  * Env_dict by default (output=dict)
  * Env_obj if output=obj

  Note : you can check if there is no match in the .env file by 
  ```python
  env.count == 0
  ```

## Optionnal argument
* location (str) : Specify a path (relative or absolute) to the .env file
  * Using : 
  ```python
  env = env(location=path_to_.env)
  ```
  * Default value : "." (pwd)
* error (bool) : Display error
  * Using : 
  ```
  env = env(error=True)
  ```
  * Default value : False
* warning (bool) : Display warning
  * Using : 
    ```
    env = env(warning=True)
    ```
  * Default value : False
* output (str) : output format
  * Using: 
    ```python
    env = env(output="obj")
    ```
  * Default value : dict

## Value specification
The algorithm will match with :
* Character specification 
  * any word character (lowercase and uppercase)
  * .
  * /
  * :
  * \
  * _
  * \-
* Patern specification
  * The right patern is the folowing : (Character specification)=(Character specification)
  * Please note there is no sepearation between the Character specification and = symbol, and space is not a valable character
* You can use comment with the # character