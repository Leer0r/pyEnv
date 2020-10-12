# pyEnv

Portage de la fonctionnalité env de JS sur python

## Utilisation :
```python
from pyenv import env

env = env()
```

## Structure de env : 
* content : Dictionnaire contenant les noms de variables et leurs valeurs
* count : contiend le nombres de variables d'environement valide
## Valeurs de retour possible
* None : Le fichier .env n'a pas été trouvé
* structure env : Au moins une valeur valide a été trouvée dans le fichier .env

## Arguments annexe
* location (str) : Il est possible de spécifier une localisation spéciale du fichier .env (pour les projet partagent le même fichier)
  * utilisation : 
  ```python
  env = env(location=path_to_.env)
  ```
  * Valeur par default : "." (pwd)
* error (bool) : Afficher les erreurs
  * utilisation : 
  ```
  env = env(error=True)
  ```
  * Valeur par default : False


