# test-technique-deep-learning

## Description

Script python3 permettant de se connecter sur Facebook et de colleter des postes (image, texte et commentaires liés aux images) 
par rapport à un sujet défini, exemple « le décès du président Jacques Chirac ».

## Requirements
Pour pouvoir exécuter ce script, il faut avoir en jeton d'access pour l'api Graph Facebook (il faut un compte développeur Facebook)
Il faut aussi installer mongo-db et les packages Python suivants: facebook-sdk, pymongo

pip install facebook-sdk pymongo

## Comment utiliser
Changez la valeur de l'access token dans le fichier config.json et mettez un token que vous récupérez depuis votre compte développeur Facebook. Puis lancez `python_question_3.py`
