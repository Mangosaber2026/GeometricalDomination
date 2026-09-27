# GeometricalDomination

A Python turtle graphics library and DSAPI with an embedded DSL for creating drawings, patterns, shapes, and other geometric designs.

## What is GeometricalDomination?

GeometricalDomination is a personal Python project built around Python's `turtle` module.

It provides a collection of tools for controlling turtles, creating geometric patterns, drawing letters and symbols, defining custom commands, and simplifying repetitive turtle operations.

The project is structured as a Python package and is currently in the 1.x.x release series.

## Features

* Chained turtle commands through `ChainTurtle`
* Geometric shapes and patterns through `Shapes`
* Alphabet and symbol drawing through `Alphabets`
* Custom turtle shapes through `UserShape`
* User-defined drawing commands through `Command`
* Reusable utility and validation functions through `UniversalFunctions`
* Reusable decorator composition through `cls_deco_superposition`
* Multi-turtle drawing functionality through `GlobalFunctions`
* Complex predefined turtle designs through `Designs`

## Installation

The package can be installed with:

```bash
pip install GeometricalDomination
```

## Project Structure

The main components of the project include:

* `TurtleRunner` — main program execution module
* `TurtleSkeleton` — extended turtle chaining functionality
* `Designs` — a collection of complex predefined geometric patterns and designs
* `Alphabets` — a collection of validated English letters, punctuation, and geometric shapes 
* `UserCommands` — the user-facing command layer of the embedded DSL
* `CustomTurtleShapes` — the API for creating and managing custom turtle shapes
* `GlobalFunctions` — turtle creation, color configuration and screen initialization
* `UniversalFunctions` — the foundational bridge between the infrastructure of the API and its underlying systems
* `Validators` — the Quantum and Classical Validator Dimension

## Requirements

* Python 3.14 or newer
* Python's built-in `turtle` module

No external Python packages are currently required... yet.

## Project Status

GeometricalDomination is under active development.

Other than testing (which is still under development), the functionality has been broadly tested to work properly.

## License

Check out the `LICENSE` file to find the information about the license that this software uses.
