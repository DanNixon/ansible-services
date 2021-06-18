import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    assert host.package("kea").is_installed


@pytest.mark.parametrize("filename,md5sum", [
    ("kea-dhcp4.conf", "6f650043dd01a6b85e194161a1f86ad0"),
    ("kea-dhcp6.conf", "09e7bf5a61550345e6e487f4976ee299"),
    ("kea-dhcp-ddns.conf", "1753e7eee118223e0aa00ed211a856b0"),
])
def test_files(host, filename, md5sum):
    f = host.file(f"/etc/kea/{filename}")
    assert f.exists
    assert f.md5sum == md5sum
