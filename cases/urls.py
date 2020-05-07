from django.urls import path

from cases.api.visuals import VisualList

urlpatterns = [
    path('history/', VisualList.as_view(), name='Historical data'),

]
