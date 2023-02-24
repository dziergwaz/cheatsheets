import requests
import json

USERNAME = 'dziergwa'
TOKEN = 'njfi32929mdksdfq'
endpoint = "https://pixe.la/v1/users"
parameters = {'token':TOKEN, 'username':USERNAME, 'agreeTermsOfService':'yes', 'notMinor':'yes'}

headers_param = {"X-USER-TOKEN":TOKEN}

#print(f"{endpoint}?token:{parameters['token']}?username:{parameters['username']}?agreeTermsOfService:{parameters['agreeTermsOfService']}?notMinor:{parameters['notMinor']}")
#print(parameters['token'])

## USER CREATE 
#req = requests.post(url=endpoint, json=parameters, verify=False)
#print(req.text, req.status_code)


## GRAPH CREATE
graph_parameters = {"id":"graph1", "name":"lol", "unit":"Km","type":"float","color":"kuro"}
#graph_token = "https://pixe.la/v1/users/a-know/graphs/test-graph"

#graph_endpoint = (f"{endpoint}/{USERNAME}/graphs")
#print(graph_endpoint)

#req = requests.post(url=graph_endpoint, json=graph_parameters, verify=False, headers=headers_param)
#print(req.text, req.status_code)


## GET GRAPH DEFINITION
# /v1/users/<username>/graphs/<graphID>/graph-def - Get a graph definition
#graph_id = "graph1"
#graph_def_endpoint = f"{endpoint}/{USERNAME}/graphs/{graph_id}.html"
#print(graph_def_endpoint)
#
#req = requests.get(url=graph_def_endpoint, headers=headers_param, verify=False)
#print(req, req.status_code)


## POST PIXEL TO THE GRAPH
# /v1/users/<username>/graphs/<graphID>
graph_id = graph_parameters["id"]
req_body = { "date":"20230223", "quantity":"18.65"}
#post_pixel_endpoint = f"{endpoint}/{USERNAME}/graphs/{graph_id}"
#
#req = requests.post(url=post_pixel_endpoint, headers=headers_param, verify=False, json=req_body)
#print(req.status_code)

## GET EXISTING PIXEL
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
#get_pixel_endpoint =  f"{endpoint}/{USERNAME}/graphs/{graph_id}/{req_body['date']}"
#req = requests.get(url=get_pixel_endpoint, headers=headers_param, verify=False)
#print(req.status_code)

## UPDATE / DELETE EXISTING PIXEL
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
req_body2 = { "date":"20230223", "new_data" : {"quantity":"14.55"}}
new_data= {"quantity":"7"}
update_pixel_endpoint =  f"{endpoint}/{USERNAME}/graphs/{graph_id}/{req_body2['date']}"
print(update_pixel_endpoint)

req = requests.put(url=update_pixel_endpoint, headers=headers_param, verify=False, json=req_body2["new_data"]) # json = <dict> NOT str !
print(req.status_code)

