FROM openapitools/openapi-generator-cli:latest

RUN apt-get update && apt-get install -y python3-pip && \
    pip3 install black

CMD ["generate"]