from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    pub_title = models.TextField()
    pub_description = models.TextField()

    def __str__(self):
        return self.pub_title


class Friend(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name="book_author")
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='book_publisher', null=True, blank=True)
    hold_by = models.ForeignKey('Friend', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='book_images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title


