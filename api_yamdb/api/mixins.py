from rest_framework import mixins, viewsets


class GetPostDelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """
    Кастомный миксин для создания, запроса списка и удаления объектов.
    """
    pass
