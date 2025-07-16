import web
import os

# ----------------------- Rutas -----------------------
urls = (
    '/', 'Index',
    '/login.html', 'Login',
    '/registro.html', 'Registro',
    '/logout', 'Logout',
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
        return render.login(msg="")
    def POST(self):
        # Deshabilitado: validación de base de datos
        # Siempre redirige a login.html para pruebas visuales
        raise web.seeother('/login.html')

class Registro:
    def GET(self):
        return render.registro(msg="")
    def POST(self):
        # Lógica de registro eliminada
        return render.registro(msg="Funcionalidad deshabilitada.")

class Logout:
    def GET(self):
        web.setcookie('usuario', '', expires=-1)
        raise web.seeother('/')

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
            path = os.path.join('static', file)
            ext = os.path.splitext(file)[1].lower()
            content_types = {
                '.css': 'text/css',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.gif': 'image/gif',
                '.mp4': 'video/mp4',
                '.ico': 'image/x-icon',
                '.svg': 'image/svg+xml',
            }
            content_type = content_types.get(ext, 'application/octet-stream')
            with open(path, 'rb') as f:
                content = f.read()
            web.header('Content-Type', content_type)
            return content
        except FileNotFoundError:
            return web.notfound("Archivo estático no encontrado.")

# ----------------------- Ejecutar -----------------------
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
