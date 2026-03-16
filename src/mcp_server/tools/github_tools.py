import requests

GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"


def search_repository(query: str, top_k: int = 3):

    params = {"q": query, "sort": "stars", "order": "desc", "per_page": top_k}

    response = requests.get(GITHUB_SEARCH_URL, params=params)
    print(response)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")

    data = response.json()
    print(data)
    repositories = []

    for repo in data.get("items", [])[:top_k]:

        repo_info = {
            "name": repo["name"],
            "full_name": repo["full_name"],
            "description": repo["description"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
            "language": repo["language"],
        }

        repositories.append(repo_info)

    return repositories


if __name__ == "__main__":
    repos = search_repository(" RAG", 5)
    print(type(repos))
    for rep in repos:
        for i in rep:
            print(i, "->", rep[i])

        print("\n")
    # print(repos)
