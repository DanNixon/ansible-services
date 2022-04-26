# `dannixon.services.syncthing`

Installs [Syncthing](https://syncthing.net/).

## Role Variables

`syncthing_service` determines if the service starting Syncthing along with the user session should be enabled.

## Example Playbook

```yaml
- hosts: all
  become: true

  roles:
    - dannixon.services.syncthing
```

## License

MIT
