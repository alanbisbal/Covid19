# Grupo 37

Yajaira Dajhan Quipusco Obeso 14206/9
Nicolas Pereyra 11350/3
Santiago Gabriel Cristobal 14413/4
Bisbal, Alan Nicolas 11652/5
.




# Consumo de api:

**Get de centros**
```
http://127.0.0.1:5000/api/centros
Retorna los centros habilitados.
```

```
http://127.0.0.1:5000/api/centros/19
Retorna un centro en particular por id
```

**Post de centro**

```
http://127.0.0.1:5000/api/centros

ejemplo de Postman
{
 "nombre": "Iglesia Sagrado Corazón de Jesús",
 "direccion": "Diagonal 73 nro 1032",
 "telefono": "221 - 5139019",
 "hora_apertura": "09:30",
 "hora_cierre": "18:00",
 "tipo": "Institución religiosa",
 "web": "",
 "email": "asdasd@asdasd.com",
 "latitud":"-34.9159",
 "longitud":"-57.9924",
 "municipio_id":"24"
}
```
