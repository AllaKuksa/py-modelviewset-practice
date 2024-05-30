from django.urls import path

from author.views import AuthorViewSet

app_name = "author"

authors_list = AuthorViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})
authors_detail = AuthorViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("authors/", authors_list, name="manage-list"),
    path("authors/<int:pk>/", authors_detail, name="manage-detail"),
]
