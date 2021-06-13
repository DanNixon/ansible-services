# `dannixon.services.git_mirror`

[![dannixon.services.git_mirror](https://github.com/DanNixon/ansible-services/actions/workflows/git_mirror.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/git_mirror.yml)

Configures unattended, periodic mirroring of Git repositories via a simple shell script and a systemd timer.

## Role Variables

The schedule by which mirrors are updated is controlled by `git_mirror_update_interval`.
This accepts any valid value for systemd's `OnCalendar` (see `man 5 systemd.timer`).

Repositories and where to mirror them locally are defined using `git_mirror_config`.
The configuration is best described via the example below.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    git_mirror_update_interval: weekly

    git_mirror_config:
      - directory: /var/srv/git/mirrors
        repositories:
          - name: ansible-services
            url: https://github.com/DanNixon/ansible-services.git

  roles:
    - dannixon.services.git_mirror
```

## License

MIT
