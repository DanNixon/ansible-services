import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("package_name", [
    "dnscrypt-proxy",
])
def test_packages(host, package_name):
    assert host.package(package_name).is_installed


def test_config_file(host):
    f = host.file("/etc/dnscrypt-proxy/dnscrypt-proxy.toml")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_blocked_names(host):
    f = host.file("/etc/dnscrypt-proxy/blocked-names.txt")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
    # TODO


def test_forwarding_rules(host):
    f = host.file("/etc/dnscrypt-proxy/forwarding-rules.txt")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
    # TODO
