FROM alpine:3.6
ENV PORT 8080
EXPOSE ${PORT}
WORKDIR /usr/src/app

COPY ./Pipfile .

RUN pip3 install pipenv

COPY ./app .
RUN pipenv install

COPY start.sh .

CMD ["bash", "start.sh"]