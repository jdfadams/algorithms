FROM python:3
ARG user=me
RUN useradd -ms /bin/bash $user
WORKDIR /home/$user/algorithms
COPY . .
