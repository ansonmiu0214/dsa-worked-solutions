# DSA Worked Solutions ![Test](https://github.com/ansonmiu0214/dsa-worked-solutions/workflows/Test/badge.svg)

Worked solutions to Data Structures and Algorithms problems.

## Solutions with Explanations

See [website](https://ansonmiu0214.github.io/dsa-worked-solutions)

## Code

See `solutions/` directory.

This repo is set up to work with the [Remote Containers extension](https://code.visualstudio.com/docs/remote/containers) on VS Code.

* `Dockerfile` pulls a lightweight Python base image
* `.dev-compose.yml` defines the development container
* `.devcontainer` tells VS Code how to access/create the development container

### Running the solution to any problem:
```bash
python -m solutions
```

Pick from interactive prompt.

### Running the solution to problem `foo`:
```bash
python -m solutions.foo
```

### Running tests for solution to problem `foo`:
```bash
python -m unittest solutions.foo.test
```
