# MongoDB CRUD Server

A REST API server for managing documents in MongoDB with full CRUD operations.

## Overview

This project provides a FastAPI-based web service that allows you to perform Create, Read, Update, and Delete operations on documents stored in MongoDB. The API is designed to manage soldier/personnel records with fields like first name, last name, phone number, and rank.

## Features

- RESTful API endpoints for document management
- MongoDB integration for data persistence
- Docker containerization support
- OpenShift deployment configuration
- Input validation using Pydantic models
- Automatic API documentation with FastAPI

## Requirements

- Python 3.12+
- MongoDB database
- Docker (optional, for containerization)

## Installation

1. Clone the repository:
```
git clone <repository-url>
cd Mongodb-Crud-Server
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Configure MongoDB connection in `services/config.py`

4. Run the application:
```
uvicorn services.api:app --host 0.0.0.0 --port 8000
```

## Docker Usage

Build and run the Docker container:

```
docker build -t mongodb-crud-server .
docker run -p 8000:8000 mongodb-crud-server
```

## API Endpoints

- `POST /documents/` - Create a new document
- `GET /documents/{id}` - Retrieve a document by ID
- `PUT /documents/{id}` - Update an existing document
- `DELETE /documents/{id}` - Delete a document
- `GET /documents/` - List all documents

## OpenShift Deployment

Deployment configurations are available in the `infrastructure/` directory:

- `api-deployment.yaml` - API service deployment
- `mongo-deployment.yaml` - MongoDB deployment

## Project Structure

```
├── services/
│   ├── api.py              # FastAPI application
│   ├── config.py           # Configuration settings
│   ├── connection_dal.py   # Database connection
│   ├── dal.py              # Data Access Layer
│   └── solider_entity.py   # Document entity model
├── infrastructure/         # OpenShift deployment files
├── scripts/               # Utility scripts
├── Dockerfile             # Docker configuration
└── requirements.txt       # Python dependencies
```

## Development

The application uses FastAPI which provides automatic interactive API documentation. Once running, visit:

- API Documentation: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc