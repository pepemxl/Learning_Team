# Node JS

- Estaremos usando la version LTS 14.15.4
- Usaremos nvm para instalar las versiones de node que necesitemos.

## Instalar NVM

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
```

En caso de tener un error de certificados podemos agregar `-k` o `--insecure`

```bash
% curl -k -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 13527  100 13527    0     0  72725      0 --:--:-- --:--:-- --:--:-- 72725
=> Downloading nvm from git to '/Users/pepe/.nvm'
=> Cloning into '/Users/pepe/.nvm'...
remote: Enumerating objects: 333, done.
remote: Counting objects: 100% (333/333), done.
remote: Compressing objects: 100% (283/283), done.
remote: Total 333 (delta 38), reused 150 (delta 25), pack-reused 0
Receiving objects: 100% (333/333), 177.15 KiB | 991.00 KiB/s, done.
Resolving deltas: 100% (38/38), done.
=> Compressing and cleaning up git repository

=> Appending nvm source string to /Users/pepe/.bash_profile
=> Appending bash_completion source string to /Users/pepe/.bash_profile
=> Close and reopen your terminal to start using nvm or run the following to use it now:

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

Como las instrucciones dicen hay que agregar la variable de entorno y cargar nvm, modificando en el caso de MAC el archivo `.zshrc` o en linux `.bash_profile`.


Finalmente especificamos la version que debe utilizar con 

`nvm use 14.15.4`

posiblemente obtengamos el siguiemte mensaje:

```
% nvm use 14.15.4
N/A: version "14.15.4 -> N/A" is not yet installed.

You need to run "nvm install 14.15.4" to install it before using it.
```

en este caso tenemos problemas con los certificados, podemos arreglar los certificados de curl, o modificar `nvm.sh` para que haga conexiones inseguras al CA correspondiente.

```
nvm install 14.15.4
Downloading and installing node v14.15.4...
Downloading https://nodejs.org/dist/v14.15.4/node-v14.15.4-darwin-x64.tar.xz...
################################################################################################################################################## 100,0%
Computing checksum with sha256sum
Checksums matched!
Now using node v14.15.4 (npm v6.14.10)
Creating default alias: default -> 14.15.4 (-> v14.15.4)
```

```
nvm use 14.15.4
Now using node v14.15.4 (npm v6.14.10
```



### `asdf` como una alternativa a nvm

Instalamos `asdf`:

`brew install asdf`
`brew install gpg gawk`

asdf is a multi-language version manager with a nodejs plugin. After installing asdf for your OS/package manager/shell, run the following commands to set up nodejs.


```
asdf plugin add nodejs
initializing plugin repository...Cloning into '/Users/pepe/.asdf/repository'...
remote: Enumerating objects: 3585, done.
remote: Counting objects: 100% (779/779), done.
remote: Compressing objects: 100% (543/543), done.
remote: Total 3585 (delta 456), reused 476 (delta 232), pack-reused 2806
Receiving objects: 100% (3585/3585), 815.27 KiB | 1.12 MiB/s, done.
```


## Yarn

```
npm install --global yarn 

> yarn@1.22.17 preinstall /Users/pepe/.nvm/versions/node/v14.15.4/lib/node_modules/yarn
> :; (node ./preinstall.js > /dev/null 2>&1 || true)

/Users/pepe/.nvm/versions/node/v14.15.4/bin/yarn -> /Users/pepe/.nvm/versions/node/v14.15.4/lib/node_modules/yarn/bin/yarn.js
/Users/pepe/.nvm/versions/node/v14.15.4/bin/yarnpkg -> /Users/pepe/.nvm/versions/node/v14.15.4/lib/node_modules/yarn/bin/yarn.js
+ yarn@1.22.17
added 1 package in 1.639s
```









