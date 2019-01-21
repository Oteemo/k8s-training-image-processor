# k8s-training-image-processor

## Local Developer Setup

### Download the python3 binary

This project was developed using Python 3.7.1. Navigate to the following [link](https://www.python.org/downloads/release/python-371/) and download the python3 binary for your particular os.

**Note the location that you saved this binary too.**

### Virtualenv
```bash
$ cd k8s-training-image-processor
$ pip install virtualenv
$ virtualenv -p /path/to/you/python3/binary venv
$ source venv/bin/activate
```
Test that you're now using the correct python binary
```bash
$ python --version
```
### Install dependancies 
```bash
$ cd app
$ pip install -r requirements.txt
```

### Run the server
```bash
#from the k8s-traning-image-processor/app directory
$ python app.py
```
### Run tests
```bash
#from the k8s-traning-image-processor/app directory
$ python -m pytest
```
###
To exit the venv python environment you can run the following command:
```bash
$ deactivate
```
