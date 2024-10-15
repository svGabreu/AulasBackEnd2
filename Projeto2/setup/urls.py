from django.contrib import admin
from django.urls import path

# from todos.views import home
# from todos.views import todo_list
from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView


# urlpatterns = [path("admin/", admin.site.urls), path("", home)]

# urlpatterns = [path("admin/", admin.site.urls), path("", todo_list)]

# urlpatterns = [path("admin/", admin.site.urls), path("", TodoListView.as_view())]

# urlpatterns = [path("admin/", admin.site.urls),
#    path("", TodoListView.as_view()),
#    path("create", TodoCreateView.as_view())]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create/<int:pk>", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
]
