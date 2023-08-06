<h1 align="center">kilroy-module-client-py-sdk</h1>

<div align="center">

SDK for kilroy module clients in Python 🧰

[![Lint](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/lint.yaml)
[![Tests](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/test-multiplatform.yaml)
[![Docs](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-client-py-sdk/actions/workflows/docs.yaml)

</div>

---

## Installing

Using `pip`:

```sh
pip install kilroy-module-client-py-sdk
```

## Usage

```python
from kilroy_module_client_py_sdk import ModuleService

service = ModuleService(host="localhost", port=11000)

await service.get_metadata()
```
