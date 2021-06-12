import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    assert host.package("dnscrypt-proxy").is_installed


def test_config_file(host):
    f = host.file("/etc/dnscrypt-proxy/dnscrypt-proxy.toml")
    assert f.is_file
    assert f.contains("require_dnssec = true")


def test_blocked_names(host):
    f = host.file("/etc/dnscrypt-proxy/blocked-names.txt")
    assert f.is_file
    assert f.contains("google.com")
    assert f.contains("facebook.com")


def test_forwarding_rules(host):
    f = host.file("/etc/dnscrypt-proxy/forwarding-rules.txt")
    assert f.is_file
    assert f.contains("lan 192.168.1.1")
