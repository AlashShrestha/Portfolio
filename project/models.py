from django.db import models


# Create your models here.
class Education(models.Model):
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    degree = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Link(models.Model):
    url = models.URLField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.icon


class Experience(models.Model):
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"


class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education = models.ManyToManyField(Education)
    skills = models.ManyToManyField(Skill)
    languages = models.ManyToManyField(Language)
    experiences = models.ManyToManyField(Experience)
    links = models.ManyToManyField(Link)
    image = models.ImageField()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
