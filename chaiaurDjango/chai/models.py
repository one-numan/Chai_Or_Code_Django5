from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return F'{self.name}'


# One to Many
class ChaiReview(models.Model):
    chai = models.ForeignKey(
        ChaiVarity, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return F'{self.user.username} Reviews for {self.chai.name}'


# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ChaiVarity = models.ManyToManyField(ChaiVarity, related_name='store')

    def __str__(self):
        return F'{self.name}'

# One to One


class ChaiCertificate(models.Model):
    chai = models.OneToOneField(
        ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self) -> str:
        return F'Certificate for {self.chai}'
