# Base image
FROM python:3

# Make  a directory for our application
WORKDIR /home/docker-workshop/tareas/karlab/tarea2-2

# Install dependencies
RUN pip install pymongo

# Copy our source code 
COPY find.py .
COPY populate.py .

# Run de application
CMD [ "python", "./populate.py", "&&", "python", "./find.py" ]
