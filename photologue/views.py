from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.date_based import object_detail, archive_day, \
                                    archive_month, archive_year, archive_index
from django.views.generic.list_detail import object_detail, object_list
from models import Gallery

# Number of random images from the gallery to display.
SAMPLE_SIZE = ":%s" % getattr(settings, 'GALLERY_SAMPLE_SIZE', 5)

@login_required
def  galleries_index(request):
    """ Displays current user's galleries.
    Extended to support users.
    """
    user_galleries =  {'date_field': 'date_added', 
                    'allow_empty': True, 
                    'queryset': Gallery.objects.filter(is_public=True, author=request.user), 
                    'extra_context':{'sample_size':SAMPLE_SIZE}
                    }
    return archive_index(request,  **user_galleries)

@login_required
def  all_galleries(request, page):
    """ Displays current user's galleries paginated. 
    Extended to support users.
    """
    user_galleries =  {'queryset': Gallery.objects.filter(is_public=True, author=request.user), 
                    'page': page,
                    'allow_empty': True, 
                    'paginate_by': 2, 
                    'extra_context':{'sample_size':SAMPLE_SIZE}
                    }
    return object_list(request,  **user_galleries)

@login_required
def  show_gallery(request, slug):
    """ Shows selected gallery thumbnail. 
    Extended to support users.
    """
    user_gallery =  {'slug_field': 'title_slug', 
                    'slug': slug,
                    'queryset': Gallery.objects.filter(is_public=True,  author=request.user), 
                    'extra_context':{'sample_size':SAMPLE_SIZE}
                    }
    return object_detail(request,  **user_gallery)