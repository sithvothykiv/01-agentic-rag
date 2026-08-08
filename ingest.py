import json
from minsearch import Index


def load_faq_data():
    documents = []

    file_path = "/Users/kivsithvothy/Downloads/01-agentic-rag/documents/all_documents.json"

    with open(file_path, 'r', encoding='utf-8') as f:
        documents = json.load(f)

    for doc in documents:
        doc["doc_id"] = doc.pop("id") #we do this so we can add the id key to sqlite so we don't reimport the same records

    return documents


def build_index(documents):
    index = Index(
        text_fields=['question', 'section', 'answer'],
        keyword_fields=['course']
    )
    index.fit(documents)
    return index
