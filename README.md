# Django_Discord_Bot

## 1- Clonar proyecto

```shell
git clone https://github.com/everyzzz/Django_Discord_Bot.git
```

## 2- Crear entorno virtual

```shell
virtualenv venv
```

## 3- Activar entorno virtual

```shell
Windows
./venv/Scripts/activate

Linux / Mac
source venv/bin/activate
```

## 4- Instalar dependencias

```shell
pip install -r requirements.txt
```

## 5- Debes reemplazar "BOT_TOKEN" por el token que se te generó del bot en Discord Dev.

## 6- Añadir tu bot a tu canal de discord
En Discord Dev. en la sección de OAuth2 en la parte de URL Generator indicar la opción: 
- [x] bot 

Y abrir el enlace que te genera.

## 7- En la sección de BOT en Discord Dev. en la parte de "Privileged Gateway Intents" habilitar las 3 opciones.

## 8- Ejecutar proyecto

```bash
python manage.py
```


## Documentación de librería discord.py
https://discordpy.readthedocs.io/en/stable/
