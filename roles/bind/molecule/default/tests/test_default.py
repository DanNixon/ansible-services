import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    assert host.package("bind").is_installed


@pytest.mark.parametrize("filename,md5sum", [
    ("/etc/named.conf", "e4b5382cad8b9cf3dbcc2d99233acf07"),
    ("/var/named/internal_fwd.zone", "ae9d32c03755e56539b2f96da92a2c53"),
    ("/var/named/guest_fwd.zone", "a75f94d83416d22e4eb01144831c8f17"),
])
def test_files(host, filename, md5sum):
    f = host.file(filename)
    assert f.exists
    assert f.md5sum == md5sum
