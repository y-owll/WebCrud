from flask import Flask, request, escape, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    quantityOfBuys = db.Column(db.Integer, nullable=True)
    def __repr__(self):
        return self.name

@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return(render_template('index.html', data=items))

@app.route('/about')
def about():
    return(render_template('about.html'))

@app.route('/create', methods = ['POST','GET'])
def create():
    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        quantityOfBuys = request.form['quantityOfBuys']

        item = Item(name = name, price = price, quantity = quantity, quantityOfBuys = quantityOfBuys)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "ошибка"
    else:
        return(render_template('create.html'))

if __name__ == "__main__":
    app.run(debug=True)
