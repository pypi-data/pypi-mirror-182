<h1 align="center">kilroy-module-server-py-sdk</h1>

<div align="center">

SDK for kilroy module servers in Python 🧰

[![Lint](https://github.com/kilroybot/kilroy-module-server-py-sdk/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-server-py-sdk/actions/workflows/lint.yaml)
[![Tests](https://github.com/kilroybot/kilroy-module-server-py-sdk/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-server-py-sdk/actions/workflows/test-multiplatform.yaml)
[![Docs](https://github.com/kilroybot/kilroy-module-server-py-sdk/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-server-py-sdk/actions/workflows/docs.yaml)

</div>

---

## Installing

Using `pip`:

```sh
pip install kilroy-module-server-py-sdk
```

## Usage

```python
from kilroy_module_server_py_sdk import Module, ModuleServer

class MyModule(Module):
    ... # Implement all necessary methods here

module = await MyModule.build()
server = ModuleServer(module)

await server.run(host="0.0.0.0", port=11000)
```
