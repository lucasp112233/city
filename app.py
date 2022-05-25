from flask import Flask, redirect , render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/datos.db'
db = SQLAlchemy(app)

class Order(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    fecha =db.Column(db.String(10))
    cliente =db.Column(db.String(200))
    movil =db.Column(db.String(200))
    precio_producto =db.Column(db.String(200))
    precio_delivery =db.Column(db.String(200))
    ciudad =db.Column(db.String(200))



@app.route("/")
def inicio():
    orders = Order.query.all()
    return render_template ("index.html",orders= orders) 
    

@app.route("/create-order", methods=['POST'])
def create_order():
    order=Order(fecha = request.form['fecha'],cliente = request.form['cliente'],movil = request.form['movil'],precio_producto = request.form['precio_producto'],precio_delivery = request.form['precio_delivery'],ciudad = request.form['ciudad'])
    db.session.add(order)
    db.session.commit()
    return redirect(url_for("inicio"))
    


if __name__ =='__main__':
    app.run(debug=True)