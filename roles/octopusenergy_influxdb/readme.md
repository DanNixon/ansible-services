# `dannixon.services.octopusenergy_influxdb`

[![dannixon.services.octopusenergy_influxdb](https://github.com/DanNixon/ansible-services/actions/workflows/octopusenergy_influxdb.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/octopusenergy_influxdb.yml)

Installs and configures [octopusenergy-influxdb](https://github.com/FileGo/octopusenergy-influxdb/).

## Role Variables

`octopusenergy_influxdb_repo` and `octopusenergy_influxdb_revision` set the version of the tool that is installed.
By default they install my slightly [custom version](https://github.com/DanNixon/octopusenergy-influxdb/tree/custom), this is required to pick up the config file from the correct location.

`octopusenergy_influxdb_time_period` sets the frequency of updates.
Accepts any valid option that can be given to `OnCalendar` (see `man 5 systemd.timer`).
Defaults to every morning at 2AM.

`octopusenergy_influxdb_config` encodes the configuration for the tool.
See the [docs](https://github.com/FileGo/octopusenergy-influxdb#configuration) for details.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    octopusenergy_influxdb_config:
      octopusenergy:
        token: nope

      influxdb:
        url: http://localhost:8086
        org: Utility
        database: octopusenergy
        token: nope

      electricity:
        mpan: nope
        serial: nope

      gas:
        mpan: nope
        serial: nope
        type: smets1

  roles:
    - dannixon.services.octopusenergy_influxdb
```

## License

MIT
