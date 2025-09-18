from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import Blog


class BlogsListView(ListView):
    model = Blog
    template_name = 'blogs.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_sign=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'create.html'
    fields = ("title", "content", "image", "publication_sign")
    success_url = reverse_lazy('blogs:blogs')


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'update.html'
    fields = ("title", "content", "image", "publication_sign")
    success_url = reverse_lazy('blogs:blogs')

    def get_success_url(self):
        return reverse('blogs:blog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('blogs:blogs')


