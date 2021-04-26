from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'base'

urlpatterns = [
    path('',views.homeView,name='home'),
    path('add-to-cart/',views.addToCart,name='add-to-cart'),
    path('add-to-wishlist/',views.wishlist,name='add-to-wishlist'),
    path('wishlist_items/',views.wishlist_items,name='wishlist_items'),
    path('remove_wish/',views.remove_wish,name='removewish'),
    path('cart_items/',views.cart_items,name='cart_items'),
    path('increment/',views.increment,name='increment'),
    path('decrement/',views.decrement,name='decrement'),
    path('remove_item/',views.remove_item,name='removeitem'),
    path('checkout/',views.checkout,name='checkout'),
    path('payment_done/',views.payment_done,name='payment_done'),
    path('review_orders/',views.review_orders,name='review_orders'),
    # path('payment/', views.payment, name='payment'),
    # path('success/' , views.success , name='success'),

    # urls for product details page
    path('cake/',views.cake,name = 'cake'),
    path('special/',views.special,name = 'special'),
    path('chocolate/',views.chocolates,name = 'chocolate'),
    path('plant/',views.plants,name = 'plant'),
    path('bouquet/',views.bouquets,name = 'bouquet'),
    path('birth/',views.birth,name = 'birth'),
    path('anniversary/',views.anniversary,name = 'anniversary'),
    path('gifts/',views.gifts,name = 'gifts'),
    path('itemDetail/<int:id>',views.itemDetail,name='itemDetail'),
    path('filter/<int:flag>/<int:amount>/<int:cat>',views.filter_view,name='filter_view'),
    # path('^chat/filter/(?P<flag>[0-9])/(?P<amount>[0-9])/(?P<cat>[0-9])/$',views.filter_view,name='filter_view'),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)