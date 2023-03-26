from simple_history import register
from django.contrib import admin
from BookNirvana.models import Book,User,Shelf,Review
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html
# Register your models here.

class BookAdmin(SimpleHistoryAdmin):
    list_display = ["id", "title", "history"]
    history_list_display = ["status"]
    search_fields = ['title',"id"]

    pass
class ShelfAdmin(SimpleHistoryAdmin):
    search_fields = ["id","name"]
    pass
class ReviewAdmin(SimpleHistoryAdmin):
    search_fields = ["id"]
    pass
class UserAdmin(SimpleHistoryAdmin):
    history_list_display = ["changed_fields","list_changes"]
    
    def changed_fields(self, obj):
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            return delta.changed_fields
        return None

    def list_changes(self, obj):
        fields = ""
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            

            for change in delta.changes:
                fields += str("<strong>{}</strong> changed from <span style='background-color:#ffb5ad'>{}</span> to <span style='background-color:#b3f7ab'>{}</span> . <br/>".format(change.field, change.old, change.new))
                
            # return format_html(fields)
        return None
# register(User)
admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Shelf, ShelfAdmin)
admin.site.register(Review, ReviewAdmin)