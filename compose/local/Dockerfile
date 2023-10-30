FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential curl \
  # Translations dependencies
  && apt-get install -y gettext nodejs npm \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Add the PostgreSQL repository and install PostGIS
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    gnupg2 \
    && curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list' \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-12-postgis-3 \
        postgis

# Additionally, install the extension into the database
RUN apt-get install -y --no-install-recommends postgresql-12-postgis-3-scripts

# Switch to the 'postgres' user to enable extensions
USER postgres

# Initialize PostGIS extension
RUN /etc/init.d/postgresql start \
    && psql --command "CREATE EXTENSION postgis;" --dbname=postgres

# Exit from the 'postgres' user
USER root


RUN apt-get update && apt-get install -y gdal-bin libgdal-dev && apt-get install -y python3-gdal \
&& apt-get install -y binutils libproj-dev

# upgrade pip
RUN pip install --upgrade pip

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt


COPY ./compose/local/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app
