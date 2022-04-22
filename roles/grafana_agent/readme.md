# `dannixon.services.grafana_agent`

Installs and configures [Grafana Agent](https://grafana.com/docs/agent/).

## Role Variables

`grafana_agent_config` is the content of the Grafana Agent config file.

`grafana_agent_deb_url` is the URL of the `.deb` used to install Grafana Agent on Ubuntu.
It can be obtained from the [GitHub releases page](https://github.com/grafana/agent/releases).

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    grafana_agent_config:
      ...

  roles:
    - dannixon.services.grafana_agent
```

## License

MIT
