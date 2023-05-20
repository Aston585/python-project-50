# Difference Calculator

##### Hexlet tests and linter status
[![Actions Status](https://github.com/Aston585/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Aston585/python-project-50/actions)
[![Linting and testing](https://github.com/Aston585/python-project-50/actions/workflows/gendiff.yml/badge.svg)](https://github.com/Aston585/python-project-50/actions/workflows/gendiff.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/bcb0d83bd6f06428dc5d/maintainability)](https://codeclimate.com/github/Aston585/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/bcb0d83bd6f06428dc5d/test_coverage)](https://codeclimate.com/github/Aston585/python-project-50/test_coverage)


A difference calculator is a program that determines the difference between two data structures.

### Utility features
- Support for different input formats: yaml, json
- Report generation in the form of plain text, stylish and json

### Installation and launch
```
$ git clone https://github.com/Aston585/python-project-50.git
$ cd ./python-project-50
$ make install
```
```
$ make build
```
### Usage example
```
$ gendiff filepath1.json filepath2.json

{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting5: {
            key5: value5
        }
    }
}

```
```
$ gendiff -f plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed
```
### Utility demo
<a href="https://asciinema.org/a/q7LSKjNvu3YIcCtw0eFVOMOa6" target="_blank"><img src="https://asciinema.org/a/q7LSKjNvu3YIcCtw0eFVOMOa6.svg" /></a>
