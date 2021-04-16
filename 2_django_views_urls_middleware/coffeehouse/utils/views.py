from django.shortcuts import render

def page_not_found(request, exception):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request,'404.html',values_for_template,status=404)

def server_error(request):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request,'500.html',values_for_template,status=500)

def bad_request(request, exception):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request,'400.html',values_for_template,status=400)

def permission_denied(request, exception):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request,'403.html',values_for_template,status=403)
