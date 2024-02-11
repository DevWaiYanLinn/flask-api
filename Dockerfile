# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /code

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

ENV TF_ENABLE_ONEDNN_OPTS=0

# Copy the requirements file into the container at /code
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the current directory contents into the container at /code
COPY . .

# Make port 7860 available to the world outside this container
EXPOSE 7860

# Run uvicorn when the container launches
# CMD ["hypercorn", "app:asgi", "--bind", "127.0.0.1:7860"]
# CMD ["uvicorn", "app:asgi", "--host", "0.0.0.0", "--port", "7860"]
CMD ["gunicorn","-w", "4", "-b", "0.0.0.0:7860"]
