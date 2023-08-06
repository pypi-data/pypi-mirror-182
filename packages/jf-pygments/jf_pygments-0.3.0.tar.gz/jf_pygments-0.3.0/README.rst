jf_pygments
===========

Extend the Python syntax highlighter with some custom lexers and styles.

https://pygments.org/docs/plugins/

::

    pip install --user "pygments[plugins]"

::

    pip install --user jf_pygments

https://python-poetry.org/docs/pyproject/#plugins

.. code-block:: toml

    [tool.poetry.plugins]

    [tool.poetry.plugins."pygments.styles"]
    white = "jf_pygments:WhiteStyle"
    baldr = "jf_pygments:BaldrStyle"

    [tool.poetry.plugins."pygments.lexers"]
    baldrsql = "jf_pygments:BaldrSqlLexer"
