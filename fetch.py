import requests

def fetch_github_repositories():
    response = requests.get("https://api.github.com/users/vestinabert/repos")
    repos = response.json()
    return sorted(repos, key=lambda x: x["created_at"], reverse=True)


def fetch_nasa_apod():
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    return response.json()


def fetch_color_palette():
    response = requests.post("http://colormind.io/api/", json={"model": "ui"})
    data = response.json()
    return "#{:02x}{:02x}{:02x}".format(*data["result"][0])