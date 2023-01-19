#!/bin/bash -eu
PROJECT_NAME=$(basename $(git config --local remote.origin.url) |sed "s/\.git$//")
find . -name .git -prune -o -exec sed -i.bk "s/oauth_reminder/${PROJECT_NAME}/g" {} \;
find . -name '*.bk' -exec rm {} \;
mv oauth_reminder ${PROJECT_NAME}
git add .
git ci -am "Convert oauth_reminder to ${PROJECT_NAME}"
