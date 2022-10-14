from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MyReactView(TemplateView):
    template_name = 'base.html'

    # def get_context_data(self, **kwargs):
    #     return {'context_variable': 'value'}

tracker_home_view = MyReactView.as_view()