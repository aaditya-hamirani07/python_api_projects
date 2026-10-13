import requests
def get_profile(username):
    profile = requests.get(f"https://api.github.com/users/{username}")
    return profile

def display_profile(data):
    print("Name:", data["name"] or "Name not provided")
    print("Public repositories:", data["public_repos"])
    print("Followers:", data["followers"])
    print("Following:", data["following"])

def get_repositories(username):
    repo = requests.get(f"https://api.github.com/users/{username}/repos")
    return repo

def display_repositories(repo):
    if repo.status_code == 200:
        repo_names = repo.json()
        print("\nRepository names:")
        for n, r in enumerate(repo_names):
            print(n + 1, r["name"])
    else:
        print("Could not fetch repositories.")

def get_repository_details(username, repo_name):
    repo = requests.get(
        f"https://api.github.com/repos/{username}/{repo_name}"
    )
    return repo

def display_repository_details(repo):
    if repo.status_code == 200:
        data = repo.json()

        print("\nRepository Details:")
        print("Name:", data["name"])
        print("Stars:", data["stargazers_count"])
        print("Forks:", data["forks_count"])
        print("Open issues:", data["open_issues_count"])
        print("URL:", data["html_url"])
    else:
        print("Repository not found!")

def display_languages(username, repo_name):
    languages = requests.get(
        f"https://api.github.com/repos/{username}/{repo_name}/languages"
    )

    if languages.status_code == 200:
        print("Languages:", ", ".join(languages.json().keys()))
    else:
        print("Could not fetch languages.")

def display_readme(username, repo_name):
    readme = requests.get(
        f"https://api.github.com/repos/{username}/{repo_name}/readme"
    )

    if readme.status_code == 200:
        readme_data = readme.json()

        print("\nREADME content:")
        print(requests.get(readme_data["download_url"]).text)
    else:
        print("README not found.")

username = input("Enter username: ")

profile = get_profile(username)
data = profile.json()
status_code = profile.status_code

if status_code == 200:
    display_profile(data)

    repo = get_repositories(username)
    display_repositories(repo)

    repo_name = input("\nEnter repository name whose details you want: ")

    repo_details = get_repository_details(username, repo_name)
    display_repository_details(repo_details)

    if repo_details.status_code == 200:
        display_languages(username, repo_name)
        display_readme(username, repo_name)
else:
    print("User not found!")