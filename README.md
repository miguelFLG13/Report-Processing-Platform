## How to use the project

I've used Docker Compose to realize the project.

Before you use docker-compose in local you need to init some env vars:

```
export DJANGO_SETTINGS_MODULE='event_platform.settings.local'
export SECRET_KEY='eHv60Lp4t&HM7NKwuAaUx%C30nUUtgbE)FOi4u0A7dw'
```

To use in easy way the project the key is the Makefile in project folder, you can use some commands:

- **make up**: It inits the project and it puts the endpoints in http://localhost.
- **make up-non-daemon**: The same as `make up`  but with log.
- **make run-tests**: It runs all the project tests.

More Info? You can read the README.md in folder docs
