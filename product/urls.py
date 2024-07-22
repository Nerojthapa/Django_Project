from django.urls import path
from .views import *
# from .views import pattern_view
# from .views import palindrome_view
# from .views import match_number_view

# urlpatterns = [
#     path('index/',pattern_view,name='index')
# ]

# urlpatterns = [
#     path('index/<int:number>/',palindrome_view,name='index')
# ]


# urlpatterns = [
#     path('index/<int:number>/',match_number_view,name='index')
# ]

urlpatterns = [
    path('home/',home,name='home'),
    path('addproduct/', addproduct, name='addproduct'),
    path('updateproduct/<int:product_id>', updateproduct, name='updateproduct'),
    path('deleteproduct/<int:product_id>', deleteproduct, name='deleteproduct'),
    path('categorylist',categorylist,name='categorylist'),
    path('addcategory/', addcategory, name='addcategory'),
    path('updatecategory/<int:category_id>',updatecategory, name='updatecategory'),
    path('deletecategory/<int:category_id>', deletecategory, name='deletecategory')
    
]
