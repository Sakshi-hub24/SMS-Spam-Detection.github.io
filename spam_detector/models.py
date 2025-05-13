from django.db import models

class SMSBase(models.Model):
    sender = models.CharField(max_length=255)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # This makes it an abstract base class

class SpamSMS(SMSBase):
    reason_flagged = models.CharField(max_length=255, help_text="Reason why this message was flagged as spam")

    def __str__(self):
        return f"Spam from {self.sender}: {self.message[:30]}..."

class NonSpamSMS(SMSBase):
    is_reviewed = models.BooleanField(default=False, help_text="Indicates whether this non-spam message has been reviewed")

    def __str__(self):
        return f"Non-Spam from {self.sender}: {self.message[:30]}..."
