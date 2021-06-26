# `dannixon.services.mmdvmhost`

[![dannixon.services.mmdvmhost](https://github.com/DanNixon/ansible-services/actions/workflows/mmdvmhost.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/mmdvmhost.yml)

Installs and configures [MMDVMHost](https://github.com/g4klx/MMDVMHost).

## Role Variables

`mmdvmhost_package` sets what should happen if the AUR packages are already installed.
It's options are as per the `state` parameter defined [here](https://github.com/kewlfft/ansible-aur#options).

`mmdvmhost_configs` allows for definition of multiple MMDVMHost instances, this can be useful for running multiple modems on the same host.
`name` is a unique identifier for the configuration.
`config` is the dictionary encoding of the (undocumented) INI configuration file.

## Example Playbook

Note that the value of `mmdvmhost_configs` does not form a functional configuration.

```yaml
- hosts: all
  become: true

  vars:
    mmdvmhost_configs:
      - name: main
        config:
          Modem:
            Port: /dev/ttyUSB0
            RFLevel: 5
          DMR:
            ColorCode: 10
          DMR Network:
            Address: 127.0.0.1

  roles:
    - dannixon.services.mmdvmhost
```

## License

MIT
