# Cloudflare DYNDNS

Small tool to update a `A` record on cloudflare.


# Installation

Build the docker image
```sh
$ docker build -t cloudflare_dyndns ./
```

You will also need to update the `dyndns.service` file to set the record, domain, and token

Finally add the service file and enable it
```sh
$ sudo ln -s $(pwd)/dyndns.service /etc/systemd/system/dyndns.service
$ sudo ln -s $(pwd)/dyndns.timer /etc/systemd/system/dyndns.timer
$ systemctl enable dyndns.timer
```
