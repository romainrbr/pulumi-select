from distutils.core import setup
setup(
  name = 'pulumi_select',
  packages = ['pulumi_select'],
  version = '0.1.3', 
  license='WTFPL',
  description = 'dynamically select urns to apply from a pulumi preview',
  author = 'romainrbr',
  author_email = 'contact@romain.tech',
  url = 'https://github.com/romainrbr/pulumi-select',
  download_url = 'https://github.com/romainrbr/pulumi-select/archive/v_01.tar.gz',
  keywords = ['pulumi', 'select'],
  install_requires=[            
          'blessed',
          'click',
          'click-spinner',
          'inquirer',
          'python-editor',
          'readchar',
          'six',
          'wcwidth'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',    
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
  entry_points={
        "console_scripts": [
            "pulumi-select = pulumi_select.__main__:main"
        ]
    }


)