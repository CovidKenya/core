from django.urls import path

from cases.api.get_visuals_data import UpdateVisualsData
from cases.api.kenyan_cases import KenyanCaseList
from cases.api.visuals import VisualList

urlpatterns = [
    path('kenyan/all', KenyanCaseList.as_view(), name='Historical data'),
    path('history/', VisualList.as_view(), name='Historical data'),
    path('update/history', UpdateVisualsData.as_view(), name='Update Historical data'),

]
