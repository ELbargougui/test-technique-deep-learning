#!/usr/bin/env python
# coding: utf-8

import json
import facebook
import pymongo


# Collecte des publications Facebook
def collect_facebook_posts(collection):
    graph = facebook.GraphAPI(access_token=FACEBOOK_ACCESS_TOKEN)
    posts = graph.get_all_connections(id='me', connection_name='posts')

    for post in posts:
        if 'message' in post and 'jacques chirac' in post['message'].lower():
            save_post(post['id'], post['message'], 'facebook', collection)


# Sauvegarde des publications dans MongoDB
def save_post(post_id, content, source, collection):
    post_data = {
        'post_id': post_id,
        'content': content,
        'source': source
    }
    collection.insert_one(post_data)
    print(f"Post saved: {post_id}")


if __name__ == '__main__':
    # lire la configuration
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Paramètres de connexion à MongoDB
    MONGODB_HOST = config['mongo_db_config']['MONGODB_HOST']
    MONGODB_PORT = config['mongo_db_config']['MONGODB_PORT'] 
    MONGODB_DB = config['mongo_db_config']['MONGODB_DB'] 
    MONGODB_COLLECTION = config['mongo_db_config']['MONGODB_COLLECTION'] 

    # Paramètres d'authentification Facebook
    FACEBOOK_ACCESS_TOKEN = config['credentials']['access_token']

    # Initialisation de la connexion MongoDB
    client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = client[MONGODB_DB]
    collection = db[MONGODB_COLLECTION]

    # Exécution de la collecte des publications
    collect_facebook_posts(collection)




