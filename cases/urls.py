from django.urls import path

from cases.api.get_visuals_data import UpdateVisualsData, UpdateYesterDayVisualsData
# from cases.api.kenyan_cases import KenyanCaseList
from cases.api.visuals import VisualList, CountryList, CountryDetailAPIView

urlpatterns = [
    # path('kenyan/all', KenyanCaseList.as_view(), name='Historical data'),
    # path('history/', VisualList.as_view(), name='Historical data'),
    path('country/', CountryList.as_view(), name='Historical data'),
    path('country/<str:name>', CountryDetailAPIView.as_view(), name='Historical data'),
    path('update/history', UpdateVisualsData.as_view(), name='Update Historical data'),
    path('update/yesterday', UpdateYesterDayVisualsData.as_view(), name='Update Historical data'),
]
