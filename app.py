from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/saluta', methods=['POST'])
def saluta():
    nome = request.form.get('nome')
    cognome = request.form.get('cognome')
    if nome and cognome:
        return jsonify({'saluto': f'Ciao, {nome} {cognome}!'})
    return jsonify({'saluto': 'Per favore, inserisci il nome e il cognome.'})

if __name__ == '__main__':
    app.run(debug=True)
