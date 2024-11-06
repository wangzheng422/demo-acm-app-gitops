# Use the official Rocky Linux 9 image as the base image
FROM docker.io/rockylinux:9

# Set the working directory
WORKDIR /app

# Copy the upload.server.py script into the container
COPY upload.server.py /app/

# Create the uploads directory
RUN mkdir -p /app/uploads

# Install Python
RUN dnf install -y python3

# Expose the port that the server will run on
EXPOSE 8000

# Run the upload.server.py script
CMD ["python3", "upload.server.py"]
