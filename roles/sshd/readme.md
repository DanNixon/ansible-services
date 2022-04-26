# `dannixon.services.sshd`

Installs [OpenSSH](https://www.openssh.com/) server with some very basic configuration.

## Example Playbook

```yaml
- hosts: all
  become: true

  roles:
    - dannixon.services.sshd
```

## License

MIT
