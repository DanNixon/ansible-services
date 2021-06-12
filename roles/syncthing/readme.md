# `dannixon.system.syncthing`

[![dannixon.system.syncthing](https://github.com/DanNixon/ansible-services/actions/workflows/syncthing.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/syncthing.yml)

Installs [Syncthing](https://syncthing.net/).

## Role Variables

`syncthing_service` determines if the service starting Syncthing along with the user session should be enabled.

## Example Playbook

```yaml
- hosts: all
  become: true

  roles:
    - dannixon.system.syncthing
```

## License

MIT
