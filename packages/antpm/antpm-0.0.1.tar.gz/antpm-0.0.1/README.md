<h1 align="center">Welcome to antpm 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="demo.com" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> the ant path matcher python version

### 🏠 [Homepage](github.com/cxiaoer/antpm)

### ✨ [Demo](baidu.com)

## Install

```sh
pip3 install antpm
```

## Usage

```python
from antpm import AntPathMatcher
ant_matcher = AntPathMatcher()
res:bool = ant_matcher.match("t?st", "test")
```

## Run tests

```sh
python -m unittest -v .\tests\test_antpm.py
```

## Author

👤 **cxiaoer**

* Website: https://github.com/cxiaoer
* Github: [@cxiaoer](https://github.com/cxiaoer)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](github.com/cxiaoer/antpm/issues). 

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_