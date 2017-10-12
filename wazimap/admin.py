from django.contrib import admin

from .models import Dataset, Release, SimpleTable, FieldTable, DBTable, FieldTableRelease


admin.site.register(SimpleTable)
admin.site.register(DBTable)


class FieldTableReleaseInline(admin.TabularInline):
    model = FieldTableRelease
    fields = ('release', 'db_table')
    extra = 0


@admin.register(FieldTable)
class FieldTableAdmin(admin.ModelAdmin):
    list_display = ('fields', 'universe', 'dataset')
    inlines = (FieldTableReleaseInline, )


class ReleaseInline(admin.StackedInline):
    model = Release
    fields = ('name', 'year')
    extra = 0


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    inlines = (ReleaseInline, )