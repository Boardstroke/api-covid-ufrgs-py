
from distutils.core import setup
setup(
  name = 'ApiCovidUfrgsPy',         # How you named your package folder (MyLib)
  packages = ['ApiCovidUfrgsPy'],   # Chose the same as "name"
  version = '0.1',
  license='MIT',
  description = 'Uma interface para acessar dados do servidor relacionado a covid no RS',
  author = 'Matheus Fachini',                   # Type in your name
  author_email = 'matheus.fachinis@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Boardstroke/api-covid-ufrgs-py',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Boardstroke/api-covid-ufrgs-py/archive/v0.1.tar.gz',    # I explain this later on
  keywords = ['API', 'COVID', 'RS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Science/Research'
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)