<h1 align="center">
  Django Rest CLI 🚀
</h1>

<p align="center">
  <img src="./assets/logo.png" width="150" height="150">
</p>

<p align="center">
   Scaffold your DRF projects with common python packages configured, auto-generated docs, auto-generated CRUD endpoints, pre-commit hook, and more ...⚡🚀
</p>

<p align="center">
  <a href="https://github.com/tiangolo/typer/actions?query=workflow%3ATest" target="_blank">
      <img src="https://github.com/tiangolo/typer/workflows/Test/badge.svg" alt="Test">
  </a>
  <a href="https://pypi.org/project/typer" target="_blank">
      <img src="https://img.shields.io/pypi/v/typer?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
</p>

## What is Django Rest CLI ?
It is a CLI tool that seeks to help you build your Django Rest APIs faster.
It takes care of the commonly repeated aspects of building a REST API with the Django Rest Framework just so you're more productive :)

This tool speeds up your development in three ways:

- It allows you start your project from one of three templates we provide: Basic, Medior, and Advanced templates. Depending on what template you select, you could scaffold your project with packages like python_decouple for managing sensitive keys, pytest for unit tests, drf_spectacular for auto-generating docs, authentication endpoints, pre-commit hook for code linting setup in your project, and docker support.Regardless of the template you select, we initialize git, and add a readme to your project.

- You can define your models and have this tool generate CRUD endpoints for each model defined.
For example, if you define a model, **Product** in your `models.py` file, this tool could generate a _GET /products POST /products PUT /products/<product_id>_ etc. endpoints for that model.

- In Django it is common to have multiple apps in your project. If you know all the apps in your project before hand, with this tool, you could create them all at once.

## Demo
working on it

## Motivation
in the works too

## Usage
I never run am yet 
### Installation

### CLI Commands

###### `startproject project_name`

###### `startapps app1_name app2_name app3_name`

###### `addcrud app1_name app2_name app3_name`

## Contributing Guide

## Acknowledgements

## Thank you Nyior :)

## Licence
MIT


**Note** On Windows, Emojis are only supported in [Windows Terminal Preview](https://www.microsoft.com/en-us/p/windows-terminal-preview/9n8g5rfz9xk3?activetab=pivot:overviewtab)