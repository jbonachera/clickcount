#!/usr/bin/env python2

import os
import httplib
import json

__NOMAD_URL__ = os.environ.get('NOMAD_URL')
__JOB_ID__ = os.environ.get('JOB_ID')
__AUTH_TOKEN__ = os.environ.get('NOMAD_AUTH_TOKEN')
__IMAGE__ = os.environ.get('IMAGE')
__TAG__ = os.environ.get('TAG')

class main:
    """
    Fetch a job from nomad, and update it
    """
    def __init__(self):
        updated = False
        taskgroup_name = ''
        task_name = ''
        nomad = httplib.HTTPConnection(__NOMAD_URL__)
        headers = {'X-Auth-Token': __AUTH_TOKEN__}
        nomad.request("GET", '/v1/job/%s' % __JOB_ID__, '', headers)
        job = json.loads(nomad.getresponse().read())
        for taskgroup in job.get('TaskGroups'):
            for task in taskgroup.get('Tasks'):
                if task.get('Config').get('image').split(':')[0] == __IMAGE__:
                    task['Config']['image'] = "%s:%s" % (__IMAGE__, __TAG__)
                    updated = True
        if updated:
            params = json.dumps({'Job': job})
            nomad.request("POST", '/v1/job/%s' % __JOB_ID__, params, headers)
            update_request = json.loads(nomad.getresponse().read())
            print("Request status: %s" % update_request)

main()
