# The bids/ndmg Docker container enables users to run end-to-end connectome estimation on structural MRI right from container launch
# https://hub.docker.com/r/bids/ndmg/
FROM bids/ndmg:v0.0.48-1
LABEL maintainer="francescacoo@gmail.com"

USER root

RUN pip install setuptools==36.4.0
RUN apt-get -y install python2.7 python-pip python-dev
RUN pip install --upgrade pip
RUN pip install jupyter

# needed to run notebook server - http://minrk-notebook.readthedocs.io/en/latest/public_server.html
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

RUN useradd -m -s /bin/bash brainhacker
WORKDIR /home/brainhacker/
USER brainhacker

EXPOSE 8888
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]
