# `dannixon.services.dnscrypt_proxy`

[![dannixon.services.dnscrypt_proxy](https://github.com/DanNixon/ansible-services/actions/workflows/dnscrypt_proxy.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/dnscrypt_proxy.yml)

Installs and configures [dnscrypt-proxy](https://github.com/DNSCrypt/dnscrypt-proxy).

## Role Variables

The following are simple translations of the appropriate entry in `dnscrypt-proxy.toml`:

  - `dnscrypt_proxy_max_clients`
  - `dnscrypt_proxy_use_ipv6`
  - `dnscrypt_proxy_listen_addresses`
  - `dnscrypt_proxy_require_dnssec`

A list of names may be provided via `dnscrypt_proxy_blocked_names`, for which DNS resolution will be blocked.
This may be used to create PiHole like ad/malware/dark-pattern blocking.
This list populates `blocked-names.txt`.

A list of mappings from names to resolvers my be provided via `dnscrypt_proxy_forwarding_rules`.
This can be useful to ensure resolution of hosts on the immediate LAN work as intended.
This list populates `forwarding-rules.txt`.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    dnscrypt_proxy_forwarding_rules:
      - name: lan
        resolver: 192.168.1.1

  roles:
    - dannixon.services.dnscrypt_proxy
```

## License

MIT
