<div align="center">
  <h1>mpsmtp</h1>

  <a href="https://travis-ci.org/manparvesh/mpsmtp/builds" target="_blank"><img src="https://img.shields.io/travis-ci/manparvesh/mpsmtp.svg?style=for-the-badge" alt="Build Status"></a> 
  <a href="https://manparvesh.mit-license.org/" target="_blank"><img src="https://img.shields.io/badge/license-MIT-blue.svg?longCache=true&style=for-the-badge" alt="License"></a> 
  
  <p><b>Man Parvesh's Simple Mail Transfer Protocol</b> is a simple implementation of an STMP server in Python 3.6</p>
</div>

## Requirements
- Python `3.6`
- [Click](http://click.pocoo.org/5/)
- `nose` for running tests
- other python requirements are listed in `requirements.txt`

## Installation
- Clone this repository
- `[Optional]` create a `virtualenv` and use python from there (only tested on Python 3.6).
- Install using pip: `pip install .`
- Run: `mpsmtp`
- Run `mpsmtp debug localhost 8081` for a debug server on port `localhost:8081`

## Implementation
- The `MPInbox` and `MPSMTPServer` are based on the implementations from [inbox.py](https://github.com/kennethreitz/inbox.py), with some changes like making the code Python 3.6 compatible and using the inbuilt `logging` library instead of `logbook`
- The debug server is a very simple implementation based on Python's `smtpd.DebuggingServer`. This simply outputs whatever email it receives on the console.

## Examples
### SMTP server
- When running the SMTP server after installation using the command `mpsmtp`, you should see the following output:
```
INFO:src.mpinbox:Starting SMTP server at localhost:8081
```

- Now, you can connect to this server using `telnet` in the following way (`S`=`server`, `C`=`client`):
```
S: Trying 127.0.0.1...
S: Connected to localhost.
S: Escape character is '^]'.
S: 220 mp Python SMTP proxy version 0.3
C: HELO localhost
S: 250 mp
C: MAIL FROM:a@a.com
S: 250 OK
C: RCPT TO:b@a.com
S: 250 OK
C: DATA
S: 354 End data with <CR><LF>.<CR><LF>
C: hey there!
C: 
C: .
S: 250 OK
C: QUIT
S: 221 Bye
```

- Alternatively, you could also use the script `mail_sender.sh` in the `tests` folder to send an email quickly.

- The logs in the server for the above action will be shown as below:
```
INFO:src.mpstmp_server:Collating message from a@a.com
INFO:src.mpstmp_server:{'to': ['b@a.com'], 'sender': 'a@a.com', 'body': b'hey there!\n'}
INFO:mpsmtp:Received email!!!!!!!!!!!
to:['b@a.com']
sender:a@a.com
body:b'hey there!\n'
```

### Debug server
- This server directly outputs the input it's getting to the console, whereas for the previous server you can implement the action to be taken on receiving email.

- You can start a debug server as follows:
```
mpsmtp debug localhost 8081
```

- After sending an email to this server like shown above, the output will be something like below:
```
INFO:mpsmtp:Running a debug server on localhost:8081
---------- MESSAGE FOLLOWS ----------
b'X-Peer: 127.0.0.1'
b''
b'Date: Wed, 9 May 2012 09:57:50 -0700 (PDT)'
b'From: abard@example.com'
b'To: abard@example.com, someoneelse@example.com'
b'Message-ID: <JavaMail.jenkins@example.net>'
b'In-Reply-To: <JavaMail.jenkins@example.net>'
b'References: <JavaMail.jenkins@example.net>'
b'Subject: Jenkins build is back to stable'
b'MIME-Version: 1.0'
b'Content-Type: text/plain; charset=utf-8'
b'Content-Transfer-Encoding: 7bit'
b''
b'Message text goes here.'
------------ END MESSAGE ------------
```

## TODO
 - [ ] implement storage and a simple REST API using flask to get and store emails.

## LICENSE
```
MIT License

Copyright (c) 2018 Man Parvesh Singh Randhawa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
