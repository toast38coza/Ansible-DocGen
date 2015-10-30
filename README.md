# Ansible-DocGen
A python utility for generating Ansible README.md files for roles

* Ansible-DocGen is tested in `python3`


## Installation

### PIP

    pip install ansible-docgeneration
    
**Note if you installed it from pip, you will need to use it like so from the command line:**

    python -m docgen

### From Source

```
git clone git@github.com:toast38coza/Ansible-DocGen.git
cd Ansible-DocGen
virtualenv-3.4 env -p python3
source env/bin/activate
pip install -r requirements.txt
```

## Usage

```
Usage: docgen.py [OPTIONS]

# Basic usage: 
python docgen.py

#Specify a path to a role: 
python docgen.py --path=/path/to/ansible/role

#Specify a path to a role, and output the result to a file: 
python docgen.py --path=/path/to/ansible/role > /path/to/ansible/role/README.md
```

**Options:**

* `--path`  Path to your role (defaults to current directory)
* `--help`       Show this message and exit.

## Test 

.. coming soon

## Example output:

A role for settings up a django application

* **Required ansible version:** >= 1.2


## Required variables:
| Parameter    | Example  | Comment  |
|--------------|----------|----------|
|`django_app_name`|`polls`|The name of your application. Typcially this will be the name of the folder containing your settings.py file|


## Optional variables:

| Parameter    | Default | 
|--------------|----------|
|`django_settings_directory_path`|`{{django_app_path}}/{{django_project_name}}`|
|`django_gunicorn_workers`|`2`|
|`django_venv_path`|`/srv/venvs/{{django_app_name}}`|
|`django_media_path`|`/srv/{{django_app_name}}/media`|
|`django_http_port`|`8000`|
|`manage_commands`|`['collectstatic', 'syncdb', 'migrate']`|
|`django_settings_vars`|`[]`|
|`django_static_path`|`/srv/{{django_app_name}}/static`|
|`django_log_path`|`/var/log/{{django_app_name}}`|
|`django_requirements_location`|`{{django_app_path}}/requirements.txt`|
|`django_env_vars`|`[]`|
|`django_version`|`1.8`|
|`django_app_path`|`/var/www/{{django_app_name}}`|
|`django_github_version`|`master`|


### Basic usage

```
- hosts: all
  vars:
    - django_app_name: polls
  roles:
    - { role: django, tags: django }

```

### TODO

* TODO: use pex to package virtualenv
* Unit testing
* Travis CI 
* Better error handling