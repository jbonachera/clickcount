#!/bin/bash
job=${1}
tag=${2}
payload="{
	\"Job\": {
		\"ID\": \"$job\",
		\"TaskGroups\": [{
			\"Name\": \"clickcount\",
			\"Tasks\": [{
				\"Name\": \"front\",
				\"Config\": {
					\"image\": \"jbonachera/clickcount:$tag\"
				}
			}]
		}]
	}
}"
curl -H "X-Auth-Token: $NOMAD_AUTH_TOKEN" $NOMAD_URL/v1/job/clickcount -d "${payload}"
