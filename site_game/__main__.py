from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Liste d'épicerie en mémoire
liste_eleves = []

@app.route('/')
def index():
    return render_template('index.html')

# Route pour afficher la liste
@app.route('/liste', methods=['GET'])
def afficher_liste():
    return jsonify(liste_eleves)

# Route pour ajouter un élément
@app.route('/ajouter', methods=['POST'])
def ajouter_element():
    data = request.json
    liste_eleves.append(data['item'])
    return jsonify({'message': 'Item ajouté !'}), 201

# Route pour supprimer un élément
@app.route('/supprimer', methods=['POST'])
def supprimer_element():
    data = request.json
    liste_eleves.remove(data['item'])
    return jsonify({'message': 'Item supprimé !'}), 200

if __name__ == '__main__':
    app.run(debug=False)
