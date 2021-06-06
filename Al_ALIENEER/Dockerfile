# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.5-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1



# Install pip requirements
RUN pip install --upgrade pip
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder: 'DJANGO_PROJECTS'. Please enter the Python path to wsgi file.

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "{AI_ALIENEER.AI_ALIENEER}.wsgi"]

CMD gunicorn --bind 0.0.0.0:8000 AI_ALIENEER.wsgi:application
