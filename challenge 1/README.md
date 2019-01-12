# How to access the endpoit:
The endpoint can be accessed at https://timgrob/messages/ and has a GET and a POST request endpoint

## GET Request:
In order to fetch a previously added sha256 code send a GET request to:
https://timgrob/messages/?sha=<SHA256>

## POST Request:
In order to post a message to the API, send a POST request to:
https://timgrob/messages/

The body of the POST request needs to look the following:
{"message": "foo"}


# What would the bottleneck be of the application? And how do you scale the microservice? 
In such a simple webservice, reading from the database and writing into the database will be the bottleneck if the number of
requets increases. In order to improve the webservice, a streaming layer needs to be implemented where the vast number of
requests can be processed. This can either be done through a data stream or an intermediate cache layer, where the requests 
will be parked for the time being. 


# How did I deploy the application? And why did I chose this way?
I deployed the application onto my PHP server, which I already had available. This was mainly the reason why I chose PHP as
my programming language. I deployed the application via the depolyment application service of my hosting provider, which is a
very manual process. 
If this had been a larger project, I would have used a deployment tool e.g. Jenkings or CircleCi, which runs all the tests 
whenever new code is commited to the porject and can also automatically deploy releases. 
