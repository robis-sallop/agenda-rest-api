# Agenda REST API (Python + Flask + MongoEngine)

This project provides a simple REST API to manage `recordatorios` stored in a local MongoDB database named `dbagenda`.

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

Ejecución

1. Asegúrate de tener MongoDB corriendo localmente y que exista la base `dbagenda`.
2. Si tu MongoDB requiere usuario/contraseña (en este proyecto usamos `admin:admin`), la URI por defecto es:

```
mongodb://admin:admin@localhost:27017/dbagenda
```

Puedes exportar la variable de entorno `MONGODB_URI` para cambiar la conexión.

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

Pruebas rápidas con `curl`:

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

Nota sobre `mongoose`:

La librería `mongoose` es un ODM de Node.js. Para Python hemos utilizado `mongoengine`, que ofrece una experiencia similar a `mongoose`. Si prefieres que implemente la API en Node.js usando `mongoose`, dime y lo cambio.
