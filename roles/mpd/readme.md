# `dannixon.services.mpd`

Installs and configures [Music Player Daemon (MPD)](https://www.musicpd.org/).

## Role Variables

MPD can run as either a `user` or `system` scoped service.
For music playback on a single device, user scope is sufficient, for music playback on a audio/media server, system scope may be more appropriate.
`mpd_service_scope` is used to set the desired scope.

`mpd_config` and `mpd_audio_outputs` set the general options and audio output configurations.
The expected formatting is shown in the example below.
Parameter names and expected values are the same as `mpd.conf` (see `man 5 mpd.conf`).

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    mpd_config:
      music_directory: /media/music

    mpd_audio_outputs:
      - type: pulse
        name: local

  roles:
    - dannixon.services.mpd
```

## License

MIT
