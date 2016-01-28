Debug = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stackblog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_UNIQUE_EMAIL = True

LOGIN_REDIRECT_URL = "home"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3
ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# EMAIL SETTINGS
EMAIL_HOST = ""
EMAIL_PORT = "587"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
# Controls whether a secure connection is used.
EMAIL_USE_TLS = True 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ACCOUNT_AUTHENTICATION_METHOD = ("username_email")

