from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin import AdminSite
from django.utils.safestring import mark_safe

class MyAdminSite(AdminSite):
    site_header = "Brainy Beam Superadmin"
    site_title = "Brainy Beam Admin"
    index_title = "Welcome to Brainy Beam Superadmin"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_head'] = mark_safe("""
    <link rel="icon" type="image/png" href="/static/your_app/your_icon.png">
    <style>
        body { background: #22223b !important; }
        #header { background: red !important; }  /* Changed to red */
        .module h2, .module caption, .grp-module h2 { color: #f2e9e4 !important; }
        .dashboard-module, .module { background: #9a8c98 !important; }
        .button, input[type=submit], input[type=button] {
            background: #c9ada7 !important;
            color: #22223b !important;
        }
        #site-name img { height: 32px; vertical-align: middle; margin-right: 8px; }
    </style>
        """)
        return context

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        return urls

admin_site = MyAdminSite(name='myadmin')

admin_site.register(User, BaseUserAdmin)

admin.site.site_header = "Brainy Beam Superadmin"
admin.site.site_title = "Brainy Beam Admin"
admin.site.index_title = "Welcome to Brainy Beam Superadmin"