FROM oracle/instantclient:21

WORKDIR /app

# Create the app directory
RUN mkdir -p /app

# Copy the Oracle Database driver files to the container
COPY oracle-database-driver-files /usr/lib/oracle/21/client64/lib
COPY oracle-database-driver-headers /usr/include/oracle/21/client64/

# Set environment variables for Oracle Instant Client
#ENV LD_LIBRARY_PATH=/usr/lib/oracle/21/client64/lib:$LD_LIBRARY_PATH
# ENV PATH=/usr/lib/oracle/21/client64/lib:$PATH

# Copy the application files
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r /app/requirements.txt

# Expose the port on which your application will run (if applicable)
EXPOSE 5020

CMD ["python3", "app.py"]

