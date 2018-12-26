def auth_context(request):

    context = {
        'authed': False,
        'user': '',
    }

    if request.user.is_authenticated:
        context['authed'] = True,
        context['user'] = request.user.username

    return context
