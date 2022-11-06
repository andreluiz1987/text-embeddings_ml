import json

from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch


def get_client_es():
    return Elasticsearch(
        hosts=[{'host': 'localhost', 'port': 9200}]
    )


def insert_data(movies):
    for movie in movies:
        sentences = [movie["description"]]
        embeddings = get_text_vector_model_msmarco(sentences)
        movie["description_vector"] = embeddings[0]
        print(f'Last movies processed {movie["title"]}')
        get_client_es().index(index="idx_movies_vector", body=movie, refresh="wait_for")


def get_text_vector_model_msmarco(sentences):
    model = SentenceTransformer('sentence-transformers/msmarco-MiniLM-L-12-v3')
    embeddings = model.encode(sentences)
    #print("Embedding size: {}".format(len(embeddings[0])))
    #print(*embeddings[0], sep=", ")
    return embeddings


def get_text_vector_model_all_distilroberta(sentences):
    model = SentenceTransformer('sentence-transformers/all-distilroberta-v1')
    embeddings = model.encode(sentences)
    return embeddings


def generate():
    f = open('imdb_poster.json')
    movies = []
    data = json.load(f)
    n = 0
    for i in data:
        n = n + 1
        info = {
            "code": n,
            "title": i["Series_Title"],
            "title_suggest": list(str(i["Series_Title"]).split()),
            "genre": list(i["Genre"].replace(" ", "").split(",")),
            "director": i["Director"],
            "actors": [i["Star1"], i["Star2"], i["Star3"], i["Star4"]],
            "description": i["Overview"],
            "year": i["Released_Year"],
            "runtime": i["Runtime"],
            "rating": i["IMDB_Rating"],
            "votes": i["No_of_Votes"],
            "revenue": i["Gross"],
            "metascore": i["Meta_score"],
            "certificate": i["Certificate"],
            "avatar": i["Poster_Link"]
        }
        movies.append(info)

    # Closing file
    f.close()

    return movies


if __name__ == '__main__':
    movies = generate()
    insert_data(movies)

