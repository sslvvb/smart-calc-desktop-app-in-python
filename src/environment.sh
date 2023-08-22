#!/bin/bash

if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
fi

if [ ! -f "requirements.txt" ]; then
    touch requirements.txt
    pip install tk
    pip install sympy
    pip freeze >> requirements.txt
  else
    pip install -r requirements.txt
    pip freeze
fi

pip install --upgrade pip
echo "For switch to environment use command: "
echo "source venv/bin/activate"
