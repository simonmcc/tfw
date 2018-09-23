=================
Terraform Wrapper
=================


.. image:: https://img.shields.io/pypi/v/tfw.svg
        :target: https://pypi.python.org/pypi/tfw

.. image:: https://img.shields.io/travis/simonmcc/tfw.svg
        :target: https://travis-ci.org/simonmcc/tfw

.. image:: https://readthedocs.org/projects/tfw/badge/?version=latest
        :target: https://tfw.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




wrapper for terraform to streamline setup & multi-environment repos using terraform in a CI/CD pipeline

(based on multiple embedded scripts written in bash: https://github.com/jenkins201/packer-terraform-cicd-aws/blob/master/scripts/tf-wrapper.sh


* Free software: MIT license
* Documentation: https://tfw.readthedocs.io.


Features
--------

* Check AWS Credentials
* Setup a Terraform Remote State using AWS S3/DynamoDB (create bucket, create dynamodb table, generate remote_state.tf)

Feature Roadmap
---------------

* Setup a Terraform Remote State using Azure StorageAccount (create X, create table, generate remote_state.tf)
* Generate YAML/JSON inventory of EC2, RDS, LBs etc (for consumption by hiera, ansible etc)
* Git Branch/Terraform .tfvars mapping (master -> master.tfvars,  $branch -> $branch.tfvars with non-master-defaults.tfvars fall through)
* Git Branch/Terraform Workspace mapping (create/delete workspaces for CI builds)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
pip install --editable .
