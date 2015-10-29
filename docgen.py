## python shell script for generating documentation for Ansible roles


import click, yaml, glob
from jinja2 import Template

## usage and help instructions
help_template = """
## Preparing your role for documentation. 

* Basic meta's are populated from meta/main:galaxy_info
* Optional variables are populated from `defaults/main.yml`
* Make sure you have a `required_variables` section in `meta/main.yml`
* Examples in a directory `examples/*.yml` will be loaded into the Usage section
"""

readme_template = """

{{meta_info.galaxy_info.description}}

* **Required ansible version:** >= {{meta_info.galaxy_info.min_ansible_version}}

{% if meta_info.required_variables %}
## Required variables:
| Parameter    | Example  | Comment  |
|--------------|----------|----------|
{% for var in meta_info.required_variables %}|`{{var.key}}`|`{{var.example}}`|{{var.description}}|
{% endfor %}
{% endif %}


{% if optional_vars %}
## Optional variables:

| Parameter    | Default | 
|--------------|----------|
{% for key, value in optional_vars.items() %}|`{{key}}`|`{{value}}`|
{% endfor %}
{% endif %}

{% if examples %}
## Usage
{% for example in examples %}
### {{example.pretty_name}}

```
{{example.content}}
```

--
{% endfor %}
{% endif %}

{% if meta_info.dependencies %}
## Dependencies:
{% for dependency in meta_info.dependencies %}
* {{dependency}}{% endfor %}
{% endif %}

"""

## todo: make this a class
def _load_yml_file(base, path, default_return_value=[]):
    file_path = "{}{}" . format (base, path)
    with open(file_path, 'r') as stream:
        return yaml.load(stream)

    return default_return_value


def get_optional_vars(path):
    return _load_yml_file(path, "defaults/main.yml")
    

def get_meta(path):

    meta = _load_yml_file(path, "meta/main.yml")    
    return meta

def get_examples(path):

    examples = glob.glob("{}examples/*.yml" . format(path))

    example_list = []
    for example in examples:

        with open(example, 'r') as example_file:
            human_friendly_filename = example_file.name.split("/")[-1][:-4].replace("_", " ").capitalize()
            example_list.append({
                "filename": example,
                "pretty_name": human_friendly_filename,
                "content": example_file.read()
            })
    return example_list

@click.command()
@click.option('--path', default='./', help='Path to your role (defaults to current directory)')
def generate_documentation(path):
    """
    Generate a nice README.md file for an Ansible role

    Examples:

    Basic usage:
    python docgen.py 

    Specify a path to a role:
    python docgen.py --path=/path/to/ansible/role

    Specify a path to a role, and output the result to a file:
    python docgen.py --path=/path/to/ansible/role > /path/to/ansible/role/README.md

    """
    
    readme_path = "{}README.md" . format (path)

    context = {
        "project_name": "Django",
        "optional_vars": get_optional_vars(path),
        "meta_info": get_meta(path),
        "examples": get_examples(path),
    }
    template = Template(readme_template)
    print (template.render(**context))
    


if __name__ == '__main__':
    generate_documentation()    