#!/bin/sh

mail_sender ()
{
    from="a@a.com"
    to="b@a.com"
    message="
Date: Wed, 9 May 2012 09:57:50 -0700 (PDT)
From: abard@example.com
To: abard@example.com, someoneelse@example.com
Message-ID: <JavaMail.jenkins@example.net>
In-Reply-To: <JavaMail.jenkins@example.net>
References: <JavaMail.jenkins@example.net>
Subject: Jenkins build is back to stable
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 7bit

Message text goes here."
    telnet localhost 8081 << EOF
helo localhost
mail from: $from
rcpt to: $to
data
$message
.
EOF
}

mail_sender
