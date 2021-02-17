FROM python:3.7-slim

RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt 
#Disable the cash using --no-cache-dir option to lower image size

#change user
USER app_user
COPY ./app .

#set BASH as default command
CMD ["bash"]

