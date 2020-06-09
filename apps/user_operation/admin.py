from django.contrib import admin

#!/usr/bin/env python
# encoding: utf-8

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

from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(admin.ModelAdmin):
    list_display = ['user', 'goods', "add_time"]


class UserLeavingMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message_type', "message", "add_time"]


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ["signer_name", "signer_mobile", "district", "address"]

admin.site.register(UserFav, UserFavAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)