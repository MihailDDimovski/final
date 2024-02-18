# Use Oracle Database Express Edition as the base image
FROM container-registry.oracle.com/database/express:21.3.0-xe

# Install wget
USER root
RUN yum install -y wget

RUN mkdir /flyway

# Set the working directory
WORKDIR /flyway

# Copy the pre-downloaded Flyway archive into the container
COPY flyway-commandline-7.15.0-linux-x64.tar.gz .

# Expose the default Oracle Database port
EXPOSE 1521


