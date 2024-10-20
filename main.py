import pandas as pd
from ollama_func import llama_request_emotion, llama_request_theme, export_defined_theme, export_defined_type
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import sqlite3
def make_csv(filename):
    cnx = sqlite3.connect(filename)
    user = pd.read_sql_query("SELECT * FROM user", cnx)
    bio = pd.read_sql_query("SELECT * FROM biography", cnx)
    friend = pd.read_sql_query("SELECT * FROM friend", cnx)
    group = pd.read_sql_query("SELECT * FROM group_table", cnx)
    photo = pd.read_sql_query("SELECT * FROM photo", cnx)
    post = pd.read_sql_query("SELECT * FROM post", cnx)
    d = algorithm(user, bio, post, friend, group, photo)
    df = pd.DataFrame.from_dict(d, orient="index")
    df.to_csv(filename[:-2] + "csv")
def analize(text):
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    if (scores['neu'] == max(scores["neu"], scores["neg"], scores["pos"])):
        return 0
    elif (scores['pos'] == max(scores["neu"], scores["neg"], scores["pos"])):
        return 1
    else:
        return 2
def algorithm(users_js, biographies_js, posts_js, friends_js, groups_js, photos_js):
    users = pd.DataFrame(users_js)
    bios = pd.DataFrame(biographies_js)
    posts = pd.DataFrame(posts_js)
    friends = pd.DataFrame(friends_js)
    groups = pd.DataFrame(groups_js)
    photos = pd.DataFrame(photos_js)
    # обработка LLM
    posts["type"] = posts["text"].apply(llama_request_emotion)
    groups["theme"] = groups["description"].apply(llama_request_theme)
    groups["type"] = groups["description"].apply(llama_request_emotion)
    # Определение типов
    posts["type"] = posts["type"].apply(export_defined_type)
    groups["type"] = groups["type"].apply(export_defined_type)
    groups["theme"] = groups["type"].apply(export_defined_theme)
    # Определение типа фотографии
    photos["type"] = photos["igm2txt"].apply(analize)

    return {1: ["1ЭАГ", "Описание 1ЭАГ"] }
