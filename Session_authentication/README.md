# Session Authentication

This project implements session-based authentication for the API, building upon the Basic Authentication project.

## Features

- Basic Authentication support
- User endpoint access via authentication
- Special `/users/me` endpoint to retrieve the authenticated user
- User CRUD operations with proper authorization

## Endpoints

- `GET /api/v1/status` - Check API status
- `GET /api/v1/users` - Retrieve all users (requires authentication)
- `POST /api/v1/users` - Create a new user (requires authentication)
- `GET /api/v1/users/<user_id>` - Retrieve a specific user (requires authentication)
- `GET /api/v1/users/me` - Retrieve the authenticated user (requires authentication)
- `PUT /api/v1/users/<user_id>` - Update a user (requires authentication)
- `DELETE /api/v1/users/<user_id>` - Delete a user (requires authentication)

## Requirements

### Python Scripts
- All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the pycodestyle style (version 2.6)
- All files are executable
- All modules have documentation
- All classes have documentation
- All functions (inside and outside a class) have documentation

## Setup

1. Install dependencies:
```bash
pip3 install -r requirements.txt
```

2. Run the API:
```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
```

## Usage Example

Create a test user:
```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py
```

Test the `/users/me` endpoint:
```bash
curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
```

## Author

Holberton School Project
