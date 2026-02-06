# Práctica 10: Infraestructura de Microservicios Segura con Docker y Caché Multinivel
**Alumno:** Amado  
**Asignatura:** Seguridad y Alta Disponibilidad

## 1. Descripción
Esta práctica consiste en el despliegue de un entorno contenedorizado para la empresa "Cloud-Fast". Se implementa un Proxy Inverso (Nginx) con caché de nivel 1, una API Flask y un servidor Redis como caché de nivel 2.

## 2. Diagrama de Arquitectura
![Diagrama de Arquitectura](./diagrama.png)
*Nota: El diagrama muestra la red privada 172.x.x.x y el flujo de peticiones desde el exterior únicamente por el puerto 80.*

## 3. Instrucciones de Despliegue
Para clonar y levantar el entorno completo, ejecute:
\`\`\`bash
git clone https://github.com/Drake-73/Practica10.git
cd Practica10
docker compose up -d --build
\`\`\`

## 4. Pruebas de Verificación
Para comprobar el funcionamiento de la caché multinivel, utilice el comando curl:
\`\`\`bash
# Verificación de cabeceras y estado de caché
curl -I http://localhost
\`\`\`
* **MISS**: Primera petición o caché expirada (60s).
* **HIT**: Petición servida desde la caché de Nginx o Redis.

