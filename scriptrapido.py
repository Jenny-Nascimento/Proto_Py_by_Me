# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
from regex import R


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username='jennyeozepelim', password= 'xxxxxxx', use_firefox= 'true')

with smart_run(session):
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    session.like_by_tags(["natgeo"], amount=10)
