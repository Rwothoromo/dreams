# Dreams

[![CircleCI](https://circleci.com/gh/Rwothoromo/dreams.svg?style=svg)](https://circleci.com/gh/Rwothoromo/dreams)
[![Open Source Helpers](https://www.codetriage.com/rwothoromo/dreams/badges/users.svg)](https://www.codetriage.com/rwothoromo/dreams)

A demo bucket list on Dreams

## Getting Started

This is an open source project and all contributions are welcome.

In order to set up this repository in your local machine simply use the fork option available at the top right corner of this page.

### Prerequisites

You will need to have [python and pip installed](https://www.python.org/downloads/) locally to run this project.

### Running the app

Once you have cloned this repository to your local machine, run the following commands from the root of your cloned repository.

Install virtual environment:

```bash
#!/bin/bash
pip install virtualenv
```

Create a virtual environment (Mac OS):

```bash
#!/bin/bash
virtualenv ../dreams-venv --python=python3
```

Activate the virtual environment (Mac OS):

```bash
#!/bin/bash
source ../dreams-venv/bin/activate
```

To make sure you have all the required packages please run:


```bash
#!/bin/bash
pip install -r requirements.txt
```
For Windows:

```bash
set FLASK_APP= app.py
```

For MacOS:

```bash
export FLASK_APP= app.py
```

Next commands are common for all three platforms(i.e. Windows, MacOS and Linux):

```bash
flask db init

flask db migrate -m "Any message of your choice"

flask db upgrade
```


To run the app just execute one of following commands: Either:

```bash
python3 app.py
```
or:

```bash
flask run
```
This should initiate a flask web app running on port 8080 on your local host.

## Contributing

This is an open source project welcoming all contributions (See [CONTRIBUTING.md](./CONTRIBUTING.md)).

Feel free to make a PR for any enhancements or check out the issues page for suggested fixes.

For those who wish to have their name included in the contributors list please also add your name to the list as part of your PR in the same format as the other contributors.

## Contributors

See [Contributors.md](./Contributors.md).
