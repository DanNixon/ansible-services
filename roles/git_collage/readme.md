# `dannixon.services.git_collage`

Configures unattended, periodic mirroring of Git repositories via [`git-collage`](https://github.com/DanNixon/git-collage) and a systemd timer.

## Role Variables

The schedule by which mirrors are updated is controlled by `git_collage_update_interval`.
This accepts any valid value for systemd's `OnCalendar` (see `man 5 systemd.timer`).

Repositories and where to mirror them locally are defined using `git_collage_config`.
The configuration is best described via the example below.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    git_collage_update_interval: weekly

    git_collage_config: |
      [providers.source]
      type = 'static_list'

      [[providers.source.repos]]
      git_url = 'https://github.com/dannixon/dotfiles'
      path = 'dotfiles'
      [[providers.source.repos.ref_match.rules]]
      type = 'exact'
      expr = 'refs/heads/main'

      [[providers.source.repos]]
      git_url = 'https://github.com/dannixon/ansible-services'

  roles:
    - dannixon.services.git_collage
```

## License

MIT
