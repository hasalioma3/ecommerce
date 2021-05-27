from django import db
from django.db import models
from django.contrib.auth import User
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.models.OneToOneField("User", verbose_name=_(
        "Staff"), on_delete=models.CASCADE, blank=True, null=True)
    Location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Make:
        db_table = 'Category'
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Make(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Make:
        db_table = 'Make'
        verbose_name = "Make"
        verbose_name_plural = "Makes"


class AModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    make = models.ForeignKey(
        Make, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Make:
        db_table = 'Model'
        verbose_name = "Model"
        verbose_name_plural = "Models"


class Asset(models.Model):
    make = models.ForeignKey(
        Make, on_delete=models.CASCADE, null=True, blank=True)
    amodel = models.ForeignKey(
        AModel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(
        Make, on_delete=models.CASCADE, null=True, blank=True)
    barcode = models.CharField(max_length=200, null=True, blank=True)
    serialNo = models.CharField(max_length=200, null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    lpoNumber = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Assets'
        verbose_name = "Asset"
        verbose_name_plural = "Assets"


class DeliveryNotes(models.Model):
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, null=True, blank=True)
    dateDispatched = models.DateTimeField(auto_now_add=True)
    dispatched = models.BooleanField(default=False)
    deliveryNoteNo = models.CharField(max_length=200, null=True, blank=True)
    fromLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null=True,
                                     blank=True, related_name="FromLocation", verbose_name="From Location")
    toLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null=True,
                                   blank=True, related_name="ToLocation", verbose_name="To Location")

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'DeliveryNotes'
        verbose_name = "DeliveryNote"
        verbose_name_plural = "DeliveryNotes"


class DeliveryItems(models.Model):
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.ForeignKey(
        DeliveryNotes, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    dateDispatched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.asset.name)

    class Meta:
        db_table = 'DeliveryItems'
        managed = True
        verbose_name = 'DeliveryItem'
        verbose_name_plural = 'DeliveryItems'
