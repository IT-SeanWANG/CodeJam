#!flask/bin/python

from flask import Flask, jsonify, abort
from flask import make_response
from flask import request

app = Flask(__name__)


#simulated data in list
vnfs = [
    {
        'vnf_id':1,
        'vnf_name': u'vnf01',
        'description': u'vnf03 description'
    },
    {
        'vnf_id':2,
        'vnf_name': u'vnf02',
        'description': u'Test of nvf03 descritption'
    },
    {
        'vnf_id':3,
        'vnf_name': u'vnf03',
        'description': u'this is a test for vnf03'
    }
]


#friendly error feedback
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Sorry, Nothing Found'}),404)


#GET, Get all the VNFs info
@app.route('/todo/api/v1.0/vnfs', methods=['GET'])
def get_vnfs():
    return jsonify({'vnfs': vnfs}), 200


#GET, Get a VNF info
@app.route('/todo/api/v1.0/vnfs/<int:vnf_id>', methods=['GET'])
def get_vnf(vnf_id):
    vnf = filter(lambda t: t['vnf_id'] == vnf_id, vnfs)
    if len(vnf) == 0:
        abort(404)
    return jsonify({'vnf': vnf[0]}), 200


#POST, Create a VNF
@app.route('/todo/api/v1.0/vnfs', methods=['POST'])
def create_vnf():
    if not request.json or not 'vnf_name' in request.json:
        abort(400)

    vnf = {
        'vnf_id': vnfs[-1]['vnf_id'] + 1,
        'vnf_name': request.json['vnf_name'],
        'description': request.json.get('description', "")
    }
    vnfs.append(vnf)
    return jsonify({'vnf': vnf}), 201


#PUT, update a VNF infor
@app.route('/todo/api/v1.0/vnfs/<int:vnf_id>', methods=['PUT'])
def update_vnf(vnf_id):
    vnf = filter(lambda t: t['vnf_id'] == vnf_id, vnfs)
    if len(vnf) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'vnf_name' in request.json and type(request.json['vnf_name']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    vnf[0]['vnf_name'] = request.json.get('vnf_name', vnf[0]['vnf_name'])
    vnf[0]['description'] = request.json.get('description', vnf[0]['description'])
    return jsonify({'vnf': vnf[0]})


#DELETE, del a VNF
@app.route('/todo/api/v1.0/vnfs/<int:vnf_id>', methods=['DELETE'])
def delete_vnf(vnf_id):
    vnf = filter(lambda t: t['vnf_id'] == vnf_id, vnfs)
    if len(vnf) == 0:
        abort(404)

    vnfs.remove(vnf[0])
    return jsonify({'result': True}), 204



if __name__== '__main__':
    app.run(host='0.0.0.0',debug=True)
