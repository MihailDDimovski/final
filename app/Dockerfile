FROM ubuntu:22.04

RUN apt-get update \
      && apt-get install -y --no-install-recommends \
       python3 \
       python3-pip \
      && apt-get install -y curl \
      && mkdir -p /app \
      && useradd -d /app -s /bin/bash app \
      && chown -R app:app /app


# Set the working directory in the container
WORKDIR /app

# Create the /app directory in the container
RUN mkdir -p /app
RUN mkdir -p /opt/oracle/instantclient

# Create the sources.list file
RUN touch /etc/apt/sources.list

# Copy the Oracle Instant Client files from the host to the container
COPY oracle-instantclient-basic-21.12.0.0.0-1.x86_64.rpm /opt/oracle/instantclient
COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py

# Install required dependencies, including unzip, curl, and rpm
RUN apt-get update && \
    apt-get install -y libaio1 unzip curl rpm && \
    rm -rf /var/lib/apt/lists/*

# Install Oracle Instant Client
RUN rpm -ivh /opt/oracle/instantclient/oracle-instantclient-basic-21.12.0.0.0-1.x86_64.rpm

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set environment variables for Oracle Instant Client
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient:$LD_LIBRARY_PATH
ENV PATH=/opt/oracle/instantclient:$PATH

# Expose the port on which your application will run
EXPOSE 5020

# Specify the command to run on container start
CMD ["python3", "app.py"]

