# OpenAPI Parser

This is a simple script in python to fetch and parse the API endpoins which are compatible with OpenAPI.

## Requirements

```pip install requests
$ pip install requests
```

## Usage

```
$ python openapi_parser.py [URL]
```

## Example

```
python3 openapi_parser.py https://petstore.swagger.io/v2/swagger.json
Swagger Version: 2.0
API Title: Swagger Petstore
Version: 1.0.5
Description: This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.
Host: petstore.swagger.io
API Path: /v2
Paths:
	- /pet/{petId}/uploadImage
	- /pet
	- /pet/findByStatus
	- /pet/findByTags
	- /pet/{petId}
	- /store/order
	- /store/order/{orderId}
	- /store/inventory
	- /user/createWithArray
	- /user/createWithList
	- /user/{username}
	- /user/login
	- /user/logout
	- /user
```

