# MaxConsole v0.5.0

[![PyPI](https://img.shields.io/pypi/v/maxconsole?style=for-the-badge)](https://pypi.org/project/maxconsole/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/maxconsole?style=for-the-badge)](https://pypi.org/project/maxconsole/) [![PyPI - License](https://img.shields.io/pypi/l/maxconsole?style=for-the-badge)](https://pypi.org/project/maxconsole/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/maxconsole?style=for-the-badge)](https://pypi.org/project/maxconsole/)

![](https://i.imgur.com/4AtSGpB.png)

## Purpose

MaxConsole instantiates a singleton class that wraps the console provided by the awesome <a href="https://github.com/willmcgugan/rich/">rich</a> library. It provides a simple interface for printing to the console, and is intended to be used as a global console object. It also has customized theme to allow for more variety of generic colors.

## Installation

MaxConsole is available on PyPI and can be installed with either pip, pdm, or your favorite package manager.

### Pip

```bash
pip install maxconsole
```

### PDM

```bash
pdm add maxconsole
```



## Usage
```python
from maxconsole import MaxConsole

console = MaxConsole() # It's that easy.
```



<hr />
<div style="font-size:0.8em;color:#2e2e2e;background:#e2e2e2;padding:20px;border-radius:5px;">
    <h3>MIT License</h3>
    <p style="font-size:0.8em">Copyright (c) 2021 Max well Owen Ludden</p>
    <p>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:</p>
    <p>The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.</p>
    <p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>
</div>
