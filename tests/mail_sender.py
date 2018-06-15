
def smtp_test():
    import smtplib

    SERVER = "localhost:4467"

    FROM = "sender@example.com"
    TO = ["user@example.com"]  # must be a list

    SUBJECT = "Hello!"

    TEXT = "This message was sent with Python's smtplib."

    # Prepare actual message

    message = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail

    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, message)
    server.quit()


if __name__ == '__main__':
    smtp_test()
