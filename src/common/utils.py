from random import choices
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination

activate_code = "".join(choices("0123456789", k=6))


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 6
