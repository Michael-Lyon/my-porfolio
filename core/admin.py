from django.contrib import admin
from .models import (
    AboutMe,
    Education,
    Experience,
    Resume,
    Service,
    ServicesSection,
    Skill,
    SkillsSection,
    Project,
    ProjectsSection,
    BlogEntry,
    BlogSection,
    CounterSection,
    Contact,
)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('date', 'degree', 'university')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('date', 'position', 'company')

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('education', 'experience')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class')

class ServicesSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')

class SkillsSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

class ProjectsSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')

class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')

class BlogSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')

class CounterSectionAdmin(admin.ModelAdmin):
    list_display = ('awards', 'complete_projects', 'happy_customers', 'cups_of_coffee')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'address', 'zip_code', 'email', 'phone', 'projects_completed')
    search_fields = ('name', 'email', 'phone')

admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServicesSection, ServicesSectionAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillsSection, SkillsSectionAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectsSection, ProjectsSectionAdmin)
admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(BlogSection, BlogSectionAdmin)
admin.site.register(CounterSection, CounterSectionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(AboutMe, AboutMeAdmin)