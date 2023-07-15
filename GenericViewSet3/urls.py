from rest_framework.routers import SimpleRouter
from GenericViewSet3 import views



router = SimpleRouter()
router.register('books3', views.GenericViewSetBook3, basename='books')
urlpatterns = router.urls