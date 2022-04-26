# `dannixon.services.kea`

Installs and configures [Kea](https://www.isc.org/kea/) DHCP server.

## Role Variables

- `kea_dhcp4_enable`: Enables `kea-dhcp4`, providing IPv4 DHCP.
- `kea_dhcp4_config`: Configures `kea-dhcp4`.
- `kea_dhcp6_enable`: Enables `kea-dhcp6`, providing IPv6 DHCP.
- `kea_dhcp6_config`: Configures `kea-dhcp6`.
- `kea_dhcp_ddns_enable`: Enables `kea-dhcp-ddns`, providing dynamic DNS updates.
- `kea_dhcp_ddns_config`: Configures `kea-dhcp-ddns`.
- `kea_clean_leases`: Removes memfile backed IPv4 and IPv6 leases.

Configuration options are as per the JSON configuration options described [here](https://kea.readthedocs.io/en/latest/arm/config.html).

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    kea_dhcp4_enable: true
    kea_dhcp4_config:
      loggers:
        - name: kea-dhcp4
          severity: DEBUG
          output_options:
            - output: stdout
              pattern: "[%-5p %c] %m\n"

    kea_dhcp_ddns_enable: true
    kea_dhcp_ddns_config:
      loggers:
        - name: kea-dhcp-ddns
          severity: DEBUG
          output_options:
            - output: stdout
              pattern: "[%-5p %c] %m\n"

  roles:
    - dannixon.services.kea
```

## License

MIT
