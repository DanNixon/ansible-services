# `dannixon.services.go_neb`

[![dannixon.services.go_neb](https://github.com/DanNixon/ansible-services/actions/workflows/go_neb.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-services/actions/workflows/go_neb.yml)

Installs and configures [Go-NEB](https://github.com/matrix-org/go-neb/) Matrix bot.

## Role Variables

`go_neb_repo` and `go_neb_revision` define the version of the code to obtain.

The following options map to the environment variables described [here](https://github.com/matrix-org/go-neb#running):
  - `go_neb_bind_address` = `BIND_ADDRESS`
  - `go_neb_base_url` = `BASE_URL`
  - `go_neb_database_type` = `DATABASE_TYPE`
  - `go_neb_database_url` = `DATABASE_URL`

`go_neb_config` encodes the same data as what would be provided in the [the config file](https://github.com/matrix-org/go-neb#configuration-file).

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    go_neb_bind_address: ":4050"
    go_neb_base_url: http://localhost

    go_neb_config:
      clients:
        - UserID: "@goneb:localhost"
          AccessToken: MDASDASJDIASDJASDAFGFRGER
          DeviceID: DEVICE1
          HomeserverURL: http://localhost:8008
          Sync: true
          AutoJoinRooms: true
          DisplayName: "Go-NEB!"
          AcceptVerificationFromUsers:
            - ":localhost:8008"

  roles:
    - dannixon.services.go_neb
```

## License

MIT
