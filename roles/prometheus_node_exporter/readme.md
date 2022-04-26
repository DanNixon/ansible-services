# `dannixon.services.prometheus_node_exporter`

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
