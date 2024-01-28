FROM ubuntu:22.04

# Install required dependencies, including unzip, curl, and alien
RUN apt-get update && \
    apt-get install -y libaio1 unzip curl && \
    rm -rf /var/lib/apt/lists/*

# Create the working directory in the container
WORKDIR /app

# Create the /app directory in the container
RUN mkdir -p /app

# Create the /opt/oracle/instantclient directory in the container
RUN mkdir -p /opt/oracle/instantclient

# Create the sources.list file
RUN touch /etc/apt/sources.list

# Copy the Oracle Instant Client files from the host to the container
COPY oracle-instantclient-basic-21.12.0.0.0-1.x86_64.rpm /opt/oracle/instantclient
COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py

# Convert Oracle Instant Client RPM to DEB
RUN apt-get install -y alien && \
    alien -i /opt/oracle/instantclient/oracle-instantclient-basic-21.12.0.0.0-1.x86_64.rpm && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set environment variables for Oracle Instant Client
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient:$LD_LIBRARY_PATH
ENV PATH=/opt/oracle/instantclient:$PATH

# Expose the port on which your application will run
EXPOSE 5020

# Specify the command to run on container start
CMD ["python3", "app.py"]

