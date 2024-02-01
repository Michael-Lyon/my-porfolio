from django.db import models

class Education(models.Model):
    date = models.CharField(max_length=20)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    description = models.TextField()

class Experience(models.Model):
    date = models.CharField(max_length=20)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

class Resume(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE, blank=True, null=True)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, blank=True, null=True)


class Service(models.Model):
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50)
    description = models.TextField()

class ServicesSection(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100)
    intro_paragraph = models.TextField()
    services = models.ManyToManyField(Service)

class Skill(models.Model):
    title = models.CharField(max_length=100)
    value = models.IntegerField()


class SkillsSection(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100)
    intro_paragraph = models.TextField()
    skills = models.ManyToManyField(Skill)


class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True, null=True)

class ProjectsSection(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100)
    intro_paragraph = models.TextField()
    projects = models.ManyToManyField(Project)


class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    meta_chat = models.IntegerField()
    content = models.TextField()

class BlogSection(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100)
    intro_paragraph = models.TextField()
    blog_entries = models.ManyToManyField(BlogEntry)


class CounterSection(models.Model):
    awards = models.IntegerField(default=0)
    complete_projects = models.IntegerField(default=0)
    happy_customers = models.IntegerField(default=0)
    cups_of_coffee = models.IntegerField(default=0)



class Contact(models.Model):
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.CharField(max_length=200)


class AboutMe(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    bio = models.TextField(default="Hello world")
    zip_code = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    projects_completed = models.IntegerField()

    def __str__(self):
        return self.name