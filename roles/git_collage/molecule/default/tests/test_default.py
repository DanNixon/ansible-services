import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    assert host.package("git").is_installed


def test_git_user(host):
    assert host.user("git-collage").exists


def test_systemd_service(host):
    assert host.file("/usr/lib/systemd/system/git-collage.service").is_file


def test_systemd_timer(host):
    f = host.file("/usr/lib/systemd/system/git-collage.timer")
    assert f.is_file
    assert f.contains("OnCalendar=weekly")
