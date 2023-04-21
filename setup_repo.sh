#!/usr/bin/env bash
echo "# movies-api-exercise" >> README.md
git init
git remote add origin $1
# Sets the new remote
git remote -v
# Verifies the new remote URL
git pull
git add .
git commit -m "First commit !"
git push -u origin main
# Pushes the changes in your local repository up to the remote repository you specified as the origin
echo "git remote repo setup ready."
