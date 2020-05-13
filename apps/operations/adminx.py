import xadmin
from apps.operations.models import UserCourse,Banner,UserAsk,UserFavorite,UserMessage,CourseComments
#不用继承admin.ModelAdmin
class UserCourseAdmin(object):
    # list_display=["id","name","learn_times","desc"]
    # search_file=["name","desc"]
    pass
class BannerAdmin(object):
    pass
class UserAskAdmin(object):
    pass
class CourseResourceAdmin(object):
    pass
class UserFavoriteAdmin(object):
    pass
class UserMessageAdmin(object):
    pass
class CourseCommentsAdmin(object):
    pass

xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)