DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stackblog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.opennut.net'
EMAIL_PORT=587
EMAIL_HOST_USER='mario.solis'
EMAIL_HOST_PASSWORD='premier123'
EMAIL_USE_TLS=True