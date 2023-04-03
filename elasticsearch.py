from elasticsearch import Elasticsearch

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Indexer les données de sentiment
doc = {
    "positive_percent": 50,
    "negative_percent": 10,
    "neutral_percent": 40
}
es.index(index="sentiment-graph", body=doc)

@registry.register_document
class SentimentGraph(Document):
    positive_percent = fields.FloatField()
    negative_percent = fields.FloatField()
    neutral_percent = fields.FloatField()

    class Index:
        name = 'sentiment-graph'
