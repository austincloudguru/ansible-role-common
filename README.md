Common
=========
[![Molecule](https://github.com/austincloudguru/ansible-role-common/workflows/Molecule/badge.svg)](https://github.com/austincloudguru/ansible-role-common/actions?query=workflow%3AMolecule)
![Latest Version](https://img.shields.io/github/v/tag/austincloudguru/ansible-role-common?sort=semver&label=Latest%20Version) 
[![License](https://img.shields.io/github/license/austincloudguru/ansible-role-common)](https://github.com/austincloudguru/ansible-role-common/blob/master/LICENSE)

Role for common things that are installed on every server.  

Actions Completed:
- Users.  Creates Users.
- Group. Creates Groups.
- Sudoers: Creates individual sudoers files.
- MOTD: Creates the Message of the Day.
- Hostname: Sets the hostname.
- Extra Packages. Installs any additional package a system needs

Requirements
------------
This role is tested on Ubuntu 18.04 and Amazon Linux 2.  

Role Variables
--------------
### Playbook Variables
Within your playbook, you should set the following Variables

    common_groups:
      - name:
        id:
        state:
    common_users:
      - name:
        id:
        group:
        state:
        shell: 
        ssh_key:  
    common_sudoers:
      - name: sysadmin
        state: present
        permission: "ALL=(ALL) NOPASSWD:ALL"}
    common_hostname: 

Dependencies
------------
None

Example Playbook
----------------
Define the required variables in your playbook:

    - hosts: all
      vars:
        ansible_python_interpreter: /usr/bin/python3
        common_groups:
          - {name: sysadmin, id: 5000, state: present}
        common_users:
          - name: mark.honomichl
            id: 5000
            group: sysadmin
            state: present
            shell: /bin/zsh}
            ssh_key: ssh-rsa $MYKEY
        common_sudoers:
          - {name: sysadmin, state: present, permission: "ALL=(ALL) NOPASSWD:ALL"}
      roles:
        - austincloudguru.common

License
-------
MIT

Author Information
------------------
Mark Honomichl aka [AustinCloudGuru](https://austincloud.guru)
Created in 2020 
