# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8

ENV API_KEY=at_PQM31V7mHRXG8WeA6jjyVUY6CNl53

ADD main.py .

RUN pip install requests

CMD ["python", "./main.py"]
