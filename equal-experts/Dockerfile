FROM python:3.9.14-alpine

# Copy the python function into the container
COPY hello-world.py /

# Copy the third party package requirements file to the container
COPY requirements.txt /

# Install the required package
RUN pip install -r requirements.txt

# Expose the required port
EXPOSE 3000

# Default Entrypoint CMD for the container
CMD [ "python", "-u", "hello-world.py" ]
