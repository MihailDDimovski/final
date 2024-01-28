FROM ubuntu:22.04

# Install required dependencies, including unzip, curl, and rpm
RUN apt-get update && \
    apt-get install -y libaio1 unzip curl rpm && \
    apt-get install -y rpm2cpio && \
    rm -rf /var/lib/apt/lists/*

# Create the working directory in the container
WORKDIR /app

# Create the /app directory in the container
RUN mkdir -p /app

# Create the /opt/oracle/instantclient directory in the container
RUN mkdir -p /opt/oracle/instantclient

# Copy the Oracle Instant Client files from the host to the container
COPY oracle-instantclient-basic-21.12.0.0.0-1.x86_64.rpm /opt/oracle/instantclient

# Extract the contents of the RPM package
RUN rpm2cpio /opt/oracle/instantclient/oracle-instantclient-basic-21.12.0.0.0-1.x86_64.rpm | cpio -idmv

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r /app/requirements.txt

# Set environment variables for Oracle Instant Client
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient:$LD_LIBRARY_PATH
ENV PATH=/opt/oracle/instantclient:$PATH

# Expose the port on which your application will run
EXPOSE 5020

# Copy the application files
COPY app.py /app/app.py

# Specify the command to run on container start
CMD ["python3", "app.py"]

