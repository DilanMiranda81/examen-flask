from flask import Flask, render_template, request

app = Flask(__name__)


def calcular_compra(edad: int, cantidad: int) -> tuple[int, float, float]:
    precio_unitario = 9000
    total_sin_descuento = precio_unitario * cantidad

    if 18 <= edad <= 30:
        porcentaje_descuento = 0.15
    elif edad > 30:
        porcentaje_descuento = 0.25
    else:
        porcentaje_descuento = 0.0

    monto_descuento = total_sin_descuento * porcentaje_descuento
    total_a_pagar = total_sin_descuento - monto_descuento
    return total_sin_descuento, monto_descuento, total_a_pagar


def verificar_credenciales(usuario: str, contrasena: str) -> str:
    usuarios = {
        "juan": ("admin", "Bienvenido Administrador juan"),
        "pepe": ("user", "Bienvenido Usuario pepe"),
    }

    if usuario in usuarios:
        clave_correcta, mensaje = usuarios[usuario]
        if contrasena == clave_correcta:
            return mensaje

    return "Usuario o contraseña incorrectos"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        edad = int(request.form.get("edad", 0))
        cantidad = int(request.form.get("cantidad", 0))

        total_sin_descuento, descuento, total_a_pagar = calcular_compra(edad, cantidad)
        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "descuento": descuento,
            "total_a_pagar": total_a_pagar,
        }

    return render_template("ejercicio1.html", resultado=resultado)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        contrasena = request.form.get("contrasena", "")
        mensaje = verificar_credenciales(usuario, contrasena)

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)