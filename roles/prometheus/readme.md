# `dannixon.services.prometheus`

[![dannixon.services.prometheus](https://github.com/DanNixon/ansible-services/actions/workflows/prometheus.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/prometheus.yml)

Installs and configures [Prometheus](https://prometheus.io/).

## Role Variables

`prometheus_config` encodes the same data as what would be provided in the `prometheus.yml` config file.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    prometheus_config:
      global:
        scrape_interval: 15s

  roles:
    - dannixon.services.prometheus
```

## License

MIT
