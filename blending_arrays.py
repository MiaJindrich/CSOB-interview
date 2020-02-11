from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

def blend(*args):
    array_list = []
    for array in args:
        array_list.append(array)

    blended_array = []
    x = 0
    for i in range(len(max(array_list, key=len))):
        for array in array_list:
            try:
                value = array[x]
            except IndexError:
                value = None
            blended_array.append(value)
        x += 1

    return blended_array

@app.route('/api/blend_arrays', methods=['POST'])
def blend_arrays():
    if not request.json or not 'arrays' in request.json:
        abort(400)
    if not isinstance(request.json['arrays'], list):
        abort(400)
    list_arrays = request.json['arrays']
    return jsonify(blend(*list_arrays))
    
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

if __name__ == '__main__':
    app.run(debug=True)