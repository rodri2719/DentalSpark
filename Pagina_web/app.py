import web
import os

# ----------------------- Rutas -----------------------
urls = (
    '/', 'Index',
    '/login.html', 'Login',
    '/recomendaciones.html', 'Recomendaciones',
    '/enfermedades.html', 'Enfermedades',
    '/juego.html', 'Juego',
    '/perfil.html', 'Perfil',
    '/sobre_nosotros.html', 'SobreNosotros',
    '/static/(.*)', 'Static',  # Sirve archivos CSS
)

# ----------------------- Renderizado de plantillas -----------------------
render = web.template.render('templates/')

# ----------------------- Controladores de páginas -----------------------
class Index:
    def GET(self):
        return render.index()

class Login:
    def GET(self):
        return render.login()

class Recomendaciones:
    def GET(self):
        return render.recomendaciones()

class Enfermedades:
    def GET(self):
        return render.enfermedades()

class Juego:
    def GET(self):
        return render.juego()

class Perfil:
    def GET(self):
        return render.perfil()

class SobreNosotros:
    def GET(self):
        return render.sobre_nosotros()

# ----------------------- Servidor de archivos estáticos (solo CSS) -----------------------
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
