#!/bin/bash
USERNAME = $1
EMAIL = $2

git config --local user.username $USERNAME
git config --local user.email $EMAIL

echo 'configured user'
