FROM python:3.8.5-slim-buster
ADD postgres_test_iam.py /
RUN pip3 install psycopg2-binary boto3
CMD [ "python", "-u", "./postgres_test_iam.py" ]