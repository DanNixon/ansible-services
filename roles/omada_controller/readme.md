# `dannixon.services.omada_controller`

[![dannixon.services.omada_controller](https://github.com/DanNixon/ansible-services/actions/workflows/omada_controller.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/omada_controller.yml)

Installs TP-Link Omada SDN controller via Podman and [this Docker image](https://github.com/mbentley/docker-omada-controller).

## Role Variables

- `omada_controller_version` sets the image tag to use.
- `omada_controller_timezone` sets the site timezone.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    omada_controller_timezone: Europe/London

  roles:
    - dannixon.services.omada_controller
```

## License

MIT
