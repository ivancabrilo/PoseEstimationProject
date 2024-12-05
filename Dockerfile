# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install system dependencies required by OpenCV and MediaPipe
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean

# Install Python dependencies
RUN pip install --no-cache-dir \
    opencv-python \
    mediapipe \
    json5

# Set the default command to run your main script
CMD ["python", "PoseEstimationMin.py"]
