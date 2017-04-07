## test IDE: python 2.7 & pecan 1.12
### Setup test IDE：
1. Use Pecan web framework to implement restful APIs. Create a Pecan project;
2. Copy Q3.py to the folder 'controllers' of pecan project;
3. Modify root.py under folder 'controllers':

    Add：import Q3
    
    Add to 'class RootController(object)'：vnfs = Q3.vnfsController()

### Test procedure:
#### Windows:
1. cmd
2. cd pecanrest
3. python setup.py develop
4. pecan serve config.py
launch webservice, show info as bellow at terminal window:
Starting server in PID 7252
serving on 0.0.0.0:8080, view at http://127.0.0.1:8080/

Test case list as bellow:
1. IE Enter:   http://127.0.0.1:8080/vnfs
2. IE Enter:   http://127.0.0.1:8080/vnfs/1
3. cmd in windows terminal and enter:

curl -i -H "Content-Type: application/json" -X POST -d'''{"vnf_id":4,"vnf_name":"vnf04","vnf_desc":"test4"}'''http://localhost:8080/vnfs/
4. cmd in window terminal, enter:    curl -i -H "Content-Type:application/json" -X DELETE http://localhost:8080/vnfs/2
