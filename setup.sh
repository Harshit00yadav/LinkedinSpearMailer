#!/bin/bash

# making virtual environment
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
playwright install

deactivate

echo "setup complete"
