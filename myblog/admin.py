from django.contrib import admin
from myblog.models import Blog, Category, Tag
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'create_time', 'modify_time']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'create_time', 'modify_time']

    def save_model(self, request, obj, form, change):
        obj.save()
        #博客分类数目统计
        obj_category = obj.category
        category_number = obj_category.blog_set.count()
        obj_category.number = category_number
        obj_category.save()
        #博客标签数目统计
        obj_tag_list = obj.tag.all()
        for obj_tag in obj_tag_list:
            tag_number = obj_tag.blog_set.count()
            obj_tag.number = tag_number
            obj_tag.save()
