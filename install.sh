#!/bin/bash

REQUIRED_COMMANDS="pip3 python3"

for COMMAND in ${REQUIRED_COMMANDS}; do
    type ${COMMAND} &> /dev/null || { echo "command not found => ${COMMAND}"; exit 1; }
done

echo "Installing dependencies"
sudo pip3 install -r requirements.txt

echo "alias text-my-message=\"python3 $PWD/code/main.py\"" >> ~/.bashrc

echo "Execute => source ~/.bashrc or restart your terminal"