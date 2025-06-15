# Django REST Framework with Keycloak OIDC Integration

A Django REST Framework (DRF) backend application that integrates with Keycloak for authentication and authorization using OpenID Connect (OIDC) protocol.

## Overview

This project provides a complete authentication solution for Django applications using Keycloak as the identity provider. It supports both traditional Django session authentication and DRF token-based authentication, enabling single sign-on (SSO) capabilities across multiple applications.

## Features

- **Keycloak Integration**: Full integration with Keycloak using OpenID Connect protocol
- **Dual Authentication**: Support for both Django session authentication and DRF token authentication
- **JWT Token Management**: Secure token handling with automatic validation
- **User Management**: Automatic user creation and synchronization with Keycloak user data
- **Group Management**: Dynamic group membership based on Keycloak roles and groups
- **Session Management**: Secure session handling with logout functionality
- **Development-Ready**: Easy setup for local development environments

## Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Django REST Framework 3.12 or higher
- Access to a Keycloak server (local or remote)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/NexosoftDev/drf_oidc_connect.git
cd drf_oidc_connect
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

# Install the OIDC authentication library
pip install mozilla-django-oidc
```

### 4. Environment Configuration

Create a `.env` file in the project root with the following configuration:

```env
# JWT Token Keys
SECRET_KEY="your-private-key-generated-with-openssl"
SECRET_KEY_LOCAL="your-temporary-secret-key-for-development"

# Keycloak OIDC Configuration
OIDC_OP_BASE_URL="https://your-keycloak-server.com/realms/your-realm/"
OIDC_RP_CLIENT_ID="your-client-id"
OIDC_RP_CLIENT_SECRET="your-client-secret"
LOGOUT_REDIRECT_URL="http://localhost:8000"

# Optional: Additional OIDC Settings
OIDC_VERIFY_SSL=True
OIDC_USE_NONCE=True
OIDC_CREATE_USER=True
```

### 5. Generate Secure Keys

#### Production Key (SECRET_KEY)
Generate a secure RSA private key for production:

```bash
openssl genrsa -out private_key.pem 2048
```

Copy the entire content of `private_key.pem` (including header and footer) as the value for `SECRET_KEY`.

#### Development Key (SECRET_KEY_LOCAL)
Generate a simple base64 key for development:

```bash
openssl rand -base64 32
```

Use the output as the value for `SECRET_KEY_LOCAL`.

### 6. Database Setup

```bash
python manage.py migrate
```

### 7. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Keycloak Configuration

### Client Setup

1. **Access Keycloak Admin Console**
   - Navigate to your Keycloak admin interface
   - Select your realm

2. **Create OIDC Client**
   - Go to Clients → Create Client
   - Set Client type to "OpenID Connect"
   - Configure the following settings:
     - Client ID: `your-client-id`
     - Client authentication: ON
     - Authorization: ON (if using fine-grained permissions)

3. **Configure Client Settings**
   - **Valid redirect URIs**: `http://localhost:8000/oidc/callback/`
   - **Valid post logout redirect URIs**: `http://localhost:8000/`
   - **Web origins**: `http://localhost:8000`

4. **Client Credentials**
   - Navigate to the Credentials tab
   - Copy the Client Secret for use in your `.env` file

### Realm Configuration

Ensure your Keycloak realm has:
- Users with appropriate roles
- Groups configured (if using group-based permissions)
- Client scopes properly configured for OpenID Connect

## Environment Variables Reference

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `SECRET_KEY` | RSA private key for JWT signing (production) | Yes | `-----BEGIN RSA PRIVATE KEY-----\n...` |
| `SECRET_KEY_LOCAL` | Base64 key for development | Yes | `abc123def456...` |
| `OIDC_OP_BASE_URL` | Keycloak realm base URL | Yes | `https://keycloak.example.com/realms/myapp/` |
| `OIDC_RP_CLIENT_ID` | Keycloak client identifier | Yes | `django-app` |
| `OIDC_RP_CLIENT_SECRET` | Keycloak client secret | Yes | `your-client-secret` |
| `LOGOUT_REDIRECT_URL` | Post-logout redirect URL | Yes | `http://localhost:8000` |
| `OIDC_VERIFY_SSL` | Enable SSL verification | No | `True` (default) |
| `OIDC_USE_NONCE` | Use nonce for security | No | `True` (default) |
| `OIDC_CREATE_USER` | Auto-create users on login | No | `True` (default) |

## API Endpoints

### Authentication Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/oidc/authenticate/` | GET | Initiate OIDC authentication flow |
| `/oidc/callback/` | GET/POST | OIDC callback handler |
| `/oidc/logout/` | GET/POST | Logout and end OIDC session |

### API Endpoints

| Endpoint | Method | Description | Authentication |
|----------|--------|-------------|----------------|
| `/rest/v1/oidc/obtener-token/get-token/` | POST | Obtain JWT access token | Session |
| `/rest/v1/oidc/obtener-token/me/` | GET | Get current user information | Token |

## Usage Examples

### Frontend Integration

```javascript
// Redirect to authentication
window.location.href = '/oidc/authenticate/';

// Get user token (after authentication)
fetch('/rest/v1/oidc/obtener-token/get-token/', {
    method: 'POST',
    credentials: 'include',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
    }
})
.then(response => response.json())
.then(data => {
    const token = data.access_token;
    // Use token for subsequent API calls
});
```

### API Authentication

```javascript
// Using the JWT token for API requests
fetch('/api/protected-endpoint/', {
    headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
    }
})
.then(response => response.json())
.then(data => console.log(data));
```

## OIDC Endpoints Configuration

The system automatically configures the following OIDC endpoints based on your `OIDC_OP_BASE_URL`:

```python
OIDC_OP_AUTHORIZATION_ENDPOINT = f'{OIDC_OP_BASE_URL}/protocol/openid-connect/auth'
OIDC_OP_TOKEN_ENDPOINT = f'{OIDC_OP_BASE_URL}/protocol/openid-connect/token'
OIDC_OP_USER_ENDPOINT = f'{OIDC_OP_BASE_URL}/protocol/openid-connect/userinfo'
OIDC_OP_JWKS_ENDPOINT = f'{OIDC_OP_BASE_URL}/protocol/openid-connect/certs'
```

## Development vs Production

### Development Environment
- Use `SECRET_KEY_LOCAL` for simpler key management
- Set `OIDC_VERIFY_SSL=False` if using self-signed certificates
- Use localhost URLs for redirect URIs

### Production Environment
- Always use a secure `SECRET_KEY` generated with OpenSSL
- Enable SSL verification (`OIDC_VERIFY_SSL=True`)
- Use system environment variables instead of `.env` files
- Configure proper HTTPS redirect URIs
- Implement proper logging and monitoring

## Troubleshooting

### Common Issues

1. **Authentication Failed**
   - Verify Keycloak client configuration
   - Check redirect URIs match exactly
   - Ensure client secret is correct

2. **SSL Certificate Errors**
   - For development: set `OIDC_VERIFY_SSL=False`
   - For production: ensure valid SSL certificates

3. **Token Validation Errors**
   - Verify JWKS endpoint is accessible
   - Check token expiration settings
   - Ensure proper key configuration

### Debugging

Enable Django debug mode and check logs for detailed error information:

```python
# settings.py
DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'mozilla_django_oidc': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

## Security Considerations

- **Never commit secrets**: Keep `.env` files out of version control
- **Use HTTPS**: Always use HTTPS in production environments
- **Token Security**: Implement proper token storage and rotation
- **Regular Updates**: Keep dependencies updated for security patches
- **Access Control**: Implement proper role-based access control

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions:
- Check the [Issues](https://github.com/NexosoftDev/drf_oidc_connect/issues) section
- Review Keycloak and Django OIDC documentation
- Contact the development team

## License

This project is licensed under the MIT License - see the LICENSE file for details.