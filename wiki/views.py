from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class PageList(ListView):
    """
    CHALLENGES:
      1. On GET, display a homepage that shows all Pages in your wiki.
      2. Replace this CHALLENGE text with a descriptive docstring for PageList.
      3. Replace pass below with the code to render a template named `list.html`.
    """
    model = Page
    context_object_name = "pages"
    template_name = "list.html"

    # def get(self, request):
    #   """ Returns a list of wiki pages. """
    #   pages = Page.objects.all()
    #   return render(request, 'list.html', {
    #     "pages" : pages
    #   })


class PageDetailView(DetailView):
    """
    Render page.html
    """
    model = Page
    context_object_name = "page"
    template_name = "page.html"

    def get(self, request, slug):
    """ Returns a specific of wiki page by slug. """
      
      page = Page.objects.get(slug)
      return render(request, 'page.html', {
        "page" : page
      })

    def post(self, request, slug):
        pass
