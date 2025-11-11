# uvbump

[![PyPI - Version](https://img.shields.io/pypi/v/uvbump.svg)](https://pypi.org/project/uvbump)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/uvbump.svg)
![Last Commit](https://img.shields.io/github/last-commit/heiwa4126/uvbump)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](https://github.com/heiwa4126/uvbump/blob/main/README.md) | 日本語

## 概要

[Astral の uv](https://docs.astral.sh/uv/) で、
`uvx` や
`uv tool install` でインストール&実行されたときの、

- Python のバージョンと、
- Python の実行ファイルのパスと、
- スクリプト自身のパス

を表示するパッケージ。

uv の
`--python`
オプションの効果などを知るために作成した。

## 実行例

```console
$ uvx uvbump

Installed 1 package in 3ms
Python Version: 3.12.12 (main, Oct 28 2025, 12:10:49) [Clang 20.1.4 ]
Executable Path: /home/user1/.cache/uv/archive-v0/VEm-1_LGBHubU7SZHYbs2/bin/python
Script Path: /home/user1/.cache/uv/archive-v0/VEm-1_LGBHubU7SZHYbs2/lib/python3.12/site-packages/uvbump/uvbump.py

$ uvx --python 3.10 uvbump

Installed 1 package in 3ms
Python Version: 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0]
Executable Path: /home/user1/.cache/uv/archive-v0/Vcsgj4kD85VznE7HmFNsb/bin/python
Script Path: /home/user1/.cache/uv/archive-v0/Vcsgj4kD85VznE7HmFNsb/lib/python3.10/site-packages/uvbump/uvbump.py

$ uv tool install uvbump && uvbump

Resolved 1 package in 1ms
Installed 1 package in 3ms
 + uvbump==0.0.1
Installed 1 executable: uvbump
Python Version: 3.12.12 (main, Oct 28 2025, 12:10:49) [Clang 20.1.4 ]
Executable Path: /home/user1/.local/share/uv/tools/uvbump/bin/python
Script Path: /home/user1/.local/share/uv/tools/uvbump/lib/python3.12/site-packages/uvbump/uvbump.py

$ uv tool install --python 3.10 uvbump && uvbump

Ignoring existing environment for `uvbump`: the requested Python interpreter does not match the environment interpreter
Resolved 1 package in 1ms
Installed 1 package in 4ms
 + uvbump==0.0.1
Installed 1 executable: uvbump
Python Version: 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0]
Executable Path: /home/user1/.local/share/uv/tools/uvbump/bin/python
Script Path: /home/user1/.local/share/uv/tools/uvbump/lib/python3.10/site-packages/uvbump/uvbump.py
```

## 開発

### セットアップ

```bash
uv sync
```

### タスク実行

```bash
# テスト実行
poe test

# リント・フォーマット
poe check
poe format

# 型チェック
poe mypy

# 全チェック実行&ビルド&スモークテスト
poe build
```

### 開発要件

- Python >= 3.12
- uv

## ライセンス

MIT
