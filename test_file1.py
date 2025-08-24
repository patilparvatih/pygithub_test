from github import Github
import base64
api_key = "YOUR_GitHub_Account_API_KEY_from_website"
# Initialize the GitHub object
git = Github(api_key)
user = git.get_user()
