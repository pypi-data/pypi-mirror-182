FROM openfaas/of-watchdog:0.8.2 as watchdog
FROM python:3.10-slim-bullseye

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

# Install package by build args
ARG ADDITIONAL_PACKAGE
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    ${ADDITIONAL_PACKAGE}
# TODO: musl-dev

# Add non root user
RUN useradd -ms /bin/bash app
RUN chown app /home/app

# Set workdir to app folder
USER app
WORKDIR /home/app/
ENV PATH=$PATH:/home/app/.local/bin

# Install template requirements
USER root
WORKDIR /home/app/
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt 

# Set workdir to app folder, copy deplyed function to workdir
WORKDIR /home/app/
COPY index.py .
COPY function function
RUN touch ./function/__init__.py

# Install function requirements
WORKDIR /home/app/function/
COPY function/requirements.txt  .
RUN pip install -r requirements.txt

# Clean everything
RUN rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove build-essential

# Set right permission
WORKDIR /home/app/
RUN chown -R app:app ./
USER app

# For serving
ENV fprocess="uvicorn index:app --workers 1 --host 0.0.0.0 --port 8000"
ENV cgi_headers="true"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:8000"
HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1

# Watchdog
CMD ["fwatchdog"]