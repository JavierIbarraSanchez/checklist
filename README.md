# checklist

Para poder realizar correctamente la aplicacion:

#configuracion aplicacion 
``` bash 
# 1) Crear entormo virtual fuera de la carpeta checklist

python -m venv env

2) Activar entorno virtual

env\Scripts\activate

3) instalar requerimientos nesesarios

pip install -r requirements.txt

```

Comandos:

## Iniciar api
python manage.py runserver

## Crear superuser
python manage.py createsuperuser

## Migraciones 
python manage.py makemigrations

python manage.py migrate

