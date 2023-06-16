FROM python:3-alpine

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "flask", "--debug", "run","--host","0.0.0.0","--port","5000"]


#FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
#RUN apk --update add bash nano
#ENV STATIC_URL .
#ENV STATIC_PATH .
#COPY ./requirements.txt ./requirements.txt
#RUN pip install -r ./requirements.txt