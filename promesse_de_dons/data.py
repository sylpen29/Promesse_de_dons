import mysql.connector as mysqlpyth

bdd = None 
cursor = None

def connexion(): 
    global bdd 
    global cursor
    bdd = mysqlpyth.connect(user='root', password='root', host='localhost', port="8081", database='promesse_dons') 
    cursor = bdd.cursor()

def deconnexion(): 
    global bdd 
    global cursor
    cursor.close() 
    bdd.close()

def get_users() :
    global cursor

    connexion()
    query = "SELECT * FROM form_don"
    cursor.execute(query)
    form_don = []

    for enregistrement in cursor :
        form = {}
        form['id_form'] = enregistrement[0]
        form['nom'] = enregistrement[1]
        form['prenom'] = enregistrement[2]
        form['adresse'] = enregistrement[3]
        form['email'] = enregistrement[4]
        form['somme_promise'] = enregistrement[5]
        form_don.append(form)
    
    print(form_don)
    deconnexion()
    return form_don

def get_user():
    global cursor

    connexion()
    query = "SELECT * FROM form_don" 
    cursor.execute(query)
    form = {}

    for enregistrement in cursor :
        form['id_form'] = enregistrement[0]
        form['nom'] = enregistrement[1]
        form['prenom'] = enregistrement[2]
        form['adresse'] = enregistrement[3]
        form['email'] = enregistrement[4]
        form['somme_promise'] = enregistrement[5]
    
    deconnexion()
    return form
    
def set_user(nom, prenom, adresse, email, somme_promise):
    global bdd
    global cursor

    connexion()

    query = 'INSERT INTO form_don(nom, prenom, adresse, email, somme_promise) VALUES (%s, %s, %s, %s, %s);'
    valeurs = (nom, prenom, adresse, email, somme_promise)
    cursor.execute(query, valeurs)

    bdd.commit()
    deconnexion()

def total_dons() :
    global bdd
    global cursor

    connexion()
    query = "SELECT somme_promise FROM form_don"
    cursor.execute(query)
    total=0

    for enregistrement in cursor : 
        total += enregistrement[0]
    

    
    deconnexion()
    return total