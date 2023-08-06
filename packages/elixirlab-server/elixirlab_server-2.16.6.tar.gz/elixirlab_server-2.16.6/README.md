<div align="center">
    <img src="https://raw.githubusercontent.com/ElixirNote/elixirserver/main/jupyter_server/static/logo/logo.png" width=120 alt="logo" />
    <br />
    <small>go from data to knowledge</small>
</div>

# [ElixirLab Server](https://ciusji.gitbook.io/elixirnote/guides/elixirnote-lab-server)

[![codecov](https://codecov.io/gh/jupyterlab/jupyterlab_server/branch/main/graph/badge.svg?token=4fjcFj91Le)](https://codecov.io/gh/jupyterlab/jupyterlab_server)
[![Build Status](https://github.com/jupyterlab/jupyterlab_server/workflows/Tests/badge.svg?branch=master)](https://github.com/jupyterlab/jupyterlab_server/actions?query=branch%3Amaster+workflow%3A%22Tests%22)
[![Documentation Status](https://readthedocs.org/projects/jupyterlab_server/badge/?version=stable)](http://jupyterlab_server.readthedocs.io/en/stable/)

## Motivation

ElixirLab Server sits between ElixirLab and Elixir Server, and provides a
set of REST API handlers and utilities that are used by ElixirLab. It is a separate project in order to
accommodate creating JupyterLab-like applications from a more limited scope.

## Install

`pip install elixirlab-server`

## Usage

See the full documentation for [ElixirNote Lab Server Docs](https://ciusji.gitbook.io/elixirnote/guides/elixirnote-lab-server).

## Extending the Application

Subclass the `LabServerApp` and provide additional traits and handlers as appropriate for your application.

## Contribution

Please see `CONTRIBUTING.md` for details.
