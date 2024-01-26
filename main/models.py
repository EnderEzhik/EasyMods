from django.db import models


class Version(models.Model):
    version = models.CharField("Версия", max_length=10)

    def __str__(self):
        return self.version
    
    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"


class Category(models.Model):
    name = models.CharField("Категория", max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Mod(models.Model):
    name = models.CharField("Название", max_length=50)
    url = models.CharField("Ссылка", max_length=250)
    version = models.ForeignKey(Version, on_delete=models.PROTECT)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Мод"
        verbose_name_plural = "Моды"