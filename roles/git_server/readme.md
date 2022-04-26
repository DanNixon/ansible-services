# `dannixon.services.git_server`

Configures a basic Git server with SSH access following the principle described [here](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server).

## Role Variables

`git_server_path` defines the path to the directory in which Git repositories are to be stored.

The list of public SSH keys for users are provided via `git_server_ssh_pubkeys`.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    git_server_ssh_pubkeys:
      - ssh-rsa ... user

  roles:
    - dannixon.services.git_server
```

## License

MIT
