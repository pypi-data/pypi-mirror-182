# SAS DBT adapter

[![Build Status](https://github.com/DLBD-Department/dbt-sas/workflows/Tests/badge.svg)](https://github.com/DLBD-Department/dbt-sas/actions)
[![PyPI version](https://badge.fury.io/py/dbt-sas.svg)](https://badge.fury.io/py/dbt-sas)
[![PyPI](https://img.shields.io/pypi/pyversions/dbt-sas.svg)](https://pypi.org/project/dbt-sas)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The dbt-sas package allows dbt to connect to SAS.

## Installation

```
pip install dbt-sas
```

## Configurations

Basic `profile.yml` for connecting to SAS:

```yml
sas-test:
  outputs:
    dev:
      type: sas
      host: SAS host
      port: 8591
      database: sas (keep 'sas', don't change)
      schema: default libray name
      user: SAS username
      password: SAS password
      autoexec: optional local path of autoexec.sas file
      lib_base_path: optional path (on the SAS server) for new libraries
      threads: 1
      fail_on_warnings: False
      lib_name_strict_mode: False
  target: dev

```
| Key                    | Required | Description                                          |
| ---------------------- | -------- | ---------------------------------------------------- |
| `type`                 | Yes      | The specific adapter to use (`sas`)                  |
| `host`                 | Yes      | SAS server hostname                                  |
| `port`                 | Yes      | SAS server port                                      |
| `database`             | Yes      | `sas`, don't change                                  | 
| `schema`               | Yes      | Default SAS libname                                  |
| `username`             | Yes      | The username to use to connect to the server         |
| `password`             | Yes      | The password to use for authenticating to the server |
| `handler`              | Yes      | SAS handler `ws` (default) or `saspy`                |
| `autoexec`             | No       | Local path of autoexec.sas file                      |
| `lib_base_path`        | No       | Base path on the SAS server for new libraries        |
| `fail_on_warnings`     | No       | Raise and error if it encounters a warning           |
| `lib_name_strict_mode` | No       | Enable strict libname/identifier check               |

## Features

| Key      | Supported | Description                                          | 
| -------- | -------- | ---------------------------------------------------- |
| [Tests](https://docs.getdbt.com/docs/build/tests) | Yes | Run dbt tests on SAS |
| [Load seed files](https://docs.getdbt.com/docs/build/seeds) | Yes | Load seeds from CSV files to SAS |
| [View Materialization](https://docs.getdbt.com/docs/build/materializations#view) | Yes | Materialize dbt models as views in SAS |
| [Table Materialization](https://docs.getdbt.com/docs/build/materializations#table) | Yes | Materialize dbt models as tables in SAS |
| [Ephemeral Materialization](https://docs.getdbt.com/docs/build/materializations#ephemeral) | Partial | Materialize dbt ephemeral tables as temporary views in SAS |
| [Incremental Materialization](https://docs.getdbt.com/docs/build/materializations#incremental) | No |  |
| [Snapshots](https://docs.getdbt.com/docs/build/snapshots) | No |  |
| [Grants](https://docs.getdbt.com/reference/resource-configs/grants) | No | SQL grants are not supported by SAS |

## Limitations

- Schemas (lib names) are limited to 8 characters.
- Table names, column names, and aliases are limited to 32 characters.

## Usage

- Create dbt project, choose sas database and set up connection
```console    
$ dbt init <project_name>
```

## Query Logging

Enable additional logging by setting the `DBT_SAS_LOG` environment variable to the log filename, e.g.:

```console
export DBT_SAS_LOG='file.log'
```

Select the log families, e.g.:

```console
export DBT_SAS_FAMILY='sas,sql'
```

Log families are:
- sas
- sql
- original_sql

## Adapter Testing

- Install dev requirements
```console
$ pip install -r dev_requirements.txt
```
- Run pytest
```console    
$ python -m pytest tests/
```

## Licence

Apache License, Version 2.0

## Links

* [SASpy](https://github.com/sassoftware/saspy)
* [SQL Procedure](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/sqlproc/n0w2pkrm208upln11i9r4ogwyvow.htm)
