FROM python:3
ADD status.py /
CMD [ "python", "./status.py" ]
