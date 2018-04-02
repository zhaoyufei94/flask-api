## 请完成以下几个简单的API：
- [x] 注册
- [x] 登录
- [x] 登出
- [ ] 返回帖子列表
- [x] 返回用户信息
- [ ] 返回站内短信

## 测试：
### 1. 运行
```Shell
$ python main.py
```
### 2. 注册
```Shell
$ curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"pass1"}' http://127.0.0.1:5000/api/register
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 82
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:44:21 GMT

{
  "status": "success",
  "user": {
    "id": 2,
    "username": "user1"
  }
}


$ curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user2","password":"pass2"}' http://127.0.0.1:5000/api/register
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 82
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:45:10 GMT

{
  "status": "success",
  "user": {
    "id": 3,
    "username": "user2"
  }
}


$ curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"pass1"}' http://127.0.0.1:5000/api/register
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 64
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:46:42 GMT

{
  "message": "username already exists",
  "status": "fail"
}
```
### 3. 登录
```Shell
$ curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"pass1"}' http://127.0.0.1:5000/api/login
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 26
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:47:54 GMT

{
  "status": "success"
}


$ curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"wrong"}' http://127.0.0.1:5000/api/login
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 75
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:48:19 GMT

{
  "message": "username and password do not match",
  "status": "fail"
}


$ curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user3","password":"pass3"}' http://127.0.0.1:5000/api/login
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 60
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:48:46 GMT

{
  "message": "user does not exist",
  "status": "fail"
}
```
### 4. 登出
```shell
$ curl -i -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/api/logout/user1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 26
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:50:15 GMT

{
  "status": "success"
}


$ curl -i -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/api/logout/user1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 60
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:50:38 GMT

{
  "message": "user did not log in",
  "status": "fail"
}


$ curl -i -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/api/logout/user3
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 60
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:51:04 GMT

{
  "message": "user does not exist",
  "status": "fail"
}
```
### 5. 获取用户信息
```Shell
$ curl -i -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/api/user/user1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 82
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:52:38 GMT

{
  "status": "success",
  "user": {
    "id": 2,
    "username": "user1"
  }
}

$ curl -i -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/api/user/user3
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 60
Server: Werkzeug/0.14.1 Python/2.7.14
Date: Mon, 02 Apr 2018 05:53:06 GMT

{
  "message": "user does not exist",
  "status": "fail"
}
```
