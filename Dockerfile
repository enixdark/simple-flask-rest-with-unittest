FROM pypy:2-onbuild

RUN mkdir -p /usr/local/account-service

WORKDIR /usr/local/account-service

COPY . /usr/local/account-service

EXPOSE 8000
RUN pip install -U pip
RUN pip install -r requirements.txt


ENTRYPOINT ["/bin/bash" , "run.sh"]
