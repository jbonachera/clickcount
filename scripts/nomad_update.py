#!/usr/bin/env python

import os
import requests

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
        job = requests.get('%s/v1/job/%s' % (__NOMAD_URL__, __JOB_ID__),
                           headers={'X-Auth-Token': __AUTH_TOKEN__}).json()
        for taskgroup in job.get('TaskGroups'):
            for task in taskgroup.get('Tasks'):
                if task.get('Config').get('image').split(':')[0] == __IMAGE__:
                    task['Config']['image'] = "%s:%s" % (__IMAGE__, __TAG__)
                    updated = True
        if updated:
            update_request = requests.post('%s/v1/job/%s' % (__NOMAD_URL__, __JOB_ID__),
                                           headers={'X-Auth-Token': __AUTH_TOKEN__},
                                           json={ 'Job': job }
                                          )
            print("Request status: %s" % update_request.json())

main()
