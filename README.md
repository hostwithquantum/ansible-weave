![ansible-lint](https://github.com/hostwithquantum/ansible-weave/workflows/ansible-lint/badge.svg) ![ci](https://github.com/hostwithquantum/ansible-weave/workflows/ci/badge.svg)

ansible-weave
=========

The role will install weave on each host and create a network between them.

Requirements
------------

 - `docker-cli` installed
 - `systemd`

Role Variables
--------------

See [defaults/main.yml](defaults/main.yml)

Dependencies
------------

_None._

Example Playbook
----------------

Use the following to provision weave across an inventory group called `servers`:

    - hosts: servers
      gather_facts: True
      gather_subset: network
      roles:
        - role: ansible-weave
          become: true
          vars:
            weave_inventory_group: servers
            weave_password: "abc"

Weave will need the following ports to work:

 - TCP 6783 and UDP 6783/6784 between nodes
 - TCP 6781/6782 for /metrics

License
-------

Apache 2.0

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
