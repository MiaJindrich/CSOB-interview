from flask import Flask,jsonify

app = Flask(__name__)

operator_dic = {
    'plus': '+',
    'minus': '-'
}

@app.route('/api/math/<string:query>', methods=['GET'])
def parser(query):
    if 'plus' in query:
        query = query.replace('plus', operator_dic['plus'])
    if 'minus' in query:
        query = query.replace('minus', operator_dic['minus'])
    return jsonify({'result': str(eval(query))})

if __name__ == '__main__':
    app.run(debug=True)