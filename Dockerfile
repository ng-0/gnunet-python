from debian:stretch

# Install build tools
RUN apt-get update && apt-get install -y git make automake autopoint autoconf python3 python3-pip

RUN pip install dbus
RUN pip install PyGObject
# TODO: python2.7 image
