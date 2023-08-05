<div align="center">
    <img src="https://raw.githubusercontent.com/ElixirNote/elixirserver/main/jupyter_server/static/logo/logo.png" width=120 alt="logo" />
    <br />
    <small>go from data to knowledge</small>
</div>

# [Elixir Shim](https://ciusji.gitbook.io/elixirnote/guides/elixirnote-shim)

This project provides a way for ElixirNote and other frontends to switch 
to [Elixir Server](https://github.com/ElixirNote/elixirserver) for their Python Web application backend.

## Basic Usage

Install from PyPI:

```
pip install elixir-shim
```

This will automatically enable the extension in Elixir Server.

## Usage

This project also includes an API for shimming traits that moved from `NotebookApp` in to `ServerApp` in Elixir Server. 
This can be used by applications that subclassed `NotebookApp` to leverage the Python server backend of Elixir Notebooks. 
Such extensions should *now* switch to `ExtensionApp` API in Elixir Server and add `NotebookConfigShimMixin` in 
their inheritance list to properly handle moved traits.

For example, an application class that previously looked like:

```python
from notebook.notebookapp import NotebookApp

class MyApplication(NotebookApp):
```

should switch to look something like:

```python
from jupyter_server.extension.application import ExtensionApp
from notebook_shim.shim import NotebookConfigShimMixin

class MyApplication(NotebookConfigShimMixin, ExtensionApp):
```