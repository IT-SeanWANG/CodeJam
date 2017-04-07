#! /usr/bin/env python
# coding: utf-8
import pecan
import json
import copy
from pecan import abort, expose
from pecan.rest import RestController
from pecan import rest, response ,request
from pecan.jsonify import jsonify


vnfs_list = [
    {"vnf_id": 1, "vnf_name": "vnf01", "vnf_desc": "test1"},
    {"vnf_id": 2, "vnf_name": "vnf02", "vnf_desc": "test2"},
    {"vnf_id": 3, "vnf_name": "vnf03", "vnf_desc": "test3"}
    ]
vnfs_detail = [
    {"vnf_id": 1, "vnf_load": "R17"},
    {"vnf_id": 2, "vnf_load": "R18"},
    {"vnf_id": 3, "vnf_load": "R19"}
    ]


class vnfsController(RestController):
    # HTTP GET /{id}
    @pecan.expose("json")
    def get_one(self,vnf_id):
        vnf = filter(lambda t: t["vnf_id"] ==int(vnf_id)  , vnfs_list)
        vnf_detail = filter(lambda t: t["vnf_id"] == int(vnf_id), vnfs_detail)

        if len(vnf) == 0:
            abort(404)
        if len(vnf_detail) == 0:
            abort(404)

        vnf_ret = copy.deepcopy(vnf)
        vnf_ret[0]['vnf_load'] = vnf_detail[0]['vnf_load']

        response.status=200

        return vnf_ret[0]

    # HTTP GET /
    @expose(generic=True, template='json')
    def index(self):
        response.status=200
        return vnfs_list

    # HTTP POST /
    #curl -i -H "Content-Type: application/json" -X POST -d '''{"vnf_id":4,"vnf_name":"vnf04","vnf_desc":"test4"}''' http://localhost:5080/vnfs/
    @index.when(method='POST', template='json')
    def index_POST(self):
        #print "index_post==================="
        if not request.json or not 'vnf_name' in request.json or not 'vnf_desc' in request.json or not'vnf_id'in request.json:
            abort(400)

        vnf = {
            'vnf_id': request.json['vnf_id'],
            'vnf_name': request.json['vnf_name'],
            'vnf_desc': request.json['vnf_desc']
        }

        # if vnfid == input already exist, remove it in list and remove vnf_detail
        for item in vnfs_list:
            if item['vnf_id'] == request.json['vnf_id']:
                vnfs_list.remove(item)
                break

        for item in vnfs_detail:
            if item['vnf_id'] == request.json['vnf_id']:
                vnfs_detail.remove(item)
                break

        vnf_detail = {
        'vnf_id': request.json['vnf_id'],
        "vnf_load": "R17"
        }

        vnfs_list.append(vnf)
        vnfs_detail.append(vnf_detail)
        print vnf
        response.status=201
        return

    #curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5080/vnfs/2
    @pecan.expose()
    def delete(self,vnf_id):
        vnf = filter(lambda t: t['vnf_id'] == int(vnf_id), vnfs_list)
        if len(vnf) == 0:
            abort(404)
        vnfs_list.remove(vnf[0])

        vnf_detail = filter(lambda t: t['vnf_id'] == int(vnf_id), vnfs_detail)
        if len(vnf_detail) == 0:
            abort(404)
        vnfs_detail.remove(vnf_detail[0])

        response.status = 204
        return

