# `dannixon.services.dapnetgateway`

[![dannixon.services.dapnetgateway](https://github.com/DanNixon/ansible-services/actions/workflows/dapnetgateway.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/dapnetgateway.yml)

Installs and configures [DAPNETGateway](https://github.com/g4klx/DAPNETGateway).

## Role Variables

`dapnetgateway_package` sets what should happen if the AUR pacakges are already installed.
It's options are as per the `state` parameter defined [here](https://github.com/kewlfft/ansible-aur#options).

`dapnetgateway_config` is the dictionary encoding of the (undocumented) INI configuration file.

## Example Playbook

Note that the value of `dapnetgateway_config` does not form a functional configuration.

```yaml
- hosts: all
  become: true

  vars:
    dapnetgateway_config:
      General:
        Callsign: n0call
      Log:
        FileLevel: 1
      DAPNET:
        Address: dapnet.auf.rwth-aachen.de
        Port: 43434

  roles:
    - dannixon.services.dapnetgateway
```

## License

MIT
