from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='cisindia.policy',
      version=version,
      description="CIS India Plone Site Policy",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Inigo Consulting',
      author_email='team@inigo-tech.com',
      url='http://github.com/cisindia/cisindia.buildout',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['cisindia'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'plone.namedfile [blobs]',
          'collective.grok',
          # -*- Extra requirements: -*-
          'fullmarks.mathjax',
          'fullmarks.tinymceplugins.asciimath',
          'p4a.ploneaudio',
          'p4a.plonevideo',
          'p4a.plonevideoembed',
          'Products.NuPlone',
          'Products.PloneHotfix20110928',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
           ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],

      )
