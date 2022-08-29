#!/bin/bash

# check if virtual env already exists
if [ -d env ]; then
    echo "Virtual env already exists"
else {
    #
    # unable to install psutil package in a virtual
    # environment in MacOS
    #
    if [[ "$OSTYPE" == "darwin"* ]]; then {
        python3 -m pip install psutil
        python3 -m venv env --system-site-packages
    }
    else {
        python3 -m venv env
    }
    fi
}
fi
# activate virtual env

source env/bin/activate

psu=$(python3 -m pip list --disable-pip-version-check | grep psutil)
if echo $psu | grep -q "psutil"
    then echo "requirement satisfied"
else
    python3 -m pip install -r requirements.txt
fi

# ${arg} - argument provided while initializing
# a build from jenkins
opts=${arg}
echo "provided option: ${opts}"
python3 src/__init__.py $(opts)

