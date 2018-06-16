<div align="center">
  <h1>mpsmtp</h1>

  <a href="https://travis-ci.org/manparvesh/mpsmtp/builds" target="_blank"><img src="https://img.shields.io/travis-ci/manparvesh/mpsmtp.svg?style=for-the-badge" alt="Build Status"></a> 
  <a href="https://manparvesh.mit-license.org/" target="_blank"><img src="https://img.shields.io/badge/license-MIT-blue.svg?longCache=true&style=for-the-badge" alt="License"></a> 
  <a href="https://codecov.io/gh/manparvesh/mpsmtp" target="_blank"><img src="https://img.shields.io/codecov/c/github/manparvesh/mpsmtp/master.svg?style=for-the-badge" alt="Coverage"></a>
  <p><b>Man Parvesh's Simple Mail Transfer Protocol</b> is a simple implementation of an STMP server in Python 3.6</p>
</div>

### Requirements
- Python `3.6`
- [Click](http://click.pocoo.org/5/)
- `nose` for running tests
- other python requirements are listed in `requirements.txt`

### Installation
- Clone this repository
- `[Optional]` create a `virtualenv` and use python from there (only tested on Python 3.6).
- Install using pip: `pip install .`
- Run: `mpsmtp`
- Run `mpsmtp debug localhost 8081` for a debug server on port `localhost:8081`
