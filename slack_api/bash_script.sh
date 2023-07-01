#!/bin/bash
set -euo pipefail
FAILURE=1
SUCCESS=0
SLACKWEBHOOKURL="https://hooks.slack.com/services/FAKE_WEBHOODK"

function print_slack_summary_build() {
    local slack_msg_header
    local slack_msg_body
    local slack_channel
    
    # Populate header and define slack channels
    slack_msg_header=":x: *Build to ${ENVIRONMENTNAME} failed*"
    if [[ "${EXIT_STATUS}" == "${SUCCESS}" ]]; then
        slack_msg_header=":heavy_check_mark: *Build to ${ENVIRONMENTNAME} succeeded*"
        #slack_channel="$CHANNEL_TEST"
    fi
cat <<-SLACK
            {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "${slack_msg_header}"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Stage:*\nBuild"
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Pushed By:*\n${GITLAB_USER_NAME}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Job URL:*\nGITLAB_REPO_URL/${CI_JOB_ID}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Commit URL:*\nGITLAB_REPO_URL$(git rev-parse HEAD)"
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Commit Branch:*\n${CI_COMMIT_REF_NAME}"
                            }
                        ]
                    },
                    {
                        "type": "divider"
                    }
                ]
    }
SLACK
}
function share_slack_update_build() {
    local slack_webhook
    slack_webhook="$SLACKWEBHOOKURL"
    curl -X POST                                           \
    --data-urlencode "payload=$(print_slack_summary_build)"  \
    "${slack_webhook}"
}