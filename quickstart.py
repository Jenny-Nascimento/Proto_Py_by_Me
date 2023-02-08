""" Quickstart script for InstaPy usage """

# imports
from email.quoprimime import header_check
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy (username='jennyeozepelim', password= 'Efemac 3', headless_browser=False, want_check_browser=False)

with smart_run(session):
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    session.like_by_tags(["natgeo"], amount=10)