# Absolute Control Command Line Interface

## Introduction
This is a command line interface for the Absolute Control python library.

## Usage
Inside of a python environment, you can import the library and use 
the command line interface.
```bash
pip install -r requirements.txt
python run.py
```

If you prefer to use docker, you can use the docker image.
```bash
docker build -t cli --target RUN .
docker run cli
```

## Testing
To test the library, you can use the `run_tests.py` script. It is highly recommended to use the docker image. These tests could shut down your system or cause harm to your system.

Using docker, you can run the tests.
```bash
docker build -t tests --target TEST .
docker run tests
```

You may still run the tests on your system, but you should not do this.
```bash
pip install pytest coverage
python run_tests.py
```

## License
This project is licensed under the MIT license.

## Contribution
This project is open source. You can contribute to the project by making a pull request or by sending an email to [Johnny Irvin](mailto:irvinjohnathan@gmail.com).