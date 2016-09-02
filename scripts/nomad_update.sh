#!/bin/bash
tag=${1}
payload="{
	\"Job\": {
		\"ID\": \"clickcount\",
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
