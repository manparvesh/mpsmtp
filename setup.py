from setuptools import setup, find_packages


setup(name='mpsmtp',
      version='0.0.1',
      py_modules=['mpsmtp'],
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'Click',
          'requests',
          'nose'
      ],
      package_data={'': ['*.txt', '*.lst']},
      entry_points='''
        [console_scripts]
        mpsmtp=mpsmtp:cli
    ''',
      test_suite='nose.collector',
      tests_require=['nose'],
      )
