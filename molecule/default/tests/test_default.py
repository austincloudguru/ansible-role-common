import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_group_exists(host):
    sysadmin_group = host.group("sysadmin")
    assert sysadmin_group.exists


def test_user_exists(host):
    user = host.user("mark.honomichl")
    assert user.exists


def test_sudoers(host):
    assert host.file("/etc/sudoers.d/sysadmin").contains("sysadmin")


def test_ssh_keyfile(host):
    ssh_keyfile = host.file('/home/mark.honomichl/.ssh/authorized_keys')
    assert ssh_keyfile.exists
    assert ssh_keyfile.mode == 0o600
