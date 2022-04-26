# `dannixon.services.borg`

Installs and configures backups with [Borg](https://www.borgbackup.org/) and [Borgmatic](https://torsion.org/borgmatic/).

## Role Variables

`borg_borgmatic_user`: the user under which Borgmatic is run.

`borg_borgmatic_config`: the Borgmatic configuration as per [the documentation](https://torsion.org/borgmatic/docs/how-to/set-up-backups/#configuration).

`borg_borgmatic_enable_scheduled_backups`: controls if automatic backups should be enabled (defaults to `false`).

`borg_borgmatic_schedule`: sets the schedule for automatic backups (defaults to `daily`).
See `man 7 systemd.time` for valid values.

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
