# prune-slack
A utility to remove files older than 7 days from a Slack instance

## Running the script
    python prune-slack [instance_name]

Where _instance_name_ is (optionally) the Slack instance URL slug to access, for example `python prune-slack acme-coders` would remove your aged files from the instance at `acme-coders.slack.com`

## Requirements
The script expects a [Slack Legacy API token](https://api.slack.com/custom-integrations/legacy-tokens) to be held in an environment variable `SLACK_TOKEN`.

## Output
The script will output a message with the filename and ID of every file it tries to delete and the response JSON of the deletion attempt, for example:

    Deleting file image.png... FEF6BTUKZ
    {u'ok': True}
    Deleting file example PN.jpg... FEFCFT3GD
    {u'ok': True}
    DONE!
