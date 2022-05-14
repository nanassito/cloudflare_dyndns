# Cloudflare DYNDNS

Small tool to update a `A` record on cloudflare.


# Installation

Build the docker image
```sh
$ docker build -t cloudflare_dyndns ./
```

Add the service file and enable it
```sh
$ sudo ln -s $(pwd)/dyndns.service /etc/systemd/system/dyndns.service
$ sudo ln -s $(pwd)/dyndns.timer /etc/systemd/system/dyndns.timer
$ systemctl enable dyndns.timer
```