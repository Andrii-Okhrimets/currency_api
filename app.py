from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from schemas import CurrentSchema


app = Flask(__name__)
client = app.test_client()
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:sport007@localhost:5432/current"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = 'fhsjkjksdf4yr73iy29cyiusdhfw3r9827rehifu398r72983hwiu'

db = SQLAlchemy(app)

docs = FlaskApiSpec()

docs.init_app(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='videoblog',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/swagger/'
})



class Current(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(10))
    price = db.Column(db.String(20))
    date = db.Column(db.DateTime, default=datetime.now().date())

    def __repr__(self):
        return f'<current {self.id}>'

url = 'https://api.currencyfreaks.com/latest?apikey=0897bfca26924c718722196133f86564&symbols={}'

@app.route('/', methods=['POST', 'GET'])
def add_current():
    if request.method == 'POST':
        code_curent = request.form['currency']
        if code_curent.lower() == code_curent:
            code_curent = code_curent.upper()
        if len(code_curent) == 3:
            flash('You entered the wrong value')
        else:
            flash('request completed successfully')
        try:
            res = requests.get(url.format(code_curent)).json()
            info = Current.query.filter_by(currency=str(code_curent)).order_by(Current.id.desc()).all()
            if not info:
                c = Current(currency=code_curent, price=res['rates'][code_curent])
                db.session.add(c)
                db.session.commit()
                return redirect(url_for('current', currency_code=code_curent))
            elif info[0].price == res['rates'][code_curent]:
                return redirect(url_for('current', currency_code=code_curent))
            else:
                c = Current(currency=code_curent, price=res['rates'][code_curent])
                db.session.add(c)
                db.session.commit()
            return redirect(url_for('current', currency_code=code_curent))
        except BaseException:
            print('Error')
    
    return render_template('add_curent.html')

@app.route('/filters', methods=['GET'])
def filters():
    d = request.args.get('currency')
    f = request.args.get('date')
    info = Current.query.filter_by(currency=d).filter_by(date=f).all()
    chema = CurrentSchema(many=True)
    chemas = chema.dump(info)
    return render_template('filters.html', info=chemas)

@app.route('/current/<currency_code>')
def current(currency_code):
    info = Current.query.filter_by(currency=str(currency_code)).order_by(Current.id.desc()).limit(1)
    infod = info[0]
    schema = CurrentSchema()
    schemas = schema.dump(infod)
    
    return render_template('current.html', info=schemas)

docs.register(current)
docs.register(filters)

if __name__ == __name__:
    app.run(debug=True)
