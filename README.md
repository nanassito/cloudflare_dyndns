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
$ systemctl enable dyndns.service
$ systemctl enable dyndns.timer
```
