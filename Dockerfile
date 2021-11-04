FROM python:3.9 as RUN
WORKDIR /code

COPY run.py requirements.txt /code/
COPY src/ /code/src/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENTRYPOINT ["./run.py"]

FROM python:3.9 as TEST
WORKDIR /code

COPY run.py run_tests.py requirements.txt /code/
COPY src/ /code/src/
COPY tests/ /code/tests/

RUN pip install pytest coverage ; pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENTRYPOINT ["./run_tests.py"]