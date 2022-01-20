from flask import Flask, render_template, request
import data

app = Flask(__name__)

@app.route('/') 
def index(): 
    return render_template('index.html')


@app.route('/bonjour/<name>')
def bonjour(name):
    return render_template('bonjour.html', quelquun=name)

@app.route('/donnateur')
def donnateur():
    utilisateur = data.get_users()
    total = data.total_dons()
    return render_template('donnateur.html', quelquun=utilisateur, total=total)


@app.route('/ajouter')
def ajouter():
    return render_template('form_don.html')

@app.route('/add', methods=['POST'])
def add():
    nom = request.values.get('nom')
    prenom = request.values.get('prenom')
    adresse = request.values.get('adresse')
    email = request.values.get('email')
    somme_promise = request.values.get('somme_promise')


    data.set_user(nom, prenom, adresse, email, somme_promise)
    
    return render_template('add.html')

if __name__== "__main__" :
    app.run(debug=True, port=5000)