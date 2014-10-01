speedrun-python
=================================

A bare-bones Python environment, ready for the immediate development of Python
web applications.

## Requirements
Core:
* Python
* PIP

Vagrant:
* Vagrant >= 1.5.2
* Virtualbox
* YAML gem

## Usage



## Deployment

Local Vagrant deployment:
```sh
$ vagrant up
```

## Notes

Most of the system tools you need are provided straight out-of-the-box courtesy
of Land Registry's [infrastructure-puppet-devkit](https://github.com/LandRegistry/infrastructure-puppet-devkit).

This environment uses a standardised Land Registry-approved Ubuntu 14.04 LTS
template built using [infrastructure-packer-ubuntu](https://github.com/LandRegistry/infrastructure-packer-ubuntu).
Updates to this template are automatically pushed into your Vagrant environment
when they become available.
