# smtplib module send mail

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# TO = 'asharif@akumosolutions.io'
# SUBJECT = 'TEST MAIL'
# TEXT = 'Here is a message from python.'

# # Gmail Sign In
# gmail_sender = 'unifyshop.contact@gmail.com'
# gmail_passwd = '###########################'

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.ehlo()
# server.starttls()
# server.login(gmail_sender, gmail_passwd)

# BODY = '\r\n'.join(['To: %s' % TO,
#                     'From: %s' % gmail_sender,
#                     'Subject: %s' % SUBJECT,
#                     '', TEXT])

# try:
#     server.sendmail(gmail_sender, [TO], BODY)
#     print ('email sent')
# except:
#     print ('error sending mail')

# server.quit()

########################################################
########################################################

#! /usr/bin/python
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_order_Mail():
    # me == my email address
    # you == recipient's email address
    name = "FIRST & LAST NAME"
    me = "EMAIL ACCOUNT USED TO SEND EMAIL"
    you = "TARGET EMAIL "

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Automated email via Python script!!"
    msg['From'] = me
    msg['To'] = you


    html = '''
<!DOCTYPE html>
<html>

<head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style type="text/css">
        /* Style all font awesome icons */
        .fa {{
        padding: 5px;
        font-size: 10px;
        width: 20px;
        text-align: center;
        text-decoration: none;
        margin: 5px 2px;
        }}

        /* Add a hover effect if you want */
        .fa:hover {{
        opacity: 0.7;
        }}

        /* Set a specific color for each brand */

        /* Facebook */
        .fa-facebook-square {{
        color: #17202A;
        width: 400px,
        height: 300px
        }}
        /* Chrome */
        .fa-chrome {{
        color: #17202A;
        }}
        /* github */
        .fa-github-square {{
        color: #17202A;
        }}
        /* Telegram */
        .fa-telegram {{
        color: #17202A;
        }}
        /* Instagram */
        .fa-instagram {{
        color: #17202A;
        }}

        .checked {{
            color: rgb(37, 134, 179);
        }}
        @media screen {{
                {{
                @font-face {{
                        {{
                        font-family: 'Lato';
                        font-style: normal;
                        font-weight: 400;
                        src: local('Lato Regular'), local('Lato-Regular'), url(https://fonts.gstatic.com/s/lato/v11/qIIYRU-oROkIk8vfvxw6QvesZW2xOQ-xsNqO47m55DA.woff) format('woff');
                    }}
                }}

                @font-face {{
                        {{
                        font-family: 'Lato';
                        font-style: normal;
                        font-weight: 700;
                        src: local('Lato Bold'), local('Lato-Bold'), url(https://fonts.gstatic.com/s/lato/v11/qdgUG4U09HnJwhYI-uK18wLUuEpTyoUstqEm5AMlJo4.woff) format('woff');
                    }}
                }}

                @font-face {{
                        {{
                        font-family: 'Lato';
                        font-style: italic;
                        font-weight: 400;
                        src: local('Lato Italic'), local('Lato-Italic'), url(https://fonts.gstatic.com/s/lato/v11/RYyZNoeFgb0l7W3Vu1aSWOvvDin1pK8aKteLpeZ5c0A.woff) format('woff');
                    }}
                }}

                @font-face {{
                        {{
                        font-family: 'Lato';
                        font-style: italic;
                        font-weight: 700;
                        src: local('Lato Bold Italic'), local('Lato-BoldItalic'), url(https://fonts.gstatic.com/s/lato/v11/HkF_qI1x_noxlxhrhMQYELO3LdcAZYWl9Si6vvxL-qU.woff) format('woff');
                    }}
                }}
            }}
        }}

        /* CLIENT-SPECIFIC STYLES */
        body,
        table,
        td,
        a {{
                {{
                -webkit-text-size-adjust: 100%;
                -ms-text-size-adjust: 100%;
            }}
        }}

        table,
        td {{
                {{
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
            }}
        }}

        img {{
                {{
                -ms-interpolation-mode: bicubic;
            }}
        }}

        /* RESET STYLES */
        img {{
                {{
                border: 0;
                height: auto;
                line-height: 100%;
                outline: none;
                text-decoration: none;
            }}
        }}

        table {{
                {{
                border-collapse: collapse !important;
            }}
        }}

        body {{
                {{
                height: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
                width: 100% !important;
            }}
        }}

        /* iOS BLUE LINKS */
        a[x-apple-data-detectors] {{
                {{
                color: inherit !important;
                text-decoration: none !important;
                font-size: inherit !important;
                font-family: inherit !important;
                font-weight: inherit !important;
                line-height: inherit !important;
            }}
        }}

        /* MOBILE STYLES */
        @media screen and (max-width:600px) {{
                {{
                h1 {{
                        {{
                        font-size: 32px !important;
                        line-height: 32px !important;
                    }}
                }}
            }}
        }}

        /* ANDROID CENTER FIX */
        div[style*="margin: 16px 0;"] {{
                {{
                margin: 0 !important;
            }}
        }}
    </style>
</head>

<body style="background-color: #f4f4f4; margin: 0 !important; padding: 0 !important;">
    <!-- HIDDEN PREHEADER TEXT -->
    <div
        style="display: none; font-size: 1px; color: rgb(36, 122, 187); line-height: 1px; font-family: 'Lato', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">
    </div>
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <!-- LOGO -->
        <tr>
            <td bgcolor="#3498DB" align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td align="center" valign="top" style="padding: 40px 10px 40px 10px;"> <p></p></td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#3498DB" align="center" style="padding: 0px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">

                    <tr>
                        <td bgcolor="#ffffff" align="center" valign="top"
                            style="padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;">
                            <div align="left">
                                <img src="https://akumosolutions-public-templates.s3.us-east-2.amazonaws.com/Logo_Horizontal_AkumoSolutions.png"
                                    alt="logo" width="300" height="150" />
                            </div>
                            <img src="https://akumosolutions-public-templates.s3.us-east-2.amazonaws.com/thankyou.png" alt="">
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td bgcolor="#ffffff" align="left"
                            style="padding: 20px 30px 40px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <p style="margin: 0;">
                                Dear {} <br>
                                <br>
                                We truly appreciate your business, and we're grateful for the trust you've placed in us. Please don't hesitate to
                            contact us if you have any questions or concerns.</p>
                        </td>
                    </tr>
                    <tr>
                        <td bgcolor="#ffffff" align="left"
                            style="padding: 0px 30px 0px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <p style="margin: 0;">
                                We hope to have the pleasure of doing business with you for many years to come.
                            </p>
                        </td>
                    </tr>
                    <!-- COPY -->
                    <tr>
                        <td bgcolor="#ffffff" align="left"
                            style="padding: 20px 30px 20px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <p style="margin: 0;"><a href="#" target="_blank" style="color: #2bb9c9;"></a></p>
                        </td>
                    </tr>
                    <tr>
                        <td bgcolor="#ffffff" align="left"
                            style="padding: 0px 30px 40px 30px; border-radius: 0px 0px 4px 4px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <p style="margin: 0;">Best Regards,<br>aKumoSolutions Team</p>
                        </td>
                    </tr>
                    <tr>
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

                    <td align="center" valign="top">
                        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#3498DB;margin:0 auto;width:100%">
                            <tbody>
                                <tr>
                                    <td align="center" style="padding:40px 0">
                                        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="margin:0 auto;max-width:612px;width:90%">
                                            <tbody>
                                            <h2 align="center"> Contact Us</h2>
                                                <tr>
                                                    <td align="center" style="padding-bottom:20px">
                                                        <table border="0" cellpadding="10" cellspacing="0" role="presentation">
                                                            <tbody>
                                                                <tr>                      
                                                                    <td>
                                                                        <a href="https://www.facebook.com/pages/category/Information-Technology-Company/aKumoSolutions-100763001568331/">  <img alt="Facebook" border="0" src="https://akumosolutions-public-templates.s3.us-east-2.amazonaws.com/logos/1.png" target="_blank" class="fa fa-facebook-square" style="display:block;padding:0;outline:0;border:0;width:45px" width="45"> </a>
                                                                    </td>
                                                                    <td>
                                                                        <a href="https://akumosolutions.io/"> <img alt="Website" border="0" src="https://akumosolutions-public-templates.s3.us-east-2.amazonaws.com/logos/5.png" target="_blank" class="fa fa-chrome" style="display:block;padding:0;outline:0;border:0;width:45px" width="45"></a>
                                                                    </td>
                                                                    <td>
                                                                        <a href="https://github.com/akumosolutions"> <img alt="Github" border="0" src="https://akumosolutions-public-templates.s3.us-east-2.amazonaws.com/logos/2.png" target="_blank" class="fa fa-github-square" style="display:block;padding:0;outline:0;border:0;width:45px" width="45"></a>
                                                                    </td>
                                                                    <td>
                                                                        <a href="https://t.me/akumosolutions"> <img alt="Telegarm" border="0" src="https://akumosolutions-public-templates.s3.us-east-2.amazonaws.com/logos/4.png" target="_blank" class="fa fa-telegram" style="display:block;padding:0;outline:0;border:0;width:45px" width="45"></a>
                                                                    </td>
                                                                    <td>
                                                                        <a href="https://www.instagram.com/akumosolutions/">  <img alt="Facebook" border="0" src="https://akumosolutions-public-templates.s3.us-east-2.amazonaws.com/logos/3.png" target="_blank" class="fa fa-instagram" style="display:block;padding:0;outline:0;border:0;width:45px" width="45"></a>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="color:#ffffff;font-family:'Verdana',Arial,Helvetica,sans-serif;font-size:16px;line-height:22px;text-align:center">
                                                        <p style="margin:0;padding:0">
                                                            <br> aKumoSolutions
                                                            <br> 8755 Trumbull Ave, Suite 200,
                                                            <br> Skokie, IL 60076</p>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                    </tr>
                    <!-- COPY -->
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
    '''.format(name)


    # Record the MIME types of both parts - text/plain and text/html.
    # part1 = MIMEText(messsage, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    # msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login(me, 'PASSWORD HERE')
    mail.sendmail(me, you, msg.as_string())
    mail.quit()

    return

send_order_Mail()
