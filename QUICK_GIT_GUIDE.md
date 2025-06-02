# 🎮 404 Luck Not Found - Quick Git Guide

## 🚀 Comandos Rápidos para Commits

### 📝 **Cambios en Cliente:**
```bash
cd cliente
git add .
git commit -m "feat: tu descripción aquí"
git push origin main
cd ..
git add cliente
git commit -m "feat: actualizar cliente"
git push origin main
```

### 🖥️ **Cambios en Servidor:**
```bash
cd servidor
git add .
git commit -m "fix: tu descripción aquí"
git push origin main
cd ..
git add servidor
git commit -m "fix: actualizar servidor"
git push origin main
```

### 🔄 **Ambos a la vez:**
```bash
# 1. Cliente
cd cliente && git add . && git commit -m "feat: cambios cliente" && git push origin main

# 2. Servidor  
cd ../servidor && git add . && git commit -m "feat: cambios servidor" && git push origin main

# 3. Principal
cd .. && git add cliente servidor && git commit -m "feat: actualizar ambos submódulos" && git push origin main
```

## 📋 **Prefijos de Commit:**
- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de errores  
- `refactor:` - Refactorización
- `docs:` - Documentación
- `style:` - Formato/estilo

## 🆘 **En caso de problemas:**
Ver guía completa: `README_GIT_WORKFLOW.md`

---
*¿Dudas? Consulta la guía completa o usa `git status` para ver el estado actual.*
