from django.shortcuts import render

from projects.models import ProjectModel


# Create your views here.
def project_index(request):
    # Get all projects
    projects = ProjectModel.objects.all()
    context = {
        "title": 'Projects',
        'projects': projects
    }
    return render(request, template_name='projects/project_index.html', context=context)


def project_detail(request, id):
    project = ProjectModel.objects.get(pk=id)
    context = {
        "title": 'Project Detail',
        "project_detail": project
    }
    return render(request, template_name='projects/project_detail.html', context=context)
