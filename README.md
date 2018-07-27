# Python cookiecutter api using the `hug` REST framework

> Check out [hug](http://www.hug.rest/). It's basically Flask but much better.


### Deploying and debugging locally

Instructions for xubuntu and similar flavors of linux. These can be easily adapted for mac or windows. If you are running Windows you can install Windows Subsystem for Linux (WSL) and run a Ubuntu
shell inside Windows. [Configure WSL Here](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

Clone this repo and move to directory in terminal console (aka: the working directory should be the root of this repository)

```
sudo apt install -y python3 python3-pip
pip3 install --upgrade pip
pip3 install --user pipenv
cd hug_cookiecutter
pipenv install

pipenv shell
hug -f app.py
```

visit http://`localhost`:8000/health

(localhost could be replaced with `0.0.0.0` or `hostname` or `hostname.guest.corp.microsoft.com` )


## Helpful resources

- https://github.com/timothycrosley/hug