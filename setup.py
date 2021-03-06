from distutils.core import setup
setup(
  name = 'cs1andalus',         # How you named your package folder (MyLib)
  packages = ['cs1andalus'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'cs1 graphical modules for educational purposes',   # Give a short description about your library
  author = 'Mukerem Ali',                   # Type in your name
  author_email = 'mukeremali112@domain.com',      # Type in your E-Mail
  url = 'https://github.com/mukerem/cs1andalus',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mukerem/cs1andalus/archive/refs/tags/v1.0.tar.gz',    # I explain this later on
  install_requires=[        
          'Pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Education',    
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
