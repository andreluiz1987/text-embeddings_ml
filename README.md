# Text Embeddings ML

This project written in Python is an exercise on text embeddings and vectors in Elasticsearch. A movie dataset will have the description field represented by a vector and we will use the semantic search to get results with KNN search.

Read about [Compatible third party NLP model](https://www.elastic.co/guide/en/machine-learning/current/ml-nlp-model-ref.html#ml-nlp-model-ref-text-embedding).

## Technologies

* Python
* Elasticsearch

## Pre-requisites

### Run docker-compose

````
docker-compose up -d
````
### Mapping

````
{
   "mappings":{
      "properties":{
         "actors":{
            "type":"text",
            "fields":{
               "keyword":{
                  "type":"keyword",
                  "ignore_above":256
               }
            },
            "analyzer":"en_analyzer"
         },
         "avatar":{
            "type":"keyword"
         },
         "certificate":{
            "type":"keyword"
         },
         "code":{
            "type":"long"
         },
         "date":{
            "type":"keyword",
            "doc_values":false
         },
         "description":{
            "type":"text",
            "fields":{
               "keyword":{
                  "type":"keyword",
                  "ignore_above":256
               }
            },
            "analyzer":"en_analyzer"
         },
         "description_vector":{
            "type":"dense_vector",
            "dims":384,
            "index":true,
            "similarity":"cosine"
         },
         "director":{
            "type":"text",
            "fields":{
               "keyword":{
                  "type":"keyword",
                  "ignore_above":256
               }
            }
         },
         "genre":{
            "type":"text",
            "fields":{
               "keyword":{
                  "type":"keyword",
                  "ignore_above":256
               }
            }
         },
         "metascore":{
            "type":"long"
         },
         "rating":{
            "type":"float"
         },
         "revenue":{
            "type":"keyword"
         },
         "runtime":{
            "type":"keyword"
         },
         "title":{
            "type":"text",
            "fields":{
               "suggest":{
                  "type":"text",
                  "analyzer":"shingle_analyzer"
               }
            },
            "analyzer":"en_analyzer"
         },
         "title_suggest":{
            "type":"completion",
            "analyzer":"simple",
            "preserve_separators":true,
            "preserve_position_increments":true,
            "max_input_length":50
         },
         "votes":{
            "type":"long"
         },
         "year":{
            "type":"long"
         }
      }
   },
   "settings":{
      "number_of_shards":"1",
      "analysis":{
         "filter":{
            "shingle_filter":{
               "max_shingle_size":"3",
               "min_shingle_size":"2",
               "type":"shingle"
            }
         },
         "analyzer":{
            "shingle_analyzer":{
               "filter":[
                  "lowercase",
                  "shingle_filter"
               ],
               "type":"custom",
               "tokenizer":"standard"
            },
            "en_analyzer":{
               "filter":[
                  "lowercase",
                  "stop"
               ],
               "tokenizer":"standard"
            }
         }
      },
      "number_of_replicas":"0"
   }
}
````

### Insert data

````
 python ingestion.py
````
 
### Run project

````
 python main.py
 ````

[//]: # (## More information)

[//]: # ()
[//]: # (For more information visit)

[//]: # (post []&#40;&#41;.)
