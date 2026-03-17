import warnings
from typing import Any, Dict, List

import wikipedia

warnings.filterwarnings("ignore")


def search_wikipedia_articles(topics: List[str]) -> Dict[str, Any]:
    results = []

    for topic in topics:
        try:
            page = wikipedia.page(topic, auto_suggest=True)

        except wikipedia.exceptions.DisambiguationError as e:
            try:
                page = wikipedia.page(e.options[0])
            except Exception:
                results.append({"topic": topic, "status": "page_not_found"})
                continue

        except wikipedia.exceptions.PageError:
            results.append({"topic": topic, "status": "page_not_found"})
            continue

        # summary = wikipedia.summary(page.title, sentences=5)
        # summary = page.summary
        summary = page.summary.split(". ")[:5]
        summary = ". ".join(summary)

        results.append(
            {
                "topic": topic,
                "title": page.title,
                "summary": summary,
                "url": page.url,
                "page_id": page.pageid,
                "status": "success",
            }
        )

    return results


if __name__ == "__main__":
    results = search_wikipedia_articles(
        ["india", "What is langchain", "Python programming language"]
    )
    print(f"results \n\n\n {results}")
