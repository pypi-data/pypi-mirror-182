from setuptools import setup, find_packages
try:
    from . import __version__
except:
    import __version__
version = __version__.version
import os, sys
#import shutil

NAME = "hxfile"

def get_version():
    """Get version and version_info without importing the entire module."""
    print("NAME:", NAME)
    path = os.path.join(os.path.dirname(__file__), NAME, '__meta__.py')

    if sys.version_info.major == 3:
        import importlib.util

        spec = importlib.util.spec_from_file_location("__meta__", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        vi = module.__version_info__
        print("vi:", vi)
        print("type(vi):", type(vi))
        print("vi._get_canonical():", vi._get_canonical())
        print("vi._get_dev_status():", vi._get_dev_status())
        return vi._get_canonical(), vi._get_dev_status()
    else:
        import imp
        try:
            vi = imp.load_source("meta", "__meta__.py")
        except:
            vi = imp.load_source("meta", os.path.join(NAME, "__meta__.py"))
        return vi.__version__, vi.__status__

def get_requirements(req):
    """Load list of dependencies."""

    install_requires = []
    with open(req) as f:
        for line in f:
            if not line.startswith("#"):
                install_requires.append(line.strip())
    return install_requires


def get_description():
    """Get long description."""

    desc = ''

    if os.path.isfile('README.md'):
        with open("README.md", 'r') as f:
            desc = f.read()
    return desc

VER, DEVSTATUS = get_version()

try:
    os.remove(os.path.join(NAME, '__version__.py'))
except:
    pass
#try:
    #shutil.copy2('__version__.py', NAME)
    #shutil.copy2('hxfile.py', NAME)
    #shutil.copy2('__meta__.py', NAME)
    #shutil.copy2('__main__.py', NAME)
#except:
    #pass

entry_points = {
    "console_scripts": [
        "hxfile = hxfile.__main__:usage",
    ]
}

if sys.version_info.major == 3:
    entry_points = {
        "console_scripts": [
        "hxfile3 = hxfile.__main__:usage",
    ]
    }

setup(
    name = NAME,
    version=VER or version,
    author = 'Hadi Cahyadi LD',
    author_email = 'cumulus13@gmail.com',
    description = ('unofficial HXFILE API (still maintenance, open contributor)'),
    long_description = get_description(),
    long_description_content_type = 'text/markdown', 
    license = 'MIT License',
    keywords = ['hxfile', 'api', 'unoffcial', 'link generator', 'generator', 'download', 'downloader', 'cloud', 'file manager', 'cli', 'command line', 'unofficial HXFILE API (still maintenance, open contributor'],
    url = 'https://github.com/cumulus13/hxfile',
    scripts = [],
    # py_modules = [NAME],
    packages = [NAME],
    download_url = 'https://github.com/cumulus13/hxfile/tarball/master',
    install_requires=get_requirements('requirements.txt'),
    entry_points = entry_points,
    python_requires=">=2.7",
    classifiers=[
        'Development Status :: %s' % DEVSTATUS,
        'Environment :: Console',
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
