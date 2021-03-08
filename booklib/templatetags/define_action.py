from django import template
register = template.Library()
import datetime
@register.simple_tag
def define(issue_date):
    datetime.datetime.strptime(issue_date, "%Y,%m,%d").date()
    cur_date=datetime.date.today()
    x=(cur_date-issue_date).days
    if x>15:
        return x*2
    else:
        return 0