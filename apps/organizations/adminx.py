import xadmin
from apps.organizations.models import City,Teacher,CourseOrg
#不用继承admin.ModelAdmin
class CityAdmin(object):
    # list_display=["id","name","learn_times","desc"]
    # search_file=["name","desc"]
    pass
class TeacherAdmin(object):
    pass
class CourseOrgAdmin(object):
    pass
class CourseResourceAdmin(object):
    pass

xadmin.site.register(City,CityAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)