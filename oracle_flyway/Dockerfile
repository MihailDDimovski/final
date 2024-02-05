# Use Oracle Database Express Edition as the base image
FROM container-registry.oracle.com/database/express:21.3.0-xe

# Install wget
USER root
RUN yum install -y wget

RUN mkdir /flyway

# Set the working directory
WORKDIR ./oracle-flyway

# Download and install Flyway
RUN wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/7.15.0/flyway-commandline-7.15.0-linux-x64.tar.gz | tar -xvz && \
    ln -s `pwd`/flyway-7.15.0/flyway /usr/local/bin
    
ENV FLYWAY_URL=jdbc:oracle:thin:@//localhost:1521/XEPDB1 \
    FLYWAY_ORACLE_WALLET_LOCATION=/flyway/ewallet.p12 \
    FLYWAY_LOCATIONS=filesystem:/flyway/sql/

# Copy Flyway configuration files into the container
COPY  ./ ./flyway
# Expose the default Oracle Database port
EXPOSE 1521


