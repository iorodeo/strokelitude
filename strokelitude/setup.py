from setuptools import setup, find_packages

setup(name='strokelitude',
      description='realtime wingstroke amplitude analyzer (fview plugin)',
      version='0.2',
      entry_points = {
    'motmot.fview.plugins':
    'strokelitude = strokelitude.strokelitude:StrokelitudeClass',
    'console_scripts' : ['hfive2mat=hfive2mat:main']
    },

      packages = find_packages(),
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      zip_safe=True,
      )
