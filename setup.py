from distutils.core import setup
setup(
  name = 'cs1andalus',         # How you named your package folder (MyLib)
  packages = ['cs1andalus'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'cs1 graphical modules for educational purpose',   # Give a short description about your library
  author = 'Mukerem Ali',                   # Type in your name
  author_email = 'mukeremali112@domain.com',      # Type in your E-Mail
  url = 'https://github.com/mukerem/cs1andalus',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mukerem/cs1andalus/archive/v_01.tar.gz',    # I explain this later on
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Students',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 2.7',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)