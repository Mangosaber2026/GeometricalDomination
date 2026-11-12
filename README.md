# GeometricalDomination

A Python turtle graphics library and DSAPI with an embedded DSL for creating drawings, patterns, shapes, and other geometric designs.

## What is GeometricalDomination?

GeometricalDomination is a personal Python project built around Python's `turtle` module.

It provides a collection of tools for controlling turtles, creating geometric patterns, drawing letters and symbols, defining custom commands, and simplifying repetitive turtle operations.

The project is structured as a Python package and is currently in the 6.x.x release series.

## Features

* Geometric shapes and patterns through `shapes.py`
* Alphabet and symbol drawing through `alphabets.py`
* Custom turtle shapes through `UserShape`
* User-defined drawing commands through `Command`
* Complex predefined turtle designs through `designs.py`

## Installation

The package can be installed with:

```bash
pip install GeometricalDomination
```

## Project Structure

The main components of the project include:

* `turtle_runner.py` — main program execution module
* `designs.py` — a collection of complex predefined geometric patterns and designs
* `alphabets.py` — a collection of validated English letters, punctuation, and geometric shapes 
* `UserCommands` — the user-facing command layer of the embedded DSL
* `CustomTurtleShapes` — the API for creating and managing custom turtle shapes

## Requirements

* Python 3.15 or newer
* Python's built-in `turtle` module

### External Python packages

`UniversalFunctions` -> Provides crucial validation features with additional reusable helper functions.

`TurtleExtension` -> Provides the actual turtle framework required to run this software.

`numpy` -> used for mathematical features in `shapes_multiverse`.

## Project Status

GeometricalDomination is under active development.

Other than testing (which is still under development), the functionality has been broadly tested to work properly.

## License

Check out the `LICENSE` file to find the information about the license that this software uses.