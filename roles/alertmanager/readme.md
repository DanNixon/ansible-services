# `dannixon.services.alertmanager`

[![dannixon.services.alertmanager](https://github.com/DanNixon/ansible-services/actions/workflows/alertmanager.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/alertmanager.yml)

Installs and configures [Prometheus Alertmanager](https://github.com/prometheus/alertmanager/).

## Role Variables

`alertmanager_config` encodes the same data as what would be provided in the [`alertmanager.yml` config file](https://www.prometheus.io/docs/alerting/latest/configuration/#configuration-file).

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    alertmanager_config:
      global:
        resolve_timeout: 5m
        smtp_smarthost: 'smtp.example.com:25'
        smtp_from: 'alertmanager@example.com'

      route:
        group_by:
          - instance
          - severity
        group_wait: 30s
        group_interval: 5m
        repeat_interval: 3h
        receiver: team-1

      receivers:
        - name: team-1
          email_configs:
            - to: 'admin@example.com'

  roles:
    - dannixon.services.alertmanager
```

## License

MIT
