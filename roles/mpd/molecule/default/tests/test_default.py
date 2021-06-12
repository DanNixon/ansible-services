import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config_file(host):
    f = host.file("/root/.config/mpd/mpd.conf")
    assert f.is_file
    assert f.contains("music_directory \"/media/music\"")
    assert f.contains("type \"pulse\"")
