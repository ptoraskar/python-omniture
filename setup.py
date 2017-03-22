from setuptools import setup, find_packages

setup(name='omni2re',
      description='A wrapper for the Adobe Omniture and SiteCatalyst web analytics API.',
      long_description='Please see README.md at http://github.com/colemanja91/python-omniture/',
      author='Stijn Debrouwere, Jeremiah Coleman',
      author_email='stijn@stdout.be, colemanja91@gmail.com',
      url='http://github.com/colemanja91/python-omniture/',
      download_url='http://www.github.com/colemanja91/python-omniture/tarball/master',
      version='0.4.1',
      license='MIT',
      packages=find_packages(),
      keywords='data analytics api wrapper adobe',
      install_requires=[
            'requests',
            'python-dateutil',
      ],
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   ],
      )
