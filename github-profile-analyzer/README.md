# GitHub Profile Analyzer

A beginner-friendly Python project that uses the GitHub REST API to retrieve a GitHub user's profile information, list their public repositories, and display details about a selected repository.

## Features

- Display a user's name, public repository count, followers, and following.
- List the user's public repositories.
- Show details for a selected repository:
  - Repository name
  - Stars
  - Forks
  - Open issues
  - Repository URL
- Display the programming languages used in a repository.
- Fetch and display the repository's README content.

## Requirements

- Python 3
- `requests` library

## Installation

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install the dependency:

   ```bash
   pip install -r requirements.txt
   ```

If you do not have a `requirements.txt` file yet, you can install the library directly:

```bash
pip install requests
```

## Run the Project

Run the Python script:

```bash
python main.py
```

Enter a GitHub username when prompted. The program displays the user's profile and public repositories. Then enter a repository name to view its details, languages, and README.

## How It Works

The project uses GitHub's public REST API endpoints:

- User profile: `https://api.github.com/users/{username}`
- User repositories: `https://api.github.com/users/{username}/repos`
- Repository details: `https://api.github.com/repos/{username}/{repo_name}`
- Repository languages: `https://api.github.com/repos/{username}/{repo_name}/languages`
- Repository README: `https://api.github.com/repos/{username}/{repo_name}/readme`

The `requests` library sends HTTP requests, and the returned JSON data is used to display information in the terminal.

## Project Structure

```text
github-profile-analyzer/
├── main.py
├── README.md
└── requirements.txt
```

## Technologies Use
- Python
- Requests
- GitHub REST API
- JSON