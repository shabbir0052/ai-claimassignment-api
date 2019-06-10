FROM registry.access.redhat.com/rhel8/python-36:latest

# RUN mkdir -p /usr/src/app
WORKDIR /opt/app-root/

COPY requirements.txt /opt/app-root/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /opt/app-root

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "com_csaa_claims_ai_assignment"]
