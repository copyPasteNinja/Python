import pprint, json, time, sys, urllib3, random

def demo_users():
    users = []
    http = urllib3.PoolManager()
    github_url = "https://api.github.com/repos/akumosolutions/ansible_roles_oct2021/contributors"
    response = http.request('GET', github_url)
    parsed = json.loads(response.data)
    for user in parsed:
        users.append({'username': user['login'], 'github_profile': user['html_url']})
    return users

def randomly_chosen():
    user_list = demo_users()
    chosen_one = random.choice(user_list)
    return chosen_one

def post_to_slack():
    chosen_one = randomly_chosen()
    slack_message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Our demo presenter for this month is..."
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": '*<%s| %s>*\n Please prepare a topic of your choosing for the last Saturday of the Month! Please provide @Abdul of the topic you chose. Arigato' % (chosen_one['github_profile'], chosen_one['username'])
                }
            },
            {
                "type": "divider"
            }
        ]
    }
    slacK_message = slack_message
    http = urllib3.PoolManager()
    slack_url = "https://hooks.slack.com/services/FAKE_WEBHOOK"
    encoded_data = json.dumps(slacK_message)
    response = http.request("POST", slack_url, body=encoded_data, headers={'Content-Type': 'application/json'})


post_to_slack()