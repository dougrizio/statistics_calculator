FROM python:3

ADD . .

RUN python -m pip install --user numpy scipy

CMD ["python", "-m", "unittest", "discover", "-s", "/Tests"]