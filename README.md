# BACKEND

## Configuración del Entorno

Para ejecutar correctamente este proyecto, es necesario configurar un archivo `.env` con las variables de entorno requeridas. A continuación se detalla cómo crear y configurar este archivo.

### Creación del archivo .env

Crea un archivo llamado `.env` en la raíz del proyecto con la siguiente estructura:

```
# LLAVES PARA LOS TOKENS
SECRET_KEY="tu-clave-privada-generada-con-openssl"
SECRET_KEY_LOCAL="tu-secret-key-temporal-para-desarrollo"

# CONFIGURACION DE KEYCLOAK
OIDC_OP_BASE_URL="https://tu-servidor-keycloak.com/realms/tu-realm/"
OIDC_RP_CLIENT_ID="tu-client-id"
OIDC_RP_CLIENT_SECRET="tu-client-secret"
LOGOUT_REDIRECT_URL="http://localhost:8000"
```

### Generación de Claves Seguras

#### Generar una clave privada para SECRET_KEY

Puedes generar una clave privada segura utilizando OpenSSL con el siguiente comando:

```
openssl genrsa -out private_key.pem 2048
```

Este comando generará un archivo `private_key.pem` con una clave RSA de 2048 bits. El contenido de este archivo (incluyendo las líneas de inicio y fin) debe copiarse como valor para la variable `SECRET_KEY` en el archivo `.env`.

#### Clave para desarrollo local

Para entornos de desarrollo, puedes utilizar una clave más simple. Puedes generar una cadena aleatoria con el siguiente comando:

```
openssl rand -base64 32
```

Este comando generará una cadena aleatoria de 32 bytes codificada en base64, que puedes usar como `SECRET_KEY_LOCAL`.

### Descripción de las Variables

#### Llaves para los Tokens

- **SECRET_KEY**: Clave privada utilizada para firmar los tokens JWT en producción. Esta clave debe mantenerse segura y no debe compartirse.
- **SECRET_KEY_LOCAL**: Clave simplificada para entornos de desarrollo local. Puedes personalizar este valor para tu entorno de desarrollo.

#### Configuración de Keycloak

- **OIDC_OP_BASE_URL**: URL base del proveedor de OpenID Connect (Keycloak). Esta URL apunta al realm específico de la aplicación.
- **OIDC_RP_CLIENT_ID**: Identificador del cliente en Keycloak. Este valor debe coincidir con el cliente configurado en el servidor Keycloak.
- **OIDC_RP_CLIENT_SECRET**: Secreto del cliente en Keycloak. Este valor es proporcionado por el servidor Keycloak al configurar el cliente.
- **LOGOUT_REDIRECT_URL**: URL a la que se redirigirá después de cerrar sesión. Para desarrollo local, normalmente es la URL del servidor local.

### Configuración Interna de OIDC

El proyecto utiliza la biblioteca `mozilla-django-oidc` para la integración con Keycloak. Las variables definidas en el archivo `.env` se utilizan para configurar automáticamente los siguientes parámetros en el archivo `settings.py`:

```python
# Estos valores se generan automáticamente a partir de OIDC_OP_BASE_URL
OIDC_OP_AUTHORIZATION_ENDPOINT = f'{OIDC_OP_BASE_URL}/protocol/openid-connect/auth'
OIDC_OP_TOKEN_ENDPOINT = f'{OIDC_OP_BASE_URL}/protocol/openid-connect/token'
OIDC_OP_USER_ENDPOINT = f'{OIDC_OP_BASE_URL}/protocol/openid-connect/userinfo'
OIDC_OP_JWKS_ENDPOINT = f'{OIDC_OP_BASE_URL}/protocol/openid-connect/certs'
```

## Configuración Inicial del Proyecto

1. Crea un entorno virtual de Python:
   ```
   python -m venv venv
   ```

2. Activa el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En macOS/Linux: `source venv/bin/activate`

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Instala la dependencia de mozilla-django-oidc (no incluida en requirements.txt):
   ```
   pip install mozilla-django-oidc
   ```

5. Crea y configura el archivo `.env` como se describió anteriormente.

6. Ejecuta las migraciones de la base de datos:
   ```
   python manage.py migrate
   ```

7. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

## Endpoints de Autenticación

El proyecto incluye los siguientes endpoints para la autenticación con Keycloak:

- **Iniciar autenticación**: `/oidc/authenticate/`
- **Callback de autenticación**: `/oidc/callback/`
- **Obtener token**: `/rest/v1/oidc/obtener-token/get-token/`
- **Información del usuario**: `/rest/v1/oidc/obtener-token/me/`

## Notas Importantes

- Las claves y secretos proporcionados en este ejemplo son solo para fines de demostración. En un entorno de producción, debes generar tus propias claves seguras.
- Nunca compartas tus claves privadas o secretos de cliente en repositorios públicos.
- Para entornos de producción, considera utilizar variables de entorno del sistema en lugar de un archivo `.env`.
- El proyecto está configurado para almacenar los tokens de acceso y ID en la sesión del usuario, lo que permite su uso en las solicitudes a la API.
- Se recomienda actualizar el archivo `requirements.txt` para incluir la dependencia `mozilla-django-oidc` y así facilitar la instalación del proyecto.