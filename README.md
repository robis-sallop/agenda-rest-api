# Agenda REST API (Python + Flask + MongoEngine)

This project provides a simple REST API to manage `recordatorios` stored in a local MongoDB database named `dbagenda`.

## Cambios recientes

- Añadido endpoint de token: `POST /recordatorios/token` (expira en 60s).
- Validación de Authorization con `Bearer <token>` en todos los endpoints CRUD.
- Configuración centralizada en `config/settings.yaml` (con override por env vars).
- `requirements.txt` actualizado con `PyYAML` e `itsdangerous`.

Estructura creada:

- `app.py` - Punto de entrada de la aplicación
- `config/db.py` - Configuración/Conexión a MongoDB
- `models/reminder.py` - Modelo `Reminder` (colección `recordatorios`)
- `controllers/reminder_controller.py` - Lógica de negocio / CRUD
- `routes/reminder_routes.py` - Rutas REST (Blueprint)

Dependencias

Instalar dependencias:

```bash
pip install -r requirements.txt
```

### Nota PyYAML (Windows)

Si obtienes error al instalar PyYAML como:

- `ERROR: Failed to build 'PyYAML'`

Prueba estos pasos:

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install --only-binary :all: PyYAML
```

Si sigue fallando, instala las Visual Studio Build Tools (C/C++) o usa `conda install pyyaml`. También puedes cambiar a `ruamel.yaml` y modificar la carga YAML en `app.py`.


Ejecución

1. Asegúrate de tener MongoDB corriendo localmente y que exista la base `dbagenda`.
2. Si tu MongoDB requiere usuario/contraseña (en este proyecto usamos `admin:admin`), la URI por defecto es:

```
mongodb://admin:admin@localhost:27017/dbagenda
```

Puedes exportar la variable de entorno `MONGODB_URI` para cambiar la conexión.

$env:MONGODB_URI = 'mongodb://localhost:27017/dbagenda'

Archivo de configuración YAML:

- `config/settings.yaml`
  - `SECRET_KEY`
  - `TOKEN_EXPIRATION_SECONDS`
  - `MONGODB_URI`

Ejecutar la app:

```bash
python app.py
```

Endpoints (base `/recordatorios`):

- `POST /recordatorios/` - Crear recordatorio
  - Body JSON: `{ "title": "...", "detail": "...", "status": "pendiente|hecho" }`
- `GET /recordatorios/` - Listar todos
- `GET /recordatorios/<id>` - Detalle por ID
- `PUT /recordatorios/<id>` - Editar por ID (enviar campos a actualizar)
- `DELETE /recordatorios/<id>` - Eliminar por ID

Autorización

- Para usar los endpoints de `recordatorios`, primero genera un token:
  - `POST /recordatorios/token` (respuesta JSON `{ "token": "...", "expires_in": 60 }`)
- Todos los endpoints requiren header:
  - `Authorization: Bearer <token>`
- El token expira en 60 segundos (1 minuto).

Pruebas rápidas con `curl`:

Obtener token:
```bash
curl -X POST http://127.0.0.1:5000/recordatorios/token
```

Usar token en pruebas:
```bash
TOKEN=$(curl -s -X POST http://127.0.0.1:5000/recordatorios/token | jq -r '.token')
curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/recordatorios/ -d '{"title":"Comprar leche","detail":"Entera 1L"}'
```

```bash
curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/recordatorios/
```

```bash
curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/recordatorios/<id>
```

```bash
curl -X PUT -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" http://127.0.0.1:5000/recordatorios/<id> -d '{"status":"hecho"}'
```

```bash
curl -X DELETE -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/recordatorios/<id>
```

Crear:
```bash
curl -X POST http://127.0.0.1:5000/recordatorios/ -H "Content-Type: application/json" -d '{"title":"Comprar leche","detail":"Entera 1L"}'
```

Listar:
```bash
curl http://127.0.0.1:5000/recordatorios/
```

Detalle:
```bash
curl http://127.0.0.1:5000/recordatorios/<id>
```

Editar:
```bash
curl -X PUT http://127.0.0.1:5000/recordatorios/<id> -H "Content-Type: application/json" -d '{"status":"hecho"}'
```

Eliminar:
```bash
curl -X DELETE http://127.0.0.1:5000/recordatorios/<id>
```
