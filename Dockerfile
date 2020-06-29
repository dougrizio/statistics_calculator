FROM python:3

ADD Tests /tests

CMD [ "python", "./tests/CalculatorTests.py"]