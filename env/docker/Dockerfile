FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#The below command is executed at runtime by devcontainer.
#CMD ['/bin/bash', '-c', 'whecho Container started\ntrap \"exit 0\" 15\n\nexec \"$@\"\nwhile sleep 1 \u0026 wait $!; do :; done', '-']