import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('weave')


@pytest.mark.parametrize('file', [
  '/etc/systemd/system/weave.service',
  '/etc/sysconfig/weave',
  '/usr/local/bin/weave'
])
def test_files(host, file):
    f = host.file(file)

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_weave_launch_args(host):
    unit = host.file('/etc/systemd/system/weave.service')
    assert unit.contains('--dns-domain="mesh.local."')
    assert unit.contains('--dns-ttl=10')


def test_peers(host):
    hostname = host.check_output('hostname -s')

    sysconfig = host.file('/etc/sysconfig/weave')
    assert not sysconfig.contains(hostname)


def test_weave_is_running_and_enabled(host):
    svc = host.service("weave")
    assert svc.is_running
    assert svc.is_enabled


def test_weave_status(host):
    status = host.check_output('weave status')

    # no password is set
    assert 'Encryption: disabled' in status

    # assert on other `weave_launch_args`
    assert 'Domain: mesh.local.' in status
    assert 'TTL: 10' in status

    # this asserts the distributed network is running
    assert 'Connections: 1 (1 established)' in status
    assert 'Peers: 2 (with 2 established connections)' in status
