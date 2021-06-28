Common
=========
Role for common things that are installed on every server.  

Actions Completed:
  - Users
  - Gropuip


Right now, it just manages users/groups/sudoers and installs zsh.  It's not really for anybody else but me.

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
