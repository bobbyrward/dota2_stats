import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    ]

setup(name='dota2_stats',
      version='0.0',
      description='dota2_stats',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='dota2_stats',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = dota2_stats:main
      [console_scripts]
      populate_items = dota2_stats.scripts.populate_items:main
      populate_heroes = dota2_stats.scripts.populate_heroes:main
      populate_matches = dota2_stats.scripts.populate_matches:main
      populate_players = dota2_stats.scripts.populate_players:main
      """,
      )
