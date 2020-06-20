ansible-weave
=========

The role will install weave on each host and create a network between them.

Requirements
------------

 - Docker installed
 - systemd

Role Variables
--------------

See [defaults/main.yml](defaults/main.yml)

Dependencies
------------

_None._

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - role: ansible-weave
          vars:
            weave_host:
              - host1
              - host2
              - host3
            weave_password: "abc"

License
-------

Apache 2.0

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
