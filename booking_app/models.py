from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    TYPE_CHOICES = [
        ("BC" , "Бізнес клас"),
        ("EC" , "Економ клас"),
        ("CC" , "Комфорт клас"),
        ("LC" , "Люкс клас")
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    capacity = models.IntegerField(default=2)
    image = models.ImageField(upload_to="media/rooms_image" , null=True , blank=True)
    room_type = models.CharField(max_length=80, choices=TYPE_CHOICES, default="Standart")

    def __str__(self):
        return f"{self.title}, {self.price}, {self.room_type}"
    

    class Meta:
        ordering = ["price" , "room_type"]
        verbose_name = "Номер"
        verbose_name_plural = "Номери"


class Booking(models.Model):
    STATUS = [
        ("New" , "Нове"),
        ("Verified" , "і"),
        ("Canceled", "Скасоване"),
        ("Completed" , "Закінчене")
    ]
    check_in = models.DateTimeField()
    chech_out = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    email = models.EmailField()
    status = models.CharField(max_length=255, choices=STATUS , default="new")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"#{self.room} from {self.check_in} to {self.chech_out}"
    

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-created_at"]