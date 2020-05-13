import xadmin
from apps.courses.models import Course,Lesson,Video,CourseResource
#不用继承admin.ModelAdmin
class CourseAdmin(object):
    list_display=["id","name","learn_times","desc"]
    search_file=["name","desc"]
class LessonAdmin(object):
    pass
class VideoAdmin(object):
    pass
class CourseResourceAdmin(object):
    pass

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
