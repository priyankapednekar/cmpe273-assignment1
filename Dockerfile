FROM python:2.7.13
MAINTAINER Your Name "priyankapednekar4@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","-u","app.py"]
#CMD ["app.py","arg1"]
