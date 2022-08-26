#!/bin/bash

# check if virtual env already exists
if [ -d env ]; then
    echo "Virtual env already exists"

# python compatibility fix on machines
else {
    python3 -m venv env
} || {
    python -m venv env
}
fi
# activate virtual env

source env/bin/activate

psu=$(pip list | grep psutil)
if echo $psu | grep -q "psutil"
    then echo "requirement satisfied"
else
    pip install -r requirements.txt
fi

echo "Running Script"
python3 src/__init__.py ${arg}

deactivate