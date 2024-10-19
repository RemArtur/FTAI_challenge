import pandas as pd

def algorithm(users_js, biographies_js, posts_js, friends_js, groups_js, photos_js):
    users = pd.dataframe(users_js)
    bios = pd.dataframe(biographies_js)
    posts = pd.dataframe(posts_js)
    friends = pd.dataframe(friends_js)
    groups = pd.dataframe(groups_js)
    photos = pd.dataframe(photos_js)
    return [0]