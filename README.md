# 🚀 Guía de Trabajo con Git y Submódulos - 404 Luck Not Found

## 📋 Índice

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Flujo de Trabajo Básico](#flujo-de-trabajo-básico)
- [Trabajando con Submódulos](#trabajando-con-submódulos)
- [Comandos Útiles](#comandos-útiles)
- [Casos Comunes](#casos-comunes)
- [Solución de Problemas](#solución-de-problemas)

---

## 🏗️ Estructura del Proyecto

Este proyecto utiliza **Git Submódulos** con la siguiente estructura:

```
404_Luck_Not_Found/ (Repositorio principal)
├── .gitmodules                 # Configuración de submódulos
├── README_GIT_WORKFLOW.md      # Esta guía
├── cliente/                    # Submódulo - Frontend/UI
│   ├── screens/               # Pantallas del juego
│   ├── utils/                 # Utilidades del cliente
│   └── inicio.py              # Punto de entrada del cliente
└── servidor/                   # Submódulo - Backend/API
    ├── src/                   # Código fuente del servidor
    └── requirements.txt       # Dependencias
```

### 🔗 Repositorios SSH:

- **Principal:** `git@github.com:sga-encoder/404_Luck_Not_Found.git`
- **Cliente:** `git@github.com:sga-encoder/404_Luck_Not_Found_Cliente.git`
- **Servidor:** `git@github.com:sga-encoder/404_Luck_Not_Found_Servidor.git`

---

## 🔄 Flujo de Trabajo Básico

### 1️⃣ **Para cambios EN los submódulos (cliente o servidor):**

```bash
# Paso 1: Navegar al submódulo
cd cliente    # o 'cd servidor'

# Paso 2: Verificar estado
git status
git branch    # Asegurarse de estar en 'main'

# Paso 3: Hacer cambios y confirmarlos
git add .
git commit -m "tipo: descripción del cambio"

# Paso 4: Subir cambios del submódulo
git push origin main
```

### 2️⃣ **Para actualizar referencias en el repositorio principal:**

```bash
# Paso 5: Volver al directorio principal
cd ..

# Paso 6: Agregar referencia actualizada
git add cliente    # o 'git add servidor'
git commit -m "feat: actualizar submódulo cliente"

# Paso 7: Subir cambios del repositorio principal
git push origin main
```

---

## 🎯 Trabajando con Submódulos

### 📝 **Convenciones de Commits**

Usa estos prefijos para tus mensajes de commit:

- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de errores
- `refactor:` - Refactorización de código
- `style:` - Cambios de formato/estilo
- `docs:` - Documentación
- `test:` - Pruebas

**Ejemplos:**

```bash
git commit -m "feat: agregar formulario de login avanzado"
git commit -m "fix: corregir validación de contraseña"
git commit -m "refactor: reorganizar estructura de carpetas"
```

### 🔄 **Flujo Completo con Ejemplo**

Supongamos que quieres agregar una nueva funcionalidad al **cliente**:

```bash
# 1. Ir al submódulo cliente
cd cliente

# 2. Crear una nueva rama (opcional pero recomendado)
git checkout -b feature/nueva-funcionalidad

# 3. Hacer tus cambios
# ... editar archivos ...

# 4. Verificar cambios
git status
git diff

# 5. Agregar y confirmar cambios
git add .
git commit -m "feat: agregar nueva funcionalidad al menú"

# 6. Subir la rama (si es nueva)
git push origin feature/nueva-funcionalidad

# 7. Hacer merge a main (o crear Pull Request)
git checkout main
git merge feature/nueva-funcionalidad
git push origin main

# 8. Volver al repositorio principal
cd ..

# 9. Actualizar referencia del submódulo
git add cliente
git commit -m "feat: actualizar cliente con nueva funcionalidad"
git push origin main
```

---

## 🛠️ Comandos Útiles

### 📊 **Estado y Información**

```bash
# Ver estado de todos los submódulos
git submodule status

# Ver estado detallado
git status

# Ver log de commits recientes
git log --oneline -10

# Ver log de todos los submódulos
git submodule foreach 'git log --oneline -5'
```

### 🔄 **Sincronización**

```bash
# Actualizar todos los submódulos a la última versión
git submodule update --remote

# Hacer pull en todos los submódulos
git submodule foreach 'git pull origin main'

# Sincronizar URLs después de cambios en .gitmodules
git submodule sync
```

### 🔍 **Navegación**

```bash
# Ver configuración de submódulos
cat .gitmodules

# Ver URLs configuradas
git config --list | findstr url

# Ver remotos de un submódulo
cd cliente && git remote -v
```

---

## 📘 Casos Comunes

### 🆕 **Clonar el proyecto completo**

```bash
# Opción 1: Clonar con submódulos
git clone --recursive git@github.com:sga-encoder/404_Luck_Not_Found.git

# Opción 2: Clonar y luego inicializar submódulos
git clone git@github.com:sga-encoder/404_Luck_Not_Found.git
cd 404_Luck_Not_Found
git submodule update --init --recursive
```

### 🔧 **Hacer cambios en múltiples submódulos**

```bash
# 1. Cambios en servidor
cd servidor
git add .
git commit -m "fix: corregir bug en la lógica de juego"
git push origin main

# 2. Cambios en cliente
cd ../cliente
git add .
git commit -m "feat: agregar nueva pantalla de configuración"
git push origin main

# 3. Actualizar repositorio principal
cd ..
git add servidor cliente
git commit -m "feat: actualizar ambos submódulos con mejoras"
git push origin main
```

### 🔄 **Trabajar con ramas en submódulos**

```bash
# Crear rama en submódulo
cd cliente
git checkout -b feature/nueva-caracteristica

# Hacer cambios y commits
git add .
git commit -m "feat: implementar nueva característica"

# Subir rama
git push origin feature/nueva-caracteristica

# El repositorio principal apuntará a esta rama
cd ..
git add cliente
git commit -m "wip: cliente en rama feature/nueva-caracteristica"
```

---

## 🚨 Solución de Problemas

### ❌ **Error: "src refspec main does not match any"**

```bash
# Problema: No hay commits en la rama main
# Solución: Hacer un commit inicial
git add .
git commit -m "initial commit"
git push origin main
```

### ❌ **Submódulo en estado "detached HEAD"**

```bash
# Problema: El submódulo no está en una rama
# Solución: Cambiar a la rama main
cd cliente  # o servidor
git checkout main
git pull origin main
```

### ❌ **Conflictos en submódulos**

```bash
# Resolver conflictos manualmente en cada submódulo
cd cliente
git status
# ... resolver conflictos ...
git add .
git commit -m "fix: resolver conflictos"
git push origin main

cd ..
git add cliente
git commit -m "fix: actualizar cliente después de resolver conflictos"
```

### ❌ **URLs HTTPS vs SSH**

```bash
# Cambiar de HTTPS a SSH
git config submodule.cliente.url git@github.com:sga-encoder/404_Luck_Not_Found_Cliente.git
git config submodule.servidor.url git@github.com:sga-encoder/404_Luck_Not_Found_Servidor.git
git submodule sync

# Actualizar remotos en submódulos
cd cliente && git remote set-url origin git@github.com:sga-encoder/404_Luck_Not_Found_Cliente.git
cd ../servidor && git remote set-url origin git@github.com:sga-encoder/404_Luck_Not_Found_Servidor.git
```

---

## ✅ **Checklist antes de hacer Push**

### 🔍 **Antes de hacer commit:**

- [ ] `git status` - Verificar qué archivos están cambiados
- [ ] `git diff` - Revisar los cambios específicos
- [ ] Probar que el código funcione correctamente
- [ ] Escribir un mensaje de commit descriptivo

### 🚀 **Antes de hacer push:**

- [ ] `git log --oneline -5` - Verificar los commits
- [ ] Asegurarse de estar en la rama correcta
- [ ] Si es submódulo: actualizar referencia en el repo principal
- [ ] Probar que todo funcione después del push

### 📋 **Flujo completo verificado:**

1. ✅ Cambios en submódulo → commit → push
2. ✅ Actualizar referencia en repositorio principal → commit → push
3. ✅ Verificar que el proyecto completo funcione

---

## 🎯 **Comandos de Emergencia**

```bash
# Deshacer último commit (sin perder cambios)
git reset --soft HEAD~1

# Deshacer cambios no confirmados
git restore .

# Ver diferencias entre submódulo y remoto
cd cliente && git fetch && git log HEAD..origin/main --oneline

# Forzar actualización de submódulo
git submodule update --force
```

---

## 📞 **Contacto y Ayuda**

Si tienes problemas con Git o los submódulos:

1. Revisar esta guía
2. Usar `git status` y `git log` para entender el estado actual
3. Consultar la documentación oficial de Git
4. Hacer backup antes de operaciones complejas

**¡Recuerda siempre hacer backup de tus cambios importantes!** 🔐

---

_Última actualización: 2 de junio de 2025_
