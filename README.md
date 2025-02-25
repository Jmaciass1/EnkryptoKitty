# EnkryptoKitty
Esta es una aplicación de criptografía para el curso de *Introducción a la Criptografía y a la Teoría de la Información*.

**Autores**
- Jaime Andrés Macias Sánchez  
- Jacel Thomás Enciso Pinzón  

<div align="center">
    <img src="logo.png" alt="Logo de EnkryptoKitty" width="500" height="500"/>
</div>

## Instalación
Para instalar **EnkryptoKitty**, sigue estos pasos:

### 1. Descargar el repositorio
Puedes hacer esto descargando el archivo `.zip` de este repositorio o clonándolo con Git:
### 2. Crear un ambiente virtual
Esto se hace para garantizar que las dependencias de **EnkryptoKitty** funcionen correctamente y de manera aislada.  
Primero, navega hasta la carpeta de la interfaz gráfica (**gui**):
```
  cd path/to/folder/gui
  ```
- Crear ambiente virtual
  ```
  python -m venv myenv
  ```
- Activar ambiente virtual
  ```
  source myenv/bin/activate
  ```
- Si da problemas de permisos, ejecutar y luego repetir el paso anterior
  ```
  Set-ExecutionPolicy Unrestricted -Scope CurrentUser
  ```
### 3. Instalar dependencias
Puedes instalar todas las dependencias ejecutando:
```
pip install mpmath numpy ordered-set packaging Pillow pycipher pycryptodome pyinstaller pympler sympy PySide6
```

### 4. Ejecutar EnkryptoKitty
Asegúrate de estar en la carpeta `gui` del proyecto. Luego, ejecuta la aplicación con:
```
python main.py
```

---

Universidad Nacional de Colombia.
Departamento de Matemáticas 
2025
