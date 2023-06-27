#!/bin/bash
# Displays all HTTPS methods the server of a given URL will accept
curl -SI "$1" | grep "Allow" | cut -d " " -f 2-
