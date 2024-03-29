FROM python:3.10.0-slim-buster as base

LABEL org.opencontainers.image.authors="Oleg Strokachuk <zifter.ai@gmail.com>"
LABEL org.opencontainers.image.version="0.1.0"
LABEL org.opencontainers.image.url="https://github.com/zifter/k8s-keda-autoscaling-example"
LABEL org.opencontainers.image.title="k8s-keda-autoscaling-example"
LABEL org.opencontainers.image.description="Kubernetes keda autoscaling example application"

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libc-dev

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .

# It's not okay to install dev packages, but now it will be allowed
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --dev --ignore-pipfile

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home appuser
USER appuser

WORKDIR /home/appuser

COPY --chown=appuser src src

WORKDIR /home/appuser/

EXPOSE 5000
