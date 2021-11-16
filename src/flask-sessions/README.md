# What are Sessions?

Sessions function similar to Flask cookies except that these are stored on the server.

A Session is basically the time duration for which the user was logged in the server. The data that’s tracked during the entire session is what is stored in the server.

Each session has a Session ID (encrypted with a secret key). Sessions use a unique id to retrieve the stored values. Whenever a session is created, a cookie containing the unique session id is stored on the user’s computer, and it is returned with every request to the server.

When the user re-visits the site, he returns the Cookie containing the session ID. The server then reads the session ID and retrieves the corresponding session data.


Saving data in the form of a cookie on the Client-Side is in general not a good idea. Some of the other threats are:

1. Hackers can send a fake cookie and login as another user to hack the site.
2. Storing sensitive data like user passwords etc. in cookies is not secure.
3. We can store only a limited amount of data in cookies since most browsers don’t allow more than 4kb of data.

## Sessions in Flask

In Flask a dictionary object called session object is used to track the session data.


To set a session:

```python
session['<title>'] = value
```
To delete a session:
```python
session.pop('<title>', None)
```

```python

```



