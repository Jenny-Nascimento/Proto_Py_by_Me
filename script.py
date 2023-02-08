
from instapy import smart_run
from instapy import InstaPy

session = InstaPy(username='jennyeozepelim',
                  password='Efemac 3',
                  headless_browser=False,
                  want_check_browser=False)

with smart_run(session):
	session.set_do_follow(enable = True, percentage = 100)
	session.set_do_like(enable = True, percentage = 100)

	session.like_by_tags (['maternidadereal'], amount = 50)

	comentarios = ['Curti seu perfil!' ]
	session.set_do_comments(enable=True, percentage = 95)
	session.set_do_comments(comentarios, media= 'Photo')
	session.join_pods()
