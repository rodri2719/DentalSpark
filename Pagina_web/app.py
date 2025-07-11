import web
import os

# ----------------------- Configuración -----------------------
urls = (
    '/', 'Index',
    '/static/(.*)', 'Static'  # Solo para archivos como styles.css
)

# Sistema de plantillas (HTML con $def with ())
render = web.template.render('templates/')

# ----------------------- Controladores -----------------------

# Página principal
class Index:
    def GET(self):
        return render.index()

# Servidor de archivos estáticos (solo .css)
class Static:
    def GET(self, file):
        try:
            if not file.endswith('.css'):
                return web.notfound("Solo se permiten archivos CSS.")
            
            path = os.path.join('static', file)
            with open(path, 'rb') as f:
                content = f.read()

            web.header('Content-Type', 'text/css')
            return content
        except FileNotFoundError:
            return web.notfound("Archivo CSS no encontrado.")

# ----------------------- Ejecutar -----------------------
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
