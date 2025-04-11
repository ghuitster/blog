AUTHOR = 'David'
SITENAME = 'David Barley'
SITESUBTITLE = 'About, Resume, and Blog'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = "./theme/gum"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = [
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Social widget
SOCIAL = (
    ("Bluesky", "https://bsky.app/profile/davidmbarley.com"),
    ("Facebook", "https://www.facebook.com/david.m.barley"),
    ("LinkedIn", "https://www.linkedin.com/in/david-barley-7629367b/"),
    ("GitHub", "https://github.com/ghuitster"),
)

DEFAULT_PAGINATION = 10
