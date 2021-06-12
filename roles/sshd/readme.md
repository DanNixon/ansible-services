# `dannixon.system.sshd`

[![dannixon.system.sshd](https://github.com/DanNixon/ansible-services/actions/workflows/sshd.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/sshd.yml)

Installs [OpenSSH](https://www.openssh.com/) server with some very basic configuration.

## Example Playbook

```yaml
- hosts: all
  become: true

  roles:
    - dannixon.system.sshd
```

## License

MIT
