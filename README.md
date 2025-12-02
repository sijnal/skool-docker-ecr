# Taller de Docker y ECR - Demo de Optimización de Imágenes

Este proyecto es una demostración práctica de optimización de imágenes Docker. Incluye una aplicación Flask simple que muestra diferentes técnicas de optimización, desde una imagen básica hasta una versión optimizada y segura.

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

### 1. Docker Desktop

**Para Windows/Mac:**
- Descarga Docker Desktop desde: https://www.docker.com/products/docker-desktop
- Instala y ejecuta Docker Desktop
- Verifica la instalación ejecutando en tu terminal:
  ```bash
  docker --version
  ```

**Para Linux:**
- Instala Docker Engine siguiendo la guía oficial: https://docs.docker.com/engine/install/
- Verifica la instalación:
  ```bash
  docker --version
  ```

### 2. Cuenta de GitHub

- Si no tienes una cuenta, créala en: https://github.com/signup
- Necesitarás acceso a GitHub para clonar el repositorio y trabajar con él

### 3. Terminal/Consola

- Windows: PowerShell o Git Bash
- Mac/Linux: Terminal nativo

## 🚀 Primeros Pasos

### Paso 1: Clonar el Repositorio

Abre tu terminal y ejecuta:

```bash
git clone <URL_DEL_REPOSITORIO>
cd ieee-cicd-demo
```

### Paso 2: Verificar que Docker Funciona

Ejecuta este comando para verificar que Docker está funcionando correctamente:

```bash
docker run hello-world
```

Si ves un mensaje de bienvenida, ¡Docker está funcionando correctamente!

## 📦 Estructura del Proyecto

Este proyecto contiene **4 Dockerfiles** que muestran la progresión de optimización:

1. **`Dockerfile.pesado`** - Imagen sin optimizaciones (1.6GB+)
2. **`Dockerfile.liviano`** - Primera optimización con Alpine (92MB)
3. **`Dockerfile.multistage`** - Optimización con multi-stage build (79MB)
4. **`Dockerfile.seguro`** - Versión optimizada y segura con usuario no-root (90MB)

## 🏗️ Construcción de Imágenes Docker

### Paso 3: Construir la Primera Imagen (Pesada)

Esta es la versión sin optimizaciones. Ejecuta:

```bash
docker build -f Dockerfile.pesado -t demo-app:pesado .
```

**¿Qué hace este comando?**
- `-f Dockerfile.pesado`: Especifica qué Dockerfile usar
- `-t demo-app:pesado`: Le da un nombre y etiqueta a la imagen
- `.`: Indica que el contexto de construcción es el directorio actual

**Tiempo estimado:** 2-5 minutos (dependiendo de tu conexión)

### Paso 4: Construir la Imagen Liviana (Alpine)

Esta versión usa Alpine Linux, una distribución muy ligera:

```bash
docker build -f Dockerfile.liviano -t demo-app:liviano .
```

**Tiempo estimado:** 1-3 minutos

### Paso 5: Construir la Imagen Multi-Stage

Esta versión usa multi-stage build para separar construcción y ejecución:

```bash
docker build -f Dockerfile.multistage -t demo-app:multistage .
```

**Tiempo estimado:** 1-3 minutos

### Paso 6: Construir la Imagen Segura

Esta versión combina optimización con seguridad (usuario no-root):

```bash
docker build -f Dockerfile.seguro -t demo-app:seguro .
```

**Tiempo estimado:** 1-3 minutos

## 📊 Comparar Tamaños de las Imágenes

### Paso 7: Ver el Tamaño de las Imágenes

Ejecuta este comando para ver el tamaño de todas las imágenes construidas:

```bash
docker images demo-app
```

Deberías ver algo como esto:

```
REPOSITORY   TAG          SIZE
demo-app     seguro       90.7MB
demo-app     multistage   79.7MB
demo-app     liviano      92.6MB
demo-app     pesado       1.63GB
```

**Observa la diferencia:** La imagen pesada es aproximadamente **20 veces más grande** que las optimizadas.

## 🧪 Probar las Imágenes

### Paso 8: Ejecutar una Imagen

Para ejecutar una imagen y probar que funciona:

```bash
docker run -d -p 8080:80 --name test-app demo-app:pesado
```

**¿Qué hace este comando?**
- `-d`: Ejecuta el contenedor en segundo plano (detached)
- `-p 8080:80`: Mapea el puerto 80 del contenedor al puerto 8080 de tu máquina
- `--name test-app`: Le da un nombre al contenedor
- `demo-app:pesado`: La imagen a ejecutar

### Paso 9: Verificar que Funciona

Abre tu navegador y visita: **http://localhost:8080**

Deberías ver la aplicación Flask funcionando.

### Paso 10: Detener y Eliminar el Contenedor

```bash
docker stop test-app
docker rm test-app
```

O en un solo comando:

```bash
docker rm -f test-app
```

## 🔍 Entender las Diferencias

### Dockerfile.pesado
- Usa la imagen base completa de Python (`python:3.13.7`)
- Incluye todas las herramientas de desarrollo
- **Problema:** Muy grande, incluye cosas innecesarias

### Dockerfile.liviano
- Usa Alpine Linux (`python:3.13.7-alpine3.22`)
- Distribución mínima de Linux
- **Beneficio:** Reduce el tamaño en ~95%

### Dockerfile.multistage
- Separa el proceso de construcción del de ejecución
- Solo incluye lo necesario para ejecutar la app
- **Beneficio:** Elimina herramientas de compilación del resultado final

### Dockerfile.seguro
- Combina multi-stage con usuario no-root
- Ejecuta como usuario limitado (no root)
- **Beneficio:** Más seguro y optimizado

## 🧹 Limpieza

### Eliminar Imágenes

Si quieres eliminar las imágenes para liberar espacio:

```bash
# Eliminar una imagen específica
docker rmi demo-app:pesado

# Eliminar todas las imágenes demo-app
docker rmi demo-app:pesado demo-app:liviano demo-app:multistage demo-app:seguro
```

### Limpiar Todo Docker

Si quieres limpiar todo (imágenes, contenedores, volúmenes no usados):

```bash
docker system prune -a
```

⚠️ **Cuidado:** Esto eliminará todas las imágenes y contenedores que no estén en uso.

## 📚 Conceptos Aprendidos

Al completar este taller, habrás aprendido:

1. ✅ Cómo construir imágenes Docker
2. ✅ Diferencia entre imágenes base completas y minimalistas
3. ✅ Qué es multi-stage build y por qué es útil
4. ✅ Cómo crear imágenes seguras con usuario no-root
5. ✅ Cómo comparar tamaños de imágenes
6. ✅ Cómo ejecutar y probar contenedores Docker

## 🐛 Solución de Problemas

### Error: "Cannot connect to the Docker daemon"

**Solución:** Asegúrate de que Docker Desktop esté ejecutándose.

### Error: "port is already allocated"

**Solución:** El puerto ya está en uso. Usa otro puerto:
```bash
docker run -d -p 8081:80 --name test-app demo-app:pesado
```

### Error: "no space left on device"

**Solución:** Limpia imágenes y contenedores no usados:
```bash
docker system prune -a
```

## 📝 Variables de Entorno

La aplicación Flask soporta las siguientes variables de entorno (todas opcionales):

- `TITLE`: Título que se mostrará (default: `Not-Title`)
- `MICROSERVICIO`: Nombre del microservicio (default: `Not-Microservice`)
- `DB_HOST`: Host de la base de datos (default: `localhost`)
- `DB_PORT`: Puerto de la base de datos (default: `3306`)
- `DB_USER`: Usuario de la base de datos (default: `db_user`)
- `DB_PASSWORD`: Contraseña de la base de datos (default: `db_password`)
- `DB_NAME`: Nombre de la base de datos (default: `db_name`)

Ejemplo de uso:

```bash
docker run -d -p 8080:80 \
  -e TITLE="Mi Aplicación" \
  -e MICROSERVICIO="Mi-Servicio" \
  --name test-app demo-app:seguro
```

## 🎯 Próximos Pasos

Una vez que domines estos conceptos básicos, puedes explorar:

- Docker Compose para orquestar múltiples contenedores
- Integración con AWS ECR (Elastic Container Registry)
- CI/CD con GitHub Actions
- Despliegue en contenedores en la nube

## 💡 Consejos para Principiantes

1. **Lee los Dockerfiles:** Abre cada Dockerfile y lee los comentarios para entender qué hace cada línea
2. **Experimenta:** Prueba modificar los Dockerfiles y ver qué pasa
3. **Usa `docker ps`:** Para ver contenedores en ejecución
4. **Usa `docker logs`:** Para ver los logs de un contenedor: `docker logs test-app`
5. **No tengas miedo de borrar:** Puedes reconstruir las imágenes cuando quieras

## 🤝 Contribuir

Este es un proyecto educativo. Si encuentras errores o tienes sugerencias, ¡las contribuciones son bienvenidas!

---

**¡Feliz aprendizaje! 🐳**
