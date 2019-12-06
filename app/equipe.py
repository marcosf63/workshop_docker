from flask import Flask, escape, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    conn = psycopg2.connect('dbname=ditec user=postgres host=db')
    cur = conn.cursor()
    # teste    
    nome = request.args.get("nome")
    print(nome, flush=True)    
    if nome == None:
        nome = "World"
    else:
        cur.execute('SELECT * FROM equipe WHERE nome=%s', (nome,))
        resp = cur.fetchall()
        if len(resp) == 0:
            nome = "World"
            print("resp="+str(resp), flush=True)  
        else:
            nome = resp[0][1]

    return f'Hello, {escape(nome)}!'
