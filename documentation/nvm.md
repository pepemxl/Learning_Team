# Install NVM

NVM es una herramienta que nos permite manejar que version de node queremos usar mediante un CLI.

## Linux

En este caso probaremos sobre una version Ubuntu 20.04.3 LTS.

Si no cuentas con `curl` instalamos `curl` con:

```bash
sudo apt install curl 
```


despues bajamos el script de instalacion de nvm

```bash
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
```

lo cual te generara una salida como la siguiente:

```bash
$ curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 15462  100 15462    0     0  50695      0 --:--:-- --:--:-- --:--:-- 50529
=> Downloading nvm from git to '/home/username/.nvm'
=> Cloning into '/home/username/.nvm'...
remote: Enumerating objects: 354, done.
remote: Counting objects: 100% (354/354), done.
remote: Compressing objects: 100% (302/302), done.
remote: Total 354 (delta 40), reused 156 (delta 27), pack-reused 0
Receiving objects: 100% (354/354), 206.98 KiB | 5.75 MiB/s, done.
Resolving deltas: 100% (40/40), done.
* (HEAD detached at FETCH_HEAD)
  master
=> Compressing and cleaning up git repository

=> Appending nvm source string to /home/pepe/.bashrc
=> Appending bash_completion source string to /home/pepe/.bashrc
=> Close and reopen your terminal to start using nvm or run the following to use it now:

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

entonces reactivamos la venta para poder usar nvm:

```bash
source ~/.profile
```

veras una salida similar a 

```bash
$ nvm

Node Version Manager (v0.39.1)

Note: <version> refers to any version-like string nvm understands. This includes:
  - full or partial version numbers, starting with an optional "v" (0.10, v0.1.2, v1)
  - default (built-in) aliases: node, stable, unstable, iojs, system
  - custom aliases you define with `nvm alias foo`
...
```


con ello ya sabemos que esta bien instalado

para instalad node basta con 

```bash
$ nvm install node
Downloading and installing node v17.3.0...
Downloading https://nodejs.org/dist/v17.3.0/node-v17.3.0-linux-x64.tar.xz...
############################################################################################################# 100.0%
Computing checksum with sha256sum
Checksums matched!
Now using node v17.3.0 (npm v8.3.0)
Creating default alias: default -> node (-> v17.3.0)
```
en este caso se instalo la ultima version disponible, si deseamos una version especifica

```bash
nvm install 12.18.3 
```

recuerda que la primer version que instales se volvera tu version por defecto.



Para poder listar las versiones que se encuentran instaladas en tu sistema usamos el comando `nvm ls`.


Para poder ver que versiones se encuentran disponibles usamos el comando `nvm ls-remote`, al momento de escribir este documento tenemos la siguiente lista recortada de versiones disponibles:

```bash
$ nvm ls-remote
        v0.1.14
        v0.1.15
        v0.1.16
        v0.1.17
        v0.1.18
        v0.1.19
        v0.1.20
...
v16.12.0
       v16.13.0   (LTS: Gallium)
       v16.13.1   (Latest LTS: Gallium)
        v17.0.0
        v17.0.1
        v17.1.0
        v17.2.0
        v17.3.0
```

siempre se recomienda usar la ultima version LTS, que en este caso seria la version v16.13.1.

Procederemos a instalar esta version:

```bash
nvm install v16.13.1
Downloading and installing node v16.13.1...
Downloading https://nodejs.org/dist/v16.13.1/node-v16.13.1-linux-x64.tar.xz...
############################################################################################################# 100.0%
Computing checksum with sha256sum
Checksums matched!
Now using node v16.13.1 (npm v8.1.2)
```

Listando las versiones del sistema podemos contastar

```bash
 nvm ls
->     v16.13.1
        v17.3.0
         system
default -> node (-> v17.3.0)
iojs -> N/A (default)
unstable -> N/A (default)
node -> stable (-> v17.3.0) (default)
stable -> 17.3 (-> v17.3.0) (default)
lts/* -> lts/gallium (-> v16.13.1)
lts/argon -> v4.9.1 (-> N/A)
lts/boron -> v6.17.1 (-> N/A)
lts/carbon -> v8.17.0 (-> N/A)
lts/dubnium -> v10.24.1 (-> N/A)
lts/erbium -> v12.22.8 (-> N/A)
lts/fermium -> v14.18.2 (-> N/A)
lts/gallium -> v16.13.1
```

que la version actual es la v16.13.1 pero la version por defecto es la v17.3.0.
Igual otra manera simple de hacer lo mismo es tan solo preguntarle a node que version esta activa con `node --version`:

```bash
$ node --version
v16.13.1
```

para cambiar de version basta con usar el comando `nvm use v17.3.0`

```bash
$ nvm use v17.3.0
Now using node v17.3.0 (npm v8.3.0)
```

verificando version

```bash 
$ node --version
v17.3.0
```

para saber cual es la version por defecto en nvm usamos `nvm run default --version`:

```bash
$ nvm run default --version 
Running node v17.3.0 (npm v8.3.0)
v17.3.0
```

Ahora que si desemos correr una version especifica usamos el commando `nvm exec <version> server.js` solo debemos asegurarnos que dicha versiones este instalada, y si no instalarlar previamente:

```bash
nvm install v14.18.2 
nvm exec v14.18.2 server.js
```



