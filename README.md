# Cloudflare DYNDNS

Small tool to update a `A` record on cloudflare.


# Installation

Build the docker image
```sh
$ docker build -t cloudflare_dyndns ./
```

Add the service file and enable it
```sh
$ sudo ln -s ./dyndns.service /etc/systemd/system/dyndns.service
$ systemctl enable dyndns.timer
```