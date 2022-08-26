#!/bin/bash
USERNAME = $1
EMAIL = $2

git config user.username $USERNAME
git config user.email $EMAIL

git init
git add .
git commit -m "initial commit"
git branch -M main
