#!/bin/bash

set -euo pipefail

FAILURE=1
SUCCESS=0
SLACKWEBHOOKURL="https://hooks.slack.com/services/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"

function testing() {
    local var1
    local var2
    
    var1="First Env ${ENV1}"
    if [[ "${EXIT_STATUS}" == "${SUCCESS}" ]]; then
        var2="Second Env ${ENV2}"
    fi
    
cat <<-SLACK
            {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "TESTING"
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
                                "text": "*Pushed By:*\nAbdul"
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Job URL:*\nGITLAB_REPO_URL/TEST_JOB"
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Commit URL:*\nGITLAB_REPO_URL$(git rev-parse HEAD)"
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Commit Branch:*\nTEST_JOB"
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
    --data-urlencode "payload=$(testing)"  \
    "${slack_webhook}"
}