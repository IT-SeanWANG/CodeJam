#! /usr/bin/env python
# coding: utf-8
# note : default server:port 127.0.0.1:5000
# GET : curl -i http:///vnfs/2localhost:5000
# POST : curl -i -H "Content-Type: application/json" -X POST -d '''{"vnf_name":"vnf04","vnf_desc":"test4"}''' http://localhost:5000/vnfs
# DELETE : curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/vnfs/2


from flask import Flask
from flask import request, Response, abort
from flask import make_response
from flask import jsonify

vnfs = [{"vnf_id": 1, "vnf_name": "vnf01", "vnf_desc": "test1"},
        {"vnf_id": 2, "vnf_name": "vnf02", "vnf_desc": "test2"},
        {"vnf_id": 3, "vnf_name": "vnf03", "vnf_desc": "test3"}]

vnfs_detail = [{"vnf_id": 1, "vnf_load": "R17"},
               {"vnf_id": 2, "vnf_load": "R18"},
               {"vnf_id": 3, "vnf_load": "R19"}]

app = Flask(__name__)

@app.route('/vnfs', methods=['GET'])
def get_vnfs():
    return jsonify({'vnfs': vnfs}), 200

# curl -i http://localhost:5000/vnfs/2
@app.route('/vnfs/<int:vnf_id>', methods=['GET'])
def get_vnf(vnf_id):
    vnf = filter(lambda t: t['vnf_id'] == vnf_id, vnfs)
    vnf_detail=filter(lambda t: t['vnf_id'] == vnf_id,vnfs_detail)

    if len(vnf) == 0:
        abort(404)
    if len(vnf_detail) ==0:
        abort(404)

    vnf[0]['vnf_load'] = vnf_detail[0]['vnf_load']
    vnf_ret= vnf[0]
    return jsonify({'vnf': vnf_ret}), 200
#######################################
# curl -i -H "Content-Type: application/json" -X POST -d '''{"vnf_id":4,"vnf_name":"vnf04","vnf_desc":"test4"}''' http://localhost:5000/vnfs

@app.route('/vnfs', methods=['POST'])
def create_vnf():
    if not request.json or not 'vnf_name' in request.json or not 'vnf_desc' in request.json or not'vnf_id'in request.json:
        abort(400)

    vnf_detail = {
        'vnf_id': request.json['vnf_id'],
        "vnf_load": "R17"
    }


    vnf = {
        'vnf_id': request.json['vnf_id'],
        'vnf_name': request.json['vnf_name'],
        'vnf_desc': request.json['vnf_desc']
    }

    for item in vnfs:
        if item['vnf_id'] == request.json['vnf_id']:
            vnfs.remove(item)
            break

    for item in vnfs_detail:
        if item.has_key(request.json['vnf_id']):
            vnfs_detail.remove(item)
            break

    vnfs_detail.append(vnf_detail)
    vnfs.append(vnf)
    print vnf
    return '', 201

#curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/vnfs/2
@app.route('/vnfs/<int:vnf_id>', methods=['DELETE'])
def delete_vnf(vnf_id):
    vnf = filter(lambda t: t['vnf_id'] == vnf_id, vnfs)
    if len(vnf) == 0:
        abort(404)
    vnfs.remove(vnf[0])

    vnf_detail = filter(lambda t: t['vnf_id'] == vnf_id, vnfs_detail)
    if len(vnf) == 0:
        abort(404)
    vnfs_detail.remove(vnf_detail[0])
    return '', 204

if __name__ == '__main__':
    app.run()
