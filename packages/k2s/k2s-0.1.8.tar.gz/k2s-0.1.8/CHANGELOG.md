# CHANGELOG

## 0.1.8 (2022-12-24)
- Adds support for Google Colab's new runtime (Python 3.8)

## 0.1.7 (2022-12-24)
- Fixes Colab checking function
- `k2s get` accepts GitHub URLS (the ontas that show notebook preview)
- Adds `--no-jupyter` option to `k2s get` to skip opening Jupyter
- Support for customizing `k2s` home path
- `pkg_exists` supports pinned packages
- Better path detection (ignore `matplotlib` settings, empty strings and extensions with spaces)

## 0.1.6 (2022-09-13)
- Shows spinner when running long processes

## 0.1.5 (2022-09-13)
- Adds anonymous telemetry
- Caching `install` when using Colab
## 0.1.4 (2022-09-13)
- Adds support for Google Colab

## 0.1.3 (2022-08-30)
- Parsing `%load_ext {pkg_name}`
- Showing progress when installing packages
- Adding `metadata.kernelspec` info to notebook if missing

## 0.1.2 (2022-08-30)
- Parsing string literals in notebooks and downloading them if they exist

## 0.1.1 (2022-08-29)
- Ignores parsed `pip install` options
- Created virtual environment has `{name}-env` format

## 0.1 (2022-08-29)
- First release
