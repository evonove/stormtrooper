from .base import *


# security enforcement
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = env('DJANGO_SECURE_SSL_REDIRECT', True)
SESSION_COOKIE_SECURE = env('DJANGO_SESSION_COOKIE_SECURE', True)

# uncomment for cross-domain cookies
# SESSION_COOKIE_DOMAIN = ".{}".format(env("DJANGO_ALLOWED_HOSTS"))

# emails
DEFAULT_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', EMAIL_BACKEND_DEFAULT)
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_HOST_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True

# logging
LOGGING['loggers'] = {
    'django': {
        'handlers': ['console', 'syslog'],
        'level': env('DJANGO_LOG_LEVEL', 'INFO'),
    },
    'runaway': {
        'handlers': ['logstash', 'syslog'],
        'level': env('{{ cookiecutter.app_name|upper }}_LOG_LEVEL', 'INFO'),
    },
}