FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir \
    tensorflow \
    kivy \
    pillow \
    numpy

# Copy the current directory contents into the container at /app
COPY . /app

# Run the application
CMD ["python", "main2.py"]