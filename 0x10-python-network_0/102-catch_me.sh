#!/bin/bash
#Script that makes a request to causes an specific response
curl -s -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
