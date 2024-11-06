# Use the official Rocky Linux 9 image as the base image
FROM docker.io/rockylinux:9

# Set the working directory
WORKDIR /app

# Copy the upload.server.py script into the container
COPY upload.server.py /app/

# Create the uploads directory
RUN mkdir -p /app/uploads

# Install Python and Flask
RUN dnf install -y python3 /usr/bin/pip && \
    python3 -m pip install flask

# Create a user with UID 1000
RUN useradd -u 1000 appuser

# Change ownership of the /app directory to the new user
RUN chown -R appuser:appuser /app

# Change permissions of the uploads directory
RUN chmod -R 755 /app/uploads

# Switch to the new user
USER appuser

# Expose the port that the server will run on
EXPOSE 8000

# Run the upload.server.py script
CMD ["python3", "upload.server.py"]
