# `dannixon.services.dmrgateway`

[![dannixon.services.dmrgateway](https://github.com/DanNixon/ansible-services/actions/workflows/dmrgateway.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/dmrgateway.yml)

Installs and configures [DMRGateway](https://github.com/g4klx/DMRGateway).

## Role Variables

`dmrgateway_config` sets what should happen if the AUR pacakges are already installed.
It's options are as per the `state` parameter defined [here](https://github.com/kewlfft/ansible-aur#options).

`dmrgateway_config` is the dictionary encoding of the (undocumented) INI configuration file.


## Example Playbook

Note that the value of `dmrgateway_config` does not form a functional configuration.

```yaml
- hosts: all
  become: true

  vars:
    dmrgateway_config:
      General:
        Timeout: 10
      Info:
        Location: Somewhere
      DMR Networl 1:
        Name: BrandMeister IE
        PassAllTG:
          - 1
          - 2
        PassAllPC:
          - 1
          - 2

  roles:
    - dannixon.services.dmrgateway
```

## License

MIT
