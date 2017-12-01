from debian:stretch

# Install build tools
RUN apt-get update && apt-get install -y git make automake autopoint autoconf python3
RUN apt-get install -y python3-pip python-gi python-gi-cairo python3-gi python3-gi-cairo gir1.2-gtk-3.0 python-dbus python3-flake8

# TODO: python2.7 image
