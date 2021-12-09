# `dannixon.services.borg`

[![dannixon.services.borg](https://github.com/DanNixon/ansible-services/actions/workflows/borg.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/borg.yml)

Installs and configures backups with [Borg](https://www.borgbackup.org/) and [Borgmatic](https://torsion.org/borgmatic/).

## Role Variables

`borg_borgmatic_user`: the user under which Borgmatic is run.

`borg_borgmatic_config`: the Borgmatic configuration as per [the documentation](https://torsion.org/borgmatic/docs/how-to/set-up-backups/#configuration).

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    borg_borgmatic_user: offsite_backup
    borg_borgmatic_config:
      location:
        source_directories:
          - /some/data
          - /some/more/data
        repositories:
          - somewhere
      storage:
        encryption_passcommand: pass offsite_backup_passphrase
      retention:
        keep_within: 6m

  roles:
    - dannixon.services.borg
```

## License

MIT
