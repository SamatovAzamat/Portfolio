from django.contrib import admin
from main.models import ContactModel, PostModel


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'created_at']
    list_filter = [
        'created_at']  # list filit 2ta tipdagi po'lya uchu ishlatiladi
    # 1) bu vaqtka aloqador polyalar uchun
    # 2) bog'langan po'lyalar uchun boladi
    search_fields = ['name', 'email', 'subject', 'message']  # search bu qidirishga

# Register your models here.


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['header', 'image',  'body', 'created_at']

    @admin.action(description="Faollashtirish")
    def carousel_status_active(modeladmin, request, queryset):
        queryset.update(status=PostModel.STATUS_ACTIVE)

    @admin.action(description="Nofaollashtirish")
    def carousel_status_inactive(modeladmin, request, queryset):
        queryset.update(status=PostModel.STATUS_INACTIVE)
