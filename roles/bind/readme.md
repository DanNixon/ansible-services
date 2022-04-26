# `dannixon.services.bind`

Installs and configures ISC [BIND](https://www.isc.org/bind/) DNS server.

## Role Variables

rndc key generation:

  - `bind_rndc_generate_key` (boolean): should a key be generated for rndc/ddns
  - `bind_rndc_key_path` (string): path to generated rndc key

BIND configuration (`named.conf`):

  - `bind_include_files` (list of string): list of paths to files to be included
  - `bind_log_channels` (list of dict): list of log channels (see example)
  - `bind_log_categories` (list of dict): list of log category/channel mappings (see example)
  - `bind_acls` (list of dict): list of ACLs (see example)
  - `bind_options` (dict): options, accepts any values possible in `options` block (see `man 5 named.conf`)
  - `bind_views` (list of dict): list of views (see example)

Zones:

  - `bind_update_zones` (boolean): write zone files (overwrites server version and removes journal if changed on the server, e.g. via DDNS updates)
  - `bind_zones` (list of dict): list of zones (see example)

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    bind_acls:
      - name: internal_allowlist
        entries:
          - localhost
          - 10.1.10.0/24

      - name: guest_allowlist
        entries:
          - 10.1.11.0/24

    bind_options:
      directory: /var/named
      pid-file: /run/named/named.pid

      listen-on:
        - any
      listen-on-v6:
        - any

      allow-query:
        - internal_allowlist
        - guest_allowlist
      allow-query-cache:
        - internal_allowlist
        - guest_allowlist
      allow-recursion:
        - internal_allowlist
        - guest_allowlist
      allow-transfer:
        - none
      allow-update:
        - none

      querylog: true

      version: none
      hostname: none
      server-id: none

    bind_views:
      - name: internal
        match_clients:
          - internal_allowlist
        zones:
          - name: internal_fwd
            type: primary
            file: internal_fwd.zone
            allow-update:
              - key rndc-key

      - name: guest
        match_clients:
          - guest_allowlist
        zones:
          - name: guest_fwd
            type: primary
            file: guest_fwd.zone
            allow-update:
              - key rndc-key

    bind_zones:
      - filename: internal_fwd.zone
        soa:
          domain: internal.example.com.
        origin: internal.example.com.
        records:
          - type: A
            record: 10.1.10.1
          - type: NS
            record: ns
          - name: ns
            type: A
            record: 10.1.10.1
          - name: somehost
            type: A
            record: 10.1.10.20

      - filename: guest_fwd.zone
        soa:
          domain: guest.example.com.
        origin: guest.example.com.
        records:
          - type: A
            record: 10.1.11.1
          - type: NS
            record: ns
          - name: ns
            type: A
            record: 10.1.11.1

  roles:
    - dannixon.services.bind
```

## License

MIT
