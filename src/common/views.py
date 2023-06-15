from common.mixins import GlobalSearchMixin
from drf_multiple_model.views import ObjectMultipleModelAPIView
from common.utils import LimitPagination


class GlobalSeacrh(ObjectMultipleModelAPIView, GlobalSearchMixin):
    pagination_class = LimitPagination

    def get_querylist(self):
        querylist = ()
        search = self.request.GET.get("search")

        if search:
            return self.global_querylist(querylist, search)
        return querylist
