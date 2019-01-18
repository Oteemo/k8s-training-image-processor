# k8s-training-image-processor

## Local Developer Setup

### Download the python3 binary

This project was developed using Python 3.7.1. Navigate to the following [link](https://www.python.org/downloads/release/python-371/) and download the python3 binary for your particular os.

**Note the location that you saved this binary too.**

### Virtualenv
```
$ cd k8s-training-image-processor
$ pip install virtualenv
$ virtualenv -p /path/to/you/python3/binary venv
$ source venv/bin/activate
```
Test that you're now using the correct python binary
```
$ python --version
```
### Install dependancies 
```
$ pip install -r requirements.txt
```

### Run the server
```
$ python app.py
```
### Run tests
```
$ python -m pytest
```
###
To exit the venv python environment you can run the following command:
```
$ deactivate
```
