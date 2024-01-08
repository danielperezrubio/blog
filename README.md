# Full Stack React, FastAPI and PostgreSQL Blog

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Build

Docker compose will take care of everything, you must just define the environment variables

### Backend variables

#### Cors

- `BACKEND_CORS_ORIGINS`: List of origins that are enabled to connect with the backend.

#### Postgres database

Postgres database will be created by docker with this variables:

- `POSTGRES_USER`: Postgres username.
- `POSTGRES_PASSWORD`: Postgres password.
- `POSTGRES_DB`: Postgres database name.
- `POSTGRES_DB_TEST`: Postgres test database name, will be only used for tests.

#### Frontend

- `WEBSITE_URL`: The url for the frontend.

#### Admin

- `FIRST_SUPERUSER_USERNAME`: Admin username.
- `FIRST_SUPERUSER_EMAIL`: Admin email.
- `FIRST_SUPERUSER_PASSWORD`: Admin password.

#### Keys

- `JWT_SECRET_KEY`: JWT Secret Key.

#### Email

Your email account for the app:

- `MAIL_USERNAME`: Email address.
- `MAIL_PASSWORD`: Application-specific password generated on the email server.

The app uses google email configuration by default, but you can change it:

- `MAIL_PORT`: The port number for the email server (optional, default: 587).
- `MAIL_SERVER`: The server address for the email (optional, default: smtp.gmail.com).
- `MAIL_STARTTLS`: Enable or disable STARTTLS encryption (optional, default: True).
- `MAIL_SSL_TLS`: Enable or disable SSL/TLS encryption (optional, default: False).
- `USE_CREDENTIALS`: Enable or disable the use of credentials (optional, default: True).

### Frontend variables

- `VITE_API_URL`: Backend url
- `VITE_IMAGES_URL`: Url to load images

## Test

Run docker-compose specifying the _docker-compose.tests.yml_ file to test the API:

```bash
docker-compose -f docker-compose.tests.yml up
```

## Run

Run the app with docker-compose

```bash
docker-compose up -d
```
