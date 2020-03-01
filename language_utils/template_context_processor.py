def language_processor(request):
    lan = 'nl'
    if 'language' in request.GET:
        lan = request.GET['language']            
    return {'language': lan}