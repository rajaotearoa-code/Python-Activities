from abc import ABC, abstractmethod


# ==========================================
# PART 1: The Product Interface & Products
# ==========================================
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"[Email] Sending: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS] Sending: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"[Push] Sending: {message}")


# ==========================================
# PART 2: The Factory Interface & Factories
# ==========================================
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass


class EmailFactory(NotificationFactory):
    def create_notification(self):
        return EmailNotification()


class SMSFactory(NotificationFactory):
    def create_notification(self):
        return SMSNotification()


class PushFactory(NotificationFactory):
    def create_notification(self):
        return PushNotification()


# ==========================================
# PART 3: The Client Code
# ==========================================
def send_alert(factory, message):
    notification = factory.create_notification()
    notification.send(message)


if __name__ == "__main__":
    email_factory = EmailFactory()
    sms_factory = SMSFactory()
    push_factory = PushFactory()

    send_alert(email_factory, "Server CPU load exceeds 95%!")
    send_alert(sms_factory, "Unauthorized login detected.")
    send_alert(push_factory, "New software update available.")

    