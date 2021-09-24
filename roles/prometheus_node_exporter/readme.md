# `dannixon.services.prometheus_node_exporter`

[![dannixon.services.prometheus_node_exporter](https://github.com/DanNixon/ansible-services/actions/workflows/prometheus_node_exporter.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/prometheus_node_exporter.yml)

Installs Prometheus [node exporter](https://github.com/prometheus/node_exporter/).

## Example Playbook

```yaml
- hosts: all
  become: true

  roles:
    - dannixon.services.prometheus_node_exporter
```

## License

MIT
