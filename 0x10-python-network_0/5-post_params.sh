#!/bin/bash
#and displays the body of the response with a variables email and subject
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"
