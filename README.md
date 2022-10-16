# test_api
* Run both servers;
* server1 - uses Flask, server2 - uses flask-restful
* only server1 will show a meaningful output if used with POST
* tested with Postman
<img width="635" alt="image" src="https://user-images.githubusercontent.com/79509008/196061517-36764b9a-4b2d-4708-afa7-a17c5e94d555.png">

```curl --header "Content-Type: application/json"  --request POST  --data '{"val": 10,"max_val":13}'  http://localhost:5000```
