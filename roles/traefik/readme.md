# `dannixon.services.traefik`

Installs and configures [Traefik](https://traefik.io/).

## Role Variables

`traefik_static_config` encodes the data for the static configuration, usually found in `traefil.yml`.
Note that dynamic configuration loading is aleady configured by this role so does not need to be included in `traefik_static_config`.

`traefik_dynamic_configs` encodes the dynamic configurations.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    traefik_static_config:
      entryPoints:
        web:
          address: ":80"
          http:
            redirections:
              entryPoint:
                to: websecure
                scheme: https
                permanent: true
        websecure:
          address: ":443"

    traefik_dynamic_configs:
      - name: test
        conf:
          tls:
            certificates:
              - certFile: cert.pem
                keyFile: key.pem
          http:
            routers:
              first:
                entryPoints:
                  - websecure
                tls: {}
                rule: "Host(`example.com`)"
                service: first

            services:
              first:
                loadBalancer:
                  servers:
                    - url: http://srv1.backend.example.com
                    - url: http://srv2.backend.example.com

  roles:
    - dannixon.services.traefik
```

## License

MIT
