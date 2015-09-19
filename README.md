# Stack-blog

## ¿Que es Stack-Blog?

Stack-blog es un sistema de foro open source desarrollado por [Open Nut](http://opennut.net) sobre Django 1.8 y (MongoDB o SqlLite).

## Develop (branch)

Para iniciar Stack-blog localmente, primero configuraremos y activaremos una maquina virtual para esto ejecuta los siguientes comandos:

```
virtualenv venv
```

Esto crear una carpeta la cual contiene la maquina virtual que utilizaremos para la ejecución de Stack-Blog.

```
source venv/bin/activate
```

Ya activada nuestra maquina virtual instalaremos las dependencias necesarias de Stack-Blog, con el siguiente comando:

```
pip install -r requirements.txt
```

Ahora cd y editar el archivo `"stackblog"` `"settings.py"` en tu editor de elección con el fin de establecer la configuración básica, como la conexión de base de datos, la zona horaria por defecto o idioma de la interfaz.

A continuación, inicializar la base de datos mediante el uso de comandos migrate proporcionados por la utilidad de administración manage.py:

```
cd stackblog
python manage.py migrate

```

Luego, llame ejecute el comando `"createsuperuser"` para crear súper admin en la base de datos:

```
python manage.py createsuperuser
```

Finalmente iniciar servidor de desarrollo mediante el comando `"runserver"`:

```
python manage.py runserver
```

Si no hay nada mal con su configuración, el servidor de desarrollador Django empezar, lo que le permite visitar `127.0.0.1:8000` en tu navegador y ver la (incompleta) Índice foro.




