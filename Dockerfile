from debian:stretch

# Install build tools
RUN apt-get update && apt-get install -y git make automake autopoint autoconf python3

# TODO: python2.7 image
