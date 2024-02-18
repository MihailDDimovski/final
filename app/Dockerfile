# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Oracle Instant Client
ENV ORACLE_HOME=/usr/lib/oracle/21/client64
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib

# Install Oracle Instant Client and necessary dependencies
RUN apt-get update && apt-get install -y libaio1 curl wget && \
    mkdir -p /opt/oracle && \
    cd /opt/oracle && \
    curl -o oracle-instantclient.rpm https://yum.oracle.com/repo/OracleLinux/OL8/oracle/instantclient21/x86_64/getPackage/oracle-instantclient-basic-21.5.0.0.0-1.x86_64.rpm && \
    curl -o oracle-instantclient-devel.rpm https://yum.oracle.com/repo/OracleLinux/OL8/oracle/instantclient21/x86_64/getPackage/oracle-instantclient-devel-21.5.0.0.0-1.x86_64.rpm && \
    curl -o oracle-instantclient-sqlplus.rpm https://yum.oracle.com/repo/OracleLinux/OL8/oracle/instantclient21/x86_64/getPackage/oracle-instantclient-sqlplus-21.5.0.0.0-1.x86_64.rpm && \
    apt-get install -y alien && \
    alien -i oracle-instantclient.rpm && \
    alien -i oracle-instantclient-devel.rpm && \
    alien -i oracle-instantclient-sqlplus.rpm && \
    rm -rf /opt/oracle && \
    apt-get purge -y alien && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /flyway

# Set up Oracle Instant Client libraries
RUN echo "$ORACLE_HOME/lib" > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig

# Install Flask and cx_Oracle Python packages
RUN pip install --upgrade pip && \
    pip install flask cx_Oracle

# Copy the application code into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Set environment variables for Flyway
ENV FLYWAY_URL=jdbc:oracle:thin:@//192.168.1.2:1521/XEPDB1
ENV FLYWAY_ORACLE_WALLET_LOCATION=/flyway/ewallet.p12
ENV FLYWAY_USER=appuser
ENV FLYWAY_PASSWORD=123456
ENV FLYWAY_LOCATIONS=filesystem:/flyway/sql/

# Set environment variables for Python app
ENV PYTHON_USERNAME=appuser
ENV PYTHON_PASSWORD=123456
ENV PYTHON_CONNECTSTRING=192.168.1.2:1521/XEPDB1
# Download and install Flyway
RUN cd /flyway && \
    wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/7.15.0/flyway-commandline-7.15.0-linux-x64.tar.gz | tar -xvz && \
    ln -s /flyway/flyway-7.15.0/flyway /usr/local/bin/flyway

# Expose the Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
