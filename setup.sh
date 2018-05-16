#!/bin/bash

function clonerepo() {
  git init
  git remote add origin "$1"
  git fetch
  git reset origin/master  # this is required if files in the non-empty directory are in the repo
  git branch -u origin/master
}

git -C . pull || clonerepo 'https://github.com/BAMLCodeJam/AIY-BofAML.git'
