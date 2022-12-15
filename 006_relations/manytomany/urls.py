from django.urls import path
from .views import (
    createArticles,
    getArticleRelations,
    getPublicationsRelations,
    removeRelations,
)

urlpatterns = [
    path("create/articles/", createArticles, name="create/articles/"),
    path("get/article/relations", getArticleRelations, name="get/article/relations"),
    path(
        "get/publications/relations",
        getPublicationsRelations,
        name="get/publications/relations",
    ),
    path("remove/relations", removeRelations, name="remove/relations"),
]
