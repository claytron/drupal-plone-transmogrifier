from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='my.policy',
      version=version,
      description="A policy package to manage a Plone installation",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zope plone policy',
      author='Six Feet Up, Inc.',
      author_email='info@sixfeetup.com',
      url='http://www.sixfeetup.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['my'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'my.migration',
          'collective.blog.star',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
