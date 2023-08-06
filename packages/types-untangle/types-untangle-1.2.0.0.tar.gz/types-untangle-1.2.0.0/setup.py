from setuptools import setup

name = "types-untangle"
description = "Typing stubs for untangle"
long_description = '''
## Typing stubs for untangle

This is a PEP 561 type stub package for the `untangle` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `untangle`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/untangle. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `4379a6a509396a58b85ac9f888c3eec5aac38039`.
'''.lstrip()

setup(name=name,
      version="1.2.0.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/untangle.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['untangle-stubs'],
      package_data={'untangle-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
