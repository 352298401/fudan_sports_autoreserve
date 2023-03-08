import apis
import logs

SERVICE_CATEGORY = "2c9c486e4f821a19014f82381feb0001"  # This is the category ID for "Sports Reservation". It usually doesn't change.

# Fill in these data
USER_ID = "22210240388"
USER_PASSWORD = "ZYKcr5959559"
CAMPUS_NAME = "邯郸校区"
SPORT_NAME = "羽毛球"
SPORT_LOCATION = "江湾体育馆羽毛球场"
DATE = "2023-03-09"
TIME = "12:00"

# Optional data
EMAILS = ["352298401@qq.com"]  # Receive error notifications by email
YOUR_EMAIL = "352298401@qq.com"  # Account to send email from
EMAIL_PASSWORD = "ZYKCR5959559"  # Password for the email account


if __name__ == '__main__':
    try:
        logged_in_session = apis.login(USER_ID, USER_PASSWORD)
        campus_id, sport_id = apis.load_sports_and_campus_id(logged_in_session, SERVICE_CATEGORY, CAMPUS_NAME, SPORT_NAME)
        service_id = apis.get_service_id(logged_in_session, SERVICE_CATEGORY, campus_id, sport_id, SPORT_LOCATION)
        apis.reserve(logged_in_session, service_id, SERVICE_CATEGORY, DATE, TIME)
    except Exception as e:
        if EMAILS:
            import smtplib
            import datetime
            message = f"Subject: Failed to reserve sport field\n\n{logs.FULL_LOG}"
            connection = smtplib.SMTP("smtp-mail.outlook.com", 587)
            try:
                connection.ehlo()
                connection.starttls()
                connection.login(YOUR_EMAIL, EMAIL_PASSWORD)
                connection.sendmail(YOUR_EMAIL, EMAILS, message)
            finally:
                connection.quit()
