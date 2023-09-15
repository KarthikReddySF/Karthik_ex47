try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
# import collections
# collections.Callable = collections.abc.Callable
config={
    'description':"Project 1",
    'author':'Karthik Y C',
    'url':'URL to get it at',
    'download_url':'where to download it',
    'author_email':'My email',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'script':[],
    'name':'projectname'
}
setup(**config)