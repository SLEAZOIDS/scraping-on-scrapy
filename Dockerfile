FROM ubuntu

# Install.
RUN \
  apt-get update && \
  apt-get install -y python3 python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev && \
  pip3 install scrapy && \
  pip3 install pymongo && \
  pip3 install pulp && \
  pip3 install numpy
# Set environment variables.
ENV LANG ja_JP.UTF-8
ENV PYTHONIOENCODIND utf_8

# Define default command.
# CMD ["bin/bash"]
