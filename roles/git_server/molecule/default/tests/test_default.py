import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    assert host.package("git").is_installed


def test_git_user(host):
    assert host.user("git").exists


def test_authorized_keys(host):
    f = host.file("/home/git/.ssh/authorized_keys")
    assert f.is_file
    assert f.contains("ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGYeGwrBRv6i1qIpBv/E90aqOe2Iound9O5JG41St306 fakeuser")
