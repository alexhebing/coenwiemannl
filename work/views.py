from django.shortcuts import render
from .models import Work


def get_works_by_category(id, request):
    works = Work.objects.filter(art_publish=True).filter(
        art_cat__l_art_cat_id=id).order_by('-art_date')
    for work in works:
        add_caption(work, request)
    return works


def for_sale(request):
    works = Work.objects.filter(art_sold=False)
    context = {'works': works}
    return render(request, 'work/index.html', context)


def portraits(request):
    works = get_works_by_category(1, request)
    context = {'works': works}
    return render(request, 'work/index.html', context)


def objects(request):
    works = get_works_by_category(2, request)
    context = {'works': works}
    return render(request, 'work/index.html', context)


def surrealistic(request):
    works = get_works_by_category(3, request)
    context = {'works': works}
    return render(request, 'work/index.html', context)


def realistic(request):
    works = get_works_by_category(4, request)
    context = {'works': works}
    return render(request, 'work/index.html', context)


def add_caption(work, request):
    lan = 'nl'
    if 'language' in request.GET:
        lan = request.GET['language']

    work_type = work.art_type
    if lan == 'nl':
        title_label = "Titel"
        title = work.art_title_l1
        materials = work.art_material_l1
        if work.art_type:
            work_type =  work.art_type.l_art_type_l1
        dimension_label = 'Afmeting'
        created_with = 'Gecre&euml;erd met'
        sold = 'Verkocht'
        for_sale = 'Te koop'
    if lan == 'en':
        title_label = "Title"
        title = work.art_title_l2
        materials = work.art_material_l2
        if work.art_type:
            work_type =  work.art_type.l_art_type_l2
        dimension_label = 'Dimension'
        created_with = 'Collaborated with'
        sold = 'Sold'
        for_sale = 'For sale'
    
    caption = "&lt;p&gt;&lt;b&gt;{}: &lt;/b&gt;{}&lt;/p&gt;".format(
        title_label, title)
    caption = add_caption_line(
        work, caption, work_type, materials)
    if (work.art_dimension):
        caption = add_caption_line(
            work, caption, dimension_label, work.art_dimension)
    if (work.art_artist_worked_with):
        caption = add_caption_line(
            work, caption, created_with, work.art_artist_worked_with)
    if (work.art_sold):
        caption = "{}&lt;p&gt;({})&lt;/p&gt;".format(caption, sold)
    else:
        add_caption_line(work, caption, for_sale, work.art_price)
    work.caption = caption


def add_caption_line(work, caption, key, value):
    return "{}&lt;p&gt;&lt;b&gt;{}: &lt;/b&gt;{}&lt;/p&gt;".format(caption, key, value)
