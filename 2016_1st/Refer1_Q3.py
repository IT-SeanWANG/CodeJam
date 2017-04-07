from flask import Flask, jsonify, abort, request

app = Flask(__name__)

vnf_nodes = [
    {
        'vnf_id': 1,
        'vnf_name': u'vnf01',
        'vnf_desc': u'test1', 
        'vnf_load': u'R17'
    },
    {
        'vnf_id': 2,
        'vnf_name': u'vnf02',
        'vnf_desc': u'test2', 
        'vnf_load': u'R18'
    },
	{
        'vnf_id': 3,
        'vnf_name': u'vnf03',
        'vnf_desc': u'test3', 
        'vnf_load': u'R19'
    }
]

@app.route('/vnfs', methods=['GET'])
def get_vnfs():
    return jsonify({'vnf_nodes': vnf_nodes})

@app.route('/vnfs/<int:vnf_id>', methods=['GET'])
def get_vnf(vnf_id):
    v_node = filter(lambda t: t['vnf_id'] == vnf_id, vnf_nodes)
    if len(v_node) == 0:
        abort(404)
    return jsonify({'v_node': v_node[0]})

@app.route('/vnfs', methods=['POST'])


def create_vnf():
	if not request.json or not 'vnf_id' in request.json or not 'vnf_name' in request.json or not 'vnf_desc' in request.json:
		abort(400)
	v_node = {
        'vnf_id': request.json['vnf_id'],
        'vnf_name': request.json['vnf_name'],
        'vnf_desc': request.json['vnf_desc'],
        'vnf_load': request.json['vnf_load']
    }
	vnf_nodes.append(v_node)
	for v_node in vnf_nodes:
		print v_node
	return jsonify({'v_node': v_node}), 201

@app.route('/vnfs/<int:vnf_id>', methods=['DELETE'])
def delete_vnf(vnf_id):
    v_node = filter(lambda t: t['vnf_id'] == vnf_id, vnf_nodes)
    if len(v_node) == 0:
        abort(404)
    vnf_nodes.remove(v_node[0])
    return 204

if __name__ == '__main__':
    app.run(host='0.0.0.0')