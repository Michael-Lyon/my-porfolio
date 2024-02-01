from django.shortcuts import render

from core.models import AboutMe, Project, Resume, Service, ServicesSection, Skill, SkillsSection

# Create your views here.


def home(request):
    about = AboutMe.objects.all().first()
    resume_list = Resume.objects.all()
    skills_list = SkillsSection.objects.all().first()
    my_skills = Skill.objects.all()
    projects = Project.objects.all()
    services = ServicesSection.objects.all().first()
    return render(request, "core/index.html", {
        'about': about,
        'resume_list': resume_list,
        "skills_list": skills_list,
        "my_skills": my_skills,
        "services": services,
        "my_services": services.services.all(),
        "projects": projects
    })