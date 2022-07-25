#!/usr/bin/env bash
tmux kill-server
cd ~/Documents/Github/project-code-monkeys
git fetch && git reset origin/main --hard

python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new -d -s cur-session 'flask run --host=0.0.0.0'
tmux send-keys 'exec redeploy-site.sh' C-m
tmux detach -s cur-session
