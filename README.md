# Configuris

Configuration management made easy!

## What is it?

A collection of parsing libraries combined into one thing for configuration purposes.

## Features

- Support for JSON, YAML and TOML
- One class for everything
- Easy file management
  - File being created on object initialization
  - Methods for writing and reading file
- Only one property to use your configuration!

## Install

`pip install configuris`

## Examples

Read data from "settings.toml" file:

```python

from configuris import Configuris


settings = Configuris("settings", filetype="toml") # create configuris object
settings.read_file() # use this method to read our config

print(settings.data["info"]) # get our data from data property
```

`I like Configuris!`

Write data to "config.yml" file:

```python
from configuris import Configuris


config = Configuris(filetype="yml") # Configuris will use the default "config" value as file's name
config.data = {"auto_restart": True}
config.write_file() # will parse data property into yaml format and, obviously, writes it to file.
```

Contents of the file:

```yaml
auto_restart: true
```
