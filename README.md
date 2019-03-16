# Counting keywords in html page.

## Running app in developer mode
Firstly you may want to prepare developer config (./app/config/config_dev.py), example:
```python
#!/usr/bin/env python3
"""Developer config."""
class APP:
    IP = "0.0.0.0"
    PORT = 14000
    DEBUG = True
```

### Using Virtualenv
1. if it's first app run, you need to prepare virtualenv with all requirements. 
In main folder of project run command:<br>
`make venv` which prepare everything.
1. run app with command: `make dev_run`

### Using docker-compose
1. enter docker folder: `cd docker`
1. run docker compose: `docker-compose up`
