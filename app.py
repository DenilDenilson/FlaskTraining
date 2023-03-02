from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>"Hola mundo soy Flask 🌶️🌶️🌶️🌶️🌶️🌶️"</h1>
    """

@app.route("/contact")
def contact():
    return """
    <h1>"Contáctame soy Flask 🌶️🌶️"</h1>
    """

@app.route("/we")
def about():
    return """
    <h1>"Hola nosotros somos Flask 💓🌶️🌶️🌶️💓"</h1>
    """

@app.route("/login/<name>")
@app.route("/login")
def login(name = None): #Parámetros y URI se tienen que llamar igual
    if name is None:
        return f'<h1>Por favor ingresa tu nombre como uri</h1>'
    return redirect(url_for("dashboard", name=name))
    
@app.route("/dashboard/<name>")
@app.route("/dashboard")
def dashboard(name=None):
    if name is not None:
        return f"<h1>Bienvenido {name} al dashboard</h1>"
    return redirect(url_for("login"))

# Url_for
# Crea urls a partir de funciones alojadas por rutas
# puede servir para hacer rutas escalables en conjunto con redirect
# No tenemos que estar tratando con caracteres especiales (???)

@app.route("/ejemplo")
def example():
    return redirect(url_for("about"))

# Trabajando con métodos HTTP
# El método GET es el que se usa por defecto

# P O S T

@app.route("/loginpost", methods=["GET", "POST"]) # Se colocan los métodos permitidos
def loginPost():
    print(request)
    if request.method == "POST":
        username = request.form["username"] # name del input
        password = request.form["password"]

        if username and password:
            return redirect(url_for("loginEnter", name=username, password=password))
    
    
    return """
        <form method="POST">
            <h3>Ingresa tus datos</h3>
            <input type="text" name="username" /> <br/> <br/>
            <input type="password" name="password" /> <br/> <br/>
            <button type="submit" >Enviar</button>
        </form>
    """
# @app.route("/loginenter/<name>")
@app.route("/loginenter")
def loginEnter():
    print(request.args.get('password'))
    return f'<h1>Bienvenido {request.args.get("name")} desde el form tu contraseña es "{request.args.get("password")}" xd</h1>'