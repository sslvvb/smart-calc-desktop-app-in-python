#!/bin/bash

VENV_NAME=venv

if [ ! -d "$VENV_NAME" ]; then
    python3 -m venv $VENV_NAME
fi

source $VENV_NAME/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

echo "For switch to environment use command: "
echo "source venv/bin/activate"
