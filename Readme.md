# Smart Calculator desktop app in Python

## Table of Contents
- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)

## Introduction
SmartCalc is a powerful calculator application that allows you to perform a wide range of mathematical operations, visualize functions, and manage your calculation history.

App is built in Python 3.11 with the customtkinter library for the graphical user interface.

The program implemented using the MVP pattern.

The "core" of the calculator in the form of an algorithm for the formation and calculation of the Polish notation connect as a C++ dynamic library.

Prepared full coverage of methods in the model layer with unit tests.

## Installation
- Clone this repo to your local machine.
- `make` - to install/activate env, build a С++ dynamic library and run the app.

The app should now be up and running (I use MacOS) 🚀

- `make installer` - to prepare the installer, which will install the application to the system, create *.dmg* file.
- `make coverage` - to run tests and prepare html coverage report.
- `make lint` - to run linter.
- `make clean` - to clean project.

## Features
- Advanced Arithmetic.
- Function Plotting: Plot graphs of functions defined by expressions in infix notation with a variable 'x'. Customize the display and range of the graph to suit your needs.
- History Management: Store and recall your past calculations from the history panel.
- Calculation history is automatically saved between application runs.

- **Arithmetic operators**:

  | Operator name | Infix Notation <br />(Classic) | Prefix notation <br /> (Polish notation) | Postfix notation <br />(Reverse Polish notation) |
  | ------ | ------ | ------ | ------ |
  | Parentheses | (a + b) | (+ a b) | a b + |
  | Addition | a + b | + a b | a b + |
  | Subtraction | a - b | - a b | a b - |
  | Multiplication | a * b | * a b | a b * |
  | Division| a / b | / a b | a b \ |
  | Rasing to the power | a ^ b | ^ a b | a b ^ |
  | Remainder of division | a mod b | mod a b | a b mod |
  | Unary plus | +a | +a | a+ |
  | Unary minus | -a | -a | a- |

- **Functions**:

  | Function description | Function |
  | ---------------- | ------- |
  | Calculates cosine | cos(x) |
  | Calculates sine | sin(x) |
  | Calculates tangent | tan(x) |
  | Calculates arc cosine | acos(x) |
  | Calculates the arcsine | asin(x) |
  | Calculates arctangent | atan(x) |
  | Calculates square root | sqrt(x) |
  | Calculates natural logarithm | ln(x) |
  | Calculates decimal logarithm | log(x) |

- **Configurations**:
  - Background color.
  - Main accent color.
  - Font size.

- **Limitations**:
  - Input can contain up to 255 characters.
  - Graphs are limited to the defined value area and definition area.

## Usage
Using SmartCalc:
1. Enter your expression.
2. Utilize parentheses to group sub-expressions as needed.
3. Press '=' to calculate the result of the expression.
4. Explore the history panel to review past calculations and reload expressions.
5. To plot a function, enter the function expression, specify the display range, and press 'GRAPH'.
