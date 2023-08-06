<h1 align="center">kilroy-module-py-shared</h1>

<div align="center">

shared code for kilroy module SDKs in Python 🤝

[![Lint](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/lint.yaml)
[![Tests](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/test-multiplatform.yaml)
[![Docs](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-py-shared/actions/workflows/docs.yaml)

</div>

---

## Overview

This package contains code shared by SDKs related to modules.
Mostly it's just a bunch of utilities and dataclasses.

## Installing

Using `pip`:

```sh
pip install kilroy-module-py-shared
```

## Messages

Messages are dataclasses that are used in the APIs.
They are automatically generated from the protobuf definitions.

## Posts

Posts are `pydantic` models that are used to represent various types of posts.
There are definitions for:

- `TextOnlyPost`
- `ImageOnlyPost`
- `TextAndImagePost`
- `TextOrImagePost`
- `TextWithOptionalImagePost`
- `ImageWithOptionalTextPost`

## Models

One useful thing this package provides is a `SerializableModel` class.
It's a base class for `pydantic` models
that can be serialized to and from JSON
with a proper case convention.
