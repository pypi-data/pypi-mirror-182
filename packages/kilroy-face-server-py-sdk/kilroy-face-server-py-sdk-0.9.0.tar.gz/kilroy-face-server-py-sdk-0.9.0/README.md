<h1 align="center">kilroy-face-server-py-sdk</h1>

<div align="center">

SDK for kilroy face servers in Python 🧰

[![Lint](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/lint.yaml)
[![Tests](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/test-multiplatform.yaml)
[![Docs](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-server-py-sdk/actions/workflows/docs.yaml)

</div>

---

## Installing

Using `pip`:

```sh
pip install kilroy-face-server-py-sdk
```

## Usage

```python
from kilroy_face_server_py_sdk import Face, FaceServer

class MyFace(Face):
    ... # Implement all necessary methods here

face = await MyFace.build()
server = FaceServer(face)

await server.run(host="0.0.0.0", port=10000)
```
