import requests

def create_github_repo(repo_name, access_token):
    # Set the headers and data for the API call
    headers = {'Authorization': f'token {access_token}'}
    data = {'name': repo_name}

    # Make the API call to create the repository
    response = requests.post('https://api.github.com/user/repos', headers=headers, json=data)

    # Check if the response was successful
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
    else:
        print(f"Failed to create repository '{repo_name}'. Reason: {response.text}")
access_token = ${{secrets.PAT}}
repo_name = 'my-new-repo'

create_github_repo(repo_name, access_token)
