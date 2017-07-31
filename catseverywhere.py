from flask import Flask, render_template
from flask import request, redirect
from flask import g

import sqlite3
app = Flask(__name__)
usuarios = []
contraseas=[]

@app.route('/')
def hello_world():
    author = "Jorge"
    name = "paolo"
    return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup():
    usuario = request.form['username']
    contrasea = request.form['password']
    usuarios.append(usuario)
    contraseas.append(contrasea)
    print usuarios
    usuariosdb = g.db.execute("SELECT usuario FROM uscon").fetchall()
    clavedb = g.db.execute("SELECT conta FROM uscon").fetchall()
    print usuariosdb
    print usuariosdb[1][0]
    c=0
   # for elemento in usuarios:
   # print elemento
    for i in range (len(usuariosdb)):
        
        if usuarios[0] == usuariosdb[i][0]:
            
            #pos=usuariosdb.index(elemento)
            print "esta el usuario en "
            print i
            c=2
            #for cont in contraseas:
            if contraseas[len(contraseas)-1] == clavedb[i][0]:
                
                print "la contraseña coincide"
            else:
                print "contraseña incorrecta"
            
    
    if c==0:
        
        g.db.execute("INSERT INTO uscon VALUES (?,?)", [usuario,contrasea])
        ## g.db.execute("INSERT INTO other VALUES (?)", [contrasea])
        g.db.commit()
        print "no esta"
    #
    ##if usuarios in usuariosdb:
    #    pos=usuariosdb.index(usuario)
    #    print "esta el usuario"
    
    #g.db.execute("INSERT INTO uscon VALUES (?,?)", [usuario,contrasea])
   ## g.db.execute("INSERT INTO other VALUES (?)", [contrasea])
    #g.db.commit()
    print(usuarios)
    print (contraseas)
    del usuarios[:]
    return redirect('/')

@app.route('/emails.html')
def emails():
    usuarioss = g.db.execute("SELECT usuario FROM uscon").fetchall()
    other = g.db.execute("SELECT conta FROM uscon").fetchall()
    return render_template('emails.html', email_addresses=usuarioss, contras=other)

@app.before_request
def before_request():
    g.db = sqlite3.connect("emails.db")
    
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
    
if __name__ == "__main__":
    app.run()
