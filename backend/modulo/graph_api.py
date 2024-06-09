import requests
import json
from datetime import datetime, timedelta , timezone
import pytz


class graph_values:
    def __init__(self,github_token,username):
        self.GITHUB_TOKEN = github_token
        self.USERNAME = username
        self.HEADERS = {
            'Authorization': f'token {self.GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }
        # Fetch Pull Requests
        self.pr_url = f'https://api.github.com/search/issues?q=type:pr+author:{self.USERNAME}'
        self.pr_response = requests.get(self.pr_url, headers=self.HEADERS)
        self.pull_requests = self.pr_response.json()

        # Fetch Issues
        self.issue_url = f'https://api.github.com/search/issues?q=type:issue+author:{self.USERNAME}'
        self.issue_response = requests.get(self.issue_url, headers=self.HEADERS)
        self.issues = self.issue_response.json()

        # Fetch Commits
        self.commit_url = f'https://api.github.com/search/commits?q=author:{self.USERNAME}'
        self.commit_headers = self.HEADERS.copy()
        self.commit_headers['Accept'] = 'application/vnd.github.cloak-preview+json'
        self.commit_response = requests.get(self.commit_url, headers=self.commit_headers)
        self.commits = self.commit_response.json()
    # Example date string
    # date_str = "2024-02-01T23:25:18.000+05:30"

    def make_arr_commit(self,req_doc):
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
        return(last_30_days)

    def make_arr(self,req_doc):
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
        return(last_30_days)
    
    def return_values(self):
        self.commits_arr = self.make_arr_commit(self.commits)
        self.pull_requests_arr = self.make_arr(self.pull_requests)
        self.issue_arr = self.make_arr(self.issues)


def main():
    values = graph_values('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','sarveshdakhore')
    values.return_values()
    print(values.commits_arr)
    print(values.pull_requests_arr)
    print(values.issue_arr)


if __name__ == "__main__":
    main()