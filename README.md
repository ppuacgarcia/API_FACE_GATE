# API puerta con reconocimiento facial 
## PARA poder usar la api de primero es 
1. instalar el entorno virtual
```
pip install virtualenv
```
2. crear al entorno virtual
```
virtualenv [nombre del entorno]
ej. 
virtualenv venv
```

3. ingresar al entorno virtual
```
virutalenv venv
```

4. instalar requerimientos 
```
pip -r install requirements.txt
```

5. Hacer migraciones
```
python manage.py makemigrations
```
6. correr las migraciones
```
python manage.py  migrate
```
7. crear super usuario
```
python manage.py createsuperuser
```

8. corrrer servidor
```
python manage.py runserver
```


## para poder ver todos los datos guardados se puede entrar al /admin
```
http://127.0.0.1:8000/admin/
```
## Cliente de graphql que es como postman
```
http://127.0.0.1:8000/graphql/
``` 

## mutacion para autorizacion
```
mutation TokenAuth{
  tokenAuth(username:[usario de super user creado],
            password:[contraseña de superuser creado]){
    token
    payload
    refreshExpiresIn
		
  }
}
```

## mutacion de crear usuario 
notas:
1. solo tiene los campos necesarios y se pueden consultar mas datos 
2. el username no pueden tener 2 iguales
3. antes de empezar con la mutacion se tiene que encender la camara

```
mutation createUser{
  createUser(
    email:"pablo@pablo.com",
    firstName:"pablo",
    lastName:"puac",
    password:"admin",
    username:"pablo",
    videoPath:"./"
    isStaff:true
  ){
    user{
      id
      username
    }
  }
}
```

## query para reconocer caras
nota:
1. encender la camara antes de activar la mutacion 
```
query	recognition{
  recognize
}
```