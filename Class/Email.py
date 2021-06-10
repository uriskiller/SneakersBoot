import smtplib, ssl

class Email:
    def __init__(self):
        self.smtp = 'mail.katalitica.com'
        self.port = 465
        self.mail = 'uriel@katalitica.com'
        self.password = '4KyqKfrUqu'
        self.recipe = 'urielsm97@hotmail.com'

    def sendEmail(self, msg):

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self.smtp, self.port, context=context) as server:
            server.login(self.mail, self.password)
            # TODO: Send email here
            server.sendmail(self.mail, self.recipe, msg)

