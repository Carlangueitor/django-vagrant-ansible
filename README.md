# Ansible Demo
This a simple deme presented in *Chilango Django* Meetup.

## Prerequisites

* VirtualBox
* Vagrant >= 1.1
* Vagrant plugin `vagrant-vbguest` (install with `vagrant plugin install vagrant-vbguest`)
* Ansible >= 2.0

## Running the example locally

Make sure prerequisites are installed before run these steps:

* Install Ansible Roles with `ansible-galaxy install -r requirements.txt`
* Create Vagrant machine: `vagrant up`

To run the provider use `vagrant provision

## Runing the remote example

* Edit `inventory.cfg` with your server details.
* Run `ansible-playbook playbook.yml -i inventory.cfg -l prod -k -u <REMOTE_USER>`
