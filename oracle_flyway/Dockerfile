# Use Oracle Database Express Edition as the base image
FROM container-registry.oracle.com/database/express:21.3.0-xe

# Install wget
USER root
RUN yum install -y wget

# Set the working directory to /opt
WORKDIR /opt

# Download and install Flyway
RUN wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/7.15.0/flyway-commandline-7.15.0-linux-x64.tar.gz | tar -xvz && \
    ln -s `pwd`/flyway-7.15.0/flyway /usr/local/bin

# Copy Flyway configuration files into the container
COPY flyway.conf /opt/flyway-7.15.0/conf/flyway.conf
COPY migrations /opt/flyway-7.15.0/sql/

# Set environment variables for Flyway
ENV FLYWAY_URL=jdbc:oracle:thin:@//localhost:1521/XEPDB1 \
    FLYWAY_USER=appuser \
    FLYWAY_PASSWORD=123456 \
    FLYWAY_LOCATIONS=filesystem:/opt/flyway-7.15.0/sql/

# Expose the default Oracle Database port
EXPOSE 1521

# CMD to start Oracle Database and run Flyway migrations
CMD ["bash", "-c", "/etc/init.d/oracledb-xe configure && source /home/oracle/.bashrc && /opt/flyway-7.15.0/flyway migrate"]

