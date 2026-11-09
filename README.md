# ParcelFlow

A courier and delivery management platform built with Django and Django REST Framework.

## Overview

ParcelFlow aims to streamline courier operations by providing a centralized platform for managing shipments, warehouse operations, courier assignments, delivery attempts, shipment tracking, and cash-on-delivery transactions.

The project is being developed as a modular monolith, with separate Django applications responsible for different business domains.

## Technology Stack

- Python 3.12
- Django
- Django REST Framework
- PostgreSQL
- Redis (planned)
- Celery and RabbitMQ (planned)
- Django Channels and WebSockets (planned)
- Elasticsearch (planned)

## Project Structure

- `apps/accounts/` - User accounts and authentication
- `apps/merchants/` - Merchant management
- `apps/couriers/` - Courier management
- `apps/warehouses/` - Warehouse operations
- `apps/shipments/` - Shipment management
- `apps/deliveries/` - Delivery assignments and attempts
- `apps/tracking/` - Shipment tracking
- `apps/finance/` - COD and financial operations
- `common/` - Shared utilities and components
- `config/` - Django project configuration

## Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/omarWael000/ParcelFlow.git
cd ParcelFlow
```

### 2. Create the virtual environment

```bash
uv python pin 3.12
uv venv
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and configure your local environment variables.

You also need a PostgreSQL server running locally and a database configured with the credentials specified in `.env`.

### 5. Apply migrations

```bash
uv run python manage.py migrate
```

### 6. Create a superuser

```bash
uv run python manage.py createsuperuser
```

### 7. Start the development server

```bash
uv run python manage.py runserver
```

## API Documentation

Once the server is running:

- Swagger UI: `/api/docs/`
- ReDoc: `/api/redoc/`
- OpenAPI Schema: `/api/schema/`

## Development Status

The project is under active development. Features will be documented as they are implemented.

## License

Not licensed for redistribution at this stage.