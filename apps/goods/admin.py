from django.contrib import admin

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
from .models import Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, Banner, HotSearchWords
from .models import IndexAd

class GoodsAdmin(admin.ModelAdmin):
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]
    search_fields = ['name', ]
    list_editable = ["is_hot", ]
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category__name"]
    style_fields = {"goods_desc": "ueditor"}

    class GoodsImagesInline(admin.StackedInline):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]


class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


class GoodsBrandAdmin(admin.ModelAdmin):
    list_display = ["category", "image", "name", "desc"]

    # def get_context(self):
    #     context = super(GoodsBrandAdmin, self).get_context()
    #     if 'form' in context:
    #         context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
    #     return context


class BannerGoodsAdmin(admin.ModelAdmin):
    list_display = ["goods", "image", "index"]


class HotSearchAdmin(admin.ModelAdmin):
    list_display = ["keywords", "index", "add_time"]


class IndexAdAdmin(admin.ModelAdmin):
    list_display = ["category", "goods"]


admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsCategory, GoodsCategoryAdmin)
admin.site.register(Banner, BannerGoodsAdmin)
admin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)

admin.site.register(HotSearchWords, HotSearchAdmin)
admin.site.register(IndexAd, IndexAdAdmin)

