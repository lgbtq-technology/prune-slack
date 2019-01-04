#!/usr/bin/env python

import sys
import requests
import json
import calendar
import os
from datetime import datetime, timedelta

_token = os.environ['SLACK_TOKEN']
_instance_name = "lgbt"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        _instance_name = sys.argv[1]

    while 1:
        files_list_url = 'https://slack.com/api/files.list'
        date = str(calendar.timegm((datetime.now() + timedelta(-7))
            .utctimetuple()))
        data = {"token": _token, "ts_to": date}
        response = requests.post(files_list_url, data = data)
        if len(response.json()["files"]) == 0:
            break
        for f in response.json()["files"]:
            print "Deleting file " + f["name"] + "... " + f["id"]
            timestamp = str(calendar.timegm(datetime.now().utctimetuple()))
            delete_url = "https://" + _instance_name + ".slack.com/api/files.delete?t=" + timestamp
            response = requests.post(delete_url, data = {
                "token": _token,
                "file": f["id"]
            })
            print response.json()
    print "DONE!"
