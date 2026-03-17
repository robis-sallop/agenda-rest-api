# Prompt Utilizados para crear este proyecto


## Creacion del Backend del proyecto

### Requisitos previos

-Instalar Python

```
Crea una API creada en Pyhon. 
Esta API Rest debe conectarse a una base de datos
MongoDB creada localmente llamada dbagenda, usando una
colección llamada recordatorios; el usuario para la conexión es admin
y la contraseña es admin. Para la conexión a la base de datos
se debe usar la librería mongoose.
La API Rest debe permitir gestionar recordatorios, por lo cual debe
considerar cinco operaciones: crear un recordatorio, mostrar el
listado de recordatorios, editar un recordatorio por su ID, eliminar un recordatorio
usando su ID, y mostrar el detalle de un recordatorio de acuerdo a su
ID. Cada recordatorio debe tener un título, un detalle, la fecha de
creación y el estado actual.
Se debe considerar que en este proyecto las capas deben
estar separadas. Esto implica que debe existir un directorio
para los controladores, otro para los modelos y un directorio
para las rutas. El archivo de configuración de la base de datos
debe estar asimismo en un directorio independiente.
Finalmente, una vez que se haya creado el proyecto, es
necesario saber los pasos que se deben realizar para que la
API Rest se pueda probar.
```

## Creacion del Frontend del proyecto

### Requisitos previos

-Instalar VUE

```
node --version
npm install -g @vue/cli
vue --version
```


```
Crea una aplicación frontend Vue en la versión 3, que permita
gestionar tareas. Esta aplicación debe conectarse a una API
Rest a la cual se puede acceder por medio de la ruta
http://localhost:3000/api/tareas.
Cada tarea tiene cuatro atributos: “titulo” que corresponde al
título de la tarea, “detalle” que corresponde a la descripción
que se realiza sobre la tarea en cuestión, el atributo
“fechaCreacion” que representa la fecha y hora en la que se
crea la tarea (por defecto es la fecha y hora en que se realiza la
acción), y un atributo llamado “estado”, que muestra el estado
actual de la tarea, y que tiene como valores posibles
“pendiente”, “en progreso” y “completada”.
Este proyecto Vue debe considerar tres páginas principales:
- Una página de inicio que muestre el detalle del proyecto
- Una página que muestre el listado de las tareas, cada tarea
debe tener un enlace para editar la tarea, un enlace para ver el
detalle de la tarea o bien eliminarla, y cada enlace debe realizar la acción esperada.
- Una página para crear una tarea.
Cada página del proyecto debe ser independiente entre si, y se
debe acceder a ellas por medio de un menú. Es necesario
considerar un diseño atractivo que sea común para todas las
páginas del sitio.
Se pide además que los componentes, composables, helpers,
rutas y vistas estén separados en directorios independientes
como capas lógicas del proyecto.
Por último, se pide conocer los pasos necesarios para ejecutar
el proyecto y probarlo desde un navegador.
Crea una aplicación frontend en Vue 3 que permita gestionar
tareas. Por el momento, se necesita que el aplicativo tenga
solo una página de inicio que indique de qué trata el aplicativo
que se está construyendo.
```

```
Agrega un componente que permita crear una tarea. Cada
tarea tiene cuatro atributos: “titulo” que corresponde al título
de la tarea, “detalle” que corresponde a la descripción que se
realiza sobre la tarea en cuestión, el atributo “fechaCreacion”
que representa la fecha y hora en la que se crea la tarea (por
defecto es la fecha y hora en que se realiza la acción), y un
atributo llamado “estado”, que muestra el estado actual de la
tarea, y que tiene como valores posibles “pendiente”, “en
progreso” y “completada”.
El componente debe tener un formulario con campo adecuado
para cada atributo de las tareas. Para crear la tarea, el
formulario se debe conectar con la ruta http://localhost:3000/api/tareas.
Por último, es importante destacar que esta acción debe estar
creada usando Composition API, además debe existir una ruta
en el proyecto que permita acceder a este componente recién
creado.
```

Si arroja un error de ruteo, se puede deber a que no está instalada en el
proyecto la dependencia de vue-router. Para hacerlo ejecuta el siguiente
comando:

```
npm install vue-router

npm install axios
```

* Solucionar error CORS

```
Al conectar un frontend creado en Vue 3 a este proyecto
backend, se retorna un error de CORS: “Access to fetch at
'http://localhost:3000/api/tareas' from origin
'http://localhost:5173' has been blocked by CORS policy:
Response to preflight request doesn't pass access control
check: No 'Access-Control-Allow-Origin' header is present on
the requested resource.”. ¿De qué manera se puede
solucionar?
```

```
npm install cors
```

```
Crea un componente en el proyecto actual que permita mostrar
un listado de tareas. Este componente debe mostrar el título de
la tarea, un extracto del detalle, la fecha de creación y el
estado actual. Además, debe contener un ícono alusivo que
lleve a una acción para editar una tarea, un ícono que permita
eliminar una tarea y otro ícono que permita desplegar el detalle
de la tarea. Cada tarea tiene cuatro atributos: “titulo” que
corresponde al título de la tarea, “detalle” que corresponde a la
descripción que se realiza sobre la tarea en cuestión, el
atributo “fechaCreacion” que representa la fecha y hora en la
que se crea la tarea (por defecto es la fecha y hora en que se
realiza la acción), y un atributo llamado “estado”, que muestra el estado actual de la tarea, y que tiene como valores posibles
“pendiente”, “en progreso” y “completada”.
El detalle de la tarea debe ser desplegado en una ventana
emergente tipo modal. El formulario de edición de la tarea
también se debe mostrar en una ventana emergente tipo
modal. Para la eliminación, se debe pedir confirmación al
usuario antes de realizar la acción.
Este listado de tareas debe ser obtenido desde la API Rest que
está en la ruta http://localhost:3000/api/tareas.
Finalmente, debe existir un enlace en el menú superior que
permita al usuario acceder a este listado de tareas.
```

```
editar el menu de la aplicacion para que se pueda acceder a todas las paginas creadas del proyecto
```

## Agregar seguridad al Backend

```
Agrega una nueva funcionalidad al aplicativo. En este caso se
necesita un CRUD de usuarios. De cada usuario se debe
conocer su nombre, sus apellidos, su correo electrónico, y
debe tener una clave encriptada. Se necesita, entonces, tener
endpoints para crear un usuario, editar un usuario por medio
de un ID (sin incluir la contraseña), eliminar un usuario en base
a su ID, listar los usuarios (sin mostrar la clave), y una opción para ver el detalle de un usuario de acuerdo con su ID.
Adicional a lo anterior, debe existir un endpoint para generar un
login de usuario. Este método debe recibir el correo electrónico
del usuario y su clave, y debe retornar los datos del usuario
(sin incluir la contraseña) y un token JWT.
Los usuarios estarán almacenados en la base de datos
MongoDB llamada “dbtareas” existente en el equipo local, y la
colección en la que se almacenarán los usuarios se llama
“usuarios”.
```

El siguiente paso en esta funcionalidad consiste en bloquear el acceso público
a todos los endpoints, excepto el de login.

```
Agrega al proyecto un middleware que impida acceder a
cualquier endpoint solo si se entrega un Bearer token JWT
válido. Esta regla no debe aplicar para el endpoint de login.
```

## Agregar un Login

```
Agrega al proyecto actual un componente que realice la labor
de login o acceso al sistema. Debe contener un formulario que
reciba un correo electrónico y una clave. Estos datos deben ser
enviados vía POST al endpoint
http://localhost:3000/api/usuarios/login.
Si la llamada arroja un error, se debe mostrar el mensaje de error respectivo sobre el formulario de login o acceso. En caso
que el usuario y contraseña sean válidos, se debe almacenar el
token obtenido en una variable y hacer una redirección al
componente de inicio.
Es importante considerar que este componente de login no
debe tener el menú que poseen los demás. Por lo mismo, debe
tener un estilo CSS diferente al resto.
```

## Inlcluir token en LocalStorage

* Solo sino lo ha realizado
* Puede sugerir hacer un interceptor
api.js en frontend

Usa esta instancia en tus componentes de tareas:
Por ejemplo, en CreateTask.vue y TaskList.vue, reemplaza
import axios from 'axios'
por
import api from '../services/api'
y cambia las llamadas, por ejemplo:
await axios.post('http://localhost:3000/api/tareas', nuevaTarea)
por
await api.post('/tareas', nuevaTarea)

```
En el componente de login, cuando el acceso es correcto el
token obtenido debe ser almacenado en Local Storage. Una
vez realizado lo anterior, se debe permitir que al llamar a las acciones relacionadas con tareas (crear, editar, eliminar, listar y
obtener detalle por ID), se proporcione el token almacenado en
Local Storage.
```

## Cierre de sesion

```
Agrega al menú principal una acción que permita cerrar la
sesión activa de usuario. Esto implica eliminar la variable que
almacena el token en el Local Storage, y posterior a esto
realizar una redirección al componente de Login.
```

## Impedir el acceso a los
componentes asociados a tareas y al componente de inicio en caso que no exista
una sesión activa

```
Agrega una funcionalidad al proyecto que impida el acceso a
los componentes de inicio, el listado de tareas y la creación de
tareas en caso que no exista una sesión de usuario activa.
```

Con todas las acciones realizadas en esta actividad y en las anteriores, se ha
logrado tener una plataforma que permite gestionar tareas, separando el backend
y el frontend, con ingreso por usuario y clave y cierre de sesión incorporado.
Como acciones adicionales, lo que se podría hacer es implementar el CRUD de
usuarios, o bien crear un perfil administrador y un perfil editor, con diferentes
atribuciones.