from pathlib import Path
from typing import Dict, List


KNOWLEDGE_BASE_PATH = Path("data/knowledge_base")


def load_knowledge_base(language: str = "es") -> Dict[str, str]:
    """
    Loads synthetic knowledge base documents.

    language="es" loads Spanish documents ending in .es.md.
    language="en" loads English documents that do not end in .es.md.
    """
    documents = {}

    if language == "es":
        files = KNOWLEDGE_BASE_PATH.glob("*.es.md")
    else:
        files = [
            file for file in KNOWLEDGE_BASE_PATH.glob("*.md")
            if not file.name.endswith(".es.md")
        ]

    for file in files:
        documents[file.name] = file.read_text(encoding="utf-8")

    return documents


def keyword_search(query: str, documents: Dict[str, str], top_k: int = 2) -> List[Dict[str, str]]:
    """
    Very simple keyword-based retrieval.
    This is intentionally lightweight for the first prototype.
    """
    query_terms = set(query.lower().replace("¿", "").replace("?", "").split())
    results = []

    for document_name, content in documents.items():
        content_lower = content.lower()
        score = sum(1 for term in query_terms if term in content_lower)

        if score > 0:
            results.append({
                "document": document_name,
                "score": score,
                "content_preview": content[:900]
            })

    results = sorted(results, key=lambda item: item["score"], reverse=True)

    return results[:top_k]
