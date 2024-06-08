import requests
import json
from datetime import datetime, timedelta , timezone
import pytz

GITHUB_TOKEN = 'git hub token'
USERNAME = 'devHarshShah'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Fetch Pull Requests
pr_url = f'https://api.github.com/search/issues?q=type:pr+author:{USERNAME}'
pr_response = requests.get(pr_url, headers=HEADERS)
pull_requests = pr_response.json()

# Fetch Issues
issue_url = f'https://api.github.com/search/issues?q=type:issue+author:{USERNAME}'
issue_response = requests.get(issue_url, headers=HEADERS)
issues = issue_response.json()

# Fetch Commits
commit_url = f'https://api.github.com/search/commits?q=author:{USERNAME}'
commit_headers = HEADERS.copy()
commit_headers['Accept'] = 'application/vnd.github.cloak-preview+json'
commit_response = requests.get(commit_url, headers=commit_headers)
commits = commit_response.json()

# Print results
# print(f"Pull Requests: {pull_requests}")
# with open('pull_req_json.json', 'a') as f:
#     f.write(json.dumps(pull_requests, indent=4))
# print(f"Issues: {issues}")
# with open('issues_json.json', 'a') as f:
#     f.write(json.dumps(issues, indent=4))
# print(f"Commits: {commits}")
# with open('commits_json.json', 'a') as f:
#     f.write(json.dumps(commits, indent=4))




# Example date string
# date_str = "2024-02-01T23:25:18.000+05:30"

def make_arr_commit(req_doc):
    # Initialize the array for the last 30 days
    last_30_days = [0] * 30
    # Parse the date string
    for i in req_doc['items']:
        date_str = i['commit']['author']['date']
        date = datetime.strptime(date_str[:-6], '%Y-%m-%dT%H:%M:%S.%f')
        offset_hours, offset_minutes = map(int, date_str[-5:].split(':'))
        tz_offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        date = date.replace(tzinfo=pytz.FixedOffset(offset_hours * 60 + offset_minutes))

        # Get current time in the same timezone as the input date
        now = datetime.now(pytz.FixedOffset(offset_hours * 60 + offset_minutes))

        # Calculate the difference in days
        days_diff = (now - date).days

        # Check if the date falls within the last 30 days
        if 0 <= days_diff < 30:
            last_30_days[days_diff] += 1

        # Output the results
    print(last_30_days)

def make_arr(req_doc):
    # Initialize the array for the last 30 days
    last_30_days = [0] * 30
    # Parse the date string
    for i in req_doc['items']:
        date_str = i['created_at']
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
        date = date.replace(tzinfo=timezone.utc)

        # Get current time in the same timezone as the input date
        now = datetime.now(timezone.utc)

        # Calculate the difference in days
        days_diff = (now - date).days

        # Check if the date falls within the last 30 days
        if 0 <= days_diff < 30:
            last_30_days[days_diff] += 1

        # Output the results
    print(last_30_days)


make_arr_commit(commits)
make_arr(pull_requests)
make_arr(issues)