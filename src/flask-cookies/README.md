# What are Cookies?

Cookies or better, HTTP Cookies are text files, stored on the Client Machine. Each cookie can be stored permanently or for a specific expiry time based on the Client Browser’s cookie settings.

After the Cookie reaches its expiry date and time, it is automatically removed from the Client Browser.

Cookies present on the Client-side tracks and remember the user’s activity on the web. This information is later used to improve the user’s overall Site experience.


## How do cookies work?

As we know, HTTP is a stateless protocol, which means that the server can’t distinguish whether a user is visiting the site for the first time or not. So to solve this problem, sites use cookies.

Therefore, when a Client visits a particular site for the first time, the client will not have any cookies set by the site. So the server creates a **new cookie** and sends it to the Client machine itself.

So in the next subsequent visits, the client machine will attach the cookie to the request and send it. The server then retrieves the cookies from the request object and uses that cookie information to improve the site’s user experience.

## Setting Flask Cookies

In Flask, Cookies are set on the response object. That is, the server sends the Cookie to the user along with the response.

We do it using the `make_response()` function. Once the response is set, we use the `set_cookie()` function to attach the cookie to it.

```python
response.set_cookie('<Title>','<Value>','<Expiry Time>')
```

```python
@app.route('/setcookie')
def setcookie():
    resp = make_response(f"The Cookie has been set")
    resp.set_cookie('Name','AskPython')
    return resp
```

Now we need to get the Cookie back from the user. The cookie is sent back along with the Request to the server. We Retrieve it using the `request.cookies.get()` function.


```python
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('Name', None)
    return f"The Site : {name}"
```
A complete application using cookies in flask would look like this:

```python
from flask import Flask, make_response, request
 
app = Flask(__name__)
 
@app.route('/setcookie')
def setcookie():
    resp = make_response(f"The Cookie has been Set")
    resp.set_cookie('SiteName','Learning Team')
    return resp
 
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('SiteName')
    return f"The Site : {name}"
 
app.run(host='localhost', port=5000)
```

The DDL in chrome cookies structure is

```sql
CREATE TABLE cookies (
    creation_utc       INTEGER NOT NULL,
    top_frame_site_key TEXT    NOT NULL,
    host_key           TEXT    NOT NULL,
    name               TEXT    NOT NULL,
    value              TEXT    NOT NULL,
    encrypted_value    BLOB    DEFAULT '',
    path               TEXT    NOT NULL,
    expires_utc        INTEGER NOT NULL,
    is_secure          INTEGER NOT NULL,
    is_httponly        INTEGER NOT NULL,
    last_access_utc    INTEGER NOT NULL,
    has_expires        INTEGER NOT NULL
                               DEFAULT 1,
    is_persistent      INTEGER NOT NULL
                               DEFAULT 1,
    priority           INTEGER NOT NULL
                               DEFAULT 1,
    samesite           INTEGER NOT NULL
                               DEFAULT -1,
    source_scheme      INTEGER NOT NULL
                               DEFAULT 0,
    source_port        INTEGER NOT NULL
                               DEFAULT -1,
    is_same_party      INTEGER NOT NULL
                               DEFAULT 0,
    UNIQUE (
        top_frame_site_key,
        host_key,
        name,
        path
    )
);

```


We can customize:

```python
set_cookie( _key_ , _value = '', _max_age = None_ , _expires = None_ , _path = '/'_ , _domain = None_ , _secure = False_ , _httponly = False_ , _samesite = None_ )
```

```python


```
