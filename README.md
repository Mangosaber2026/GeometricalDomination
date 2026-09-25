# GeometricalDomination

A Python turtle graphics library and DSL for creating drawings, patterns, shapes, and other geometric designs.

## What is GeometricalDomination?

GeometricalDomination is a personal Python project built around Python's `turtle` module.

It provides a collection of tools for controlling turtles, creating geometric patterns, drawing letters and symbols, defining custom commands, and simplifying repetitive turtle operations.

The project is structured as a Python package and there is no main version yet.

## Features

* Chained turtle commands through `ChainTurtle`
* Geometric shapes and patterns `Shapes`
* Alphabet and symbol drawing `Alphabets`
* Custom turtle shapes `User`
* User-defined drawing commands `Command`
* Utility and validation functions `UniversalFunctions (package)`
* Reusable decorators `cls_deco_superposition`
* Support for multiple turtles `Globalfunctions`
* Tools for creating complex turtle-based drawings `Designs`

## Installation

The package can be installed with:

```bash
pip install GeometricalDomination
```

## Project Structure

The main components of the project include:

* `TurtleRunner` — main program entry point
* `TurtleSkeleton` — extended turtle functionality
* `Designs` — geometric designs and patterns
* `Alphabets` — letter and symbol drawing
* `UserCommands` — user-oriented drawing commands
* `CustomTurtleShapes` — custom turtle shapes
* `GlobalFunctions` — shared turtle and screen functionality
* `UniversalFunctions` — reusable helper and utility package

## Requirements

* Python 3.14 or newer
* Python's built-in `turtle` module

No external Python packages are currently required.

## Project Status

GeometricalDomination is under active development.

Other than testing (which is still under development), the functionality has been broadly tested to work properly.

## License

Check out the `LICENSE` file to find the information about the license that this software uses.
