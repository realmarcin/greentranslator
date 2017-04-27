from distutils.core import setup 
setup(
      name = 'greentranslator',
      packages = [ 'greentranslator' ], # this must be the same as the name above
      package_dir={ 'greentranslator' : 'greentranslator' },
      package_data={ 'greentranslator' : [ 'query/*.sparql' ]},
      version = '0.13',
      description = 'Green Team BioMedical Data Translator',
      author = 'Steve Cox',
      author_email = 'scox@renci.org',
      include_package_data=True,
      url = 'https://github.com/stevencox/greentranslator.git',
      download_url = 'https://github.com/stevencox/greentranslator/archive/0.13.tar.gz',
      keywords = [ 'biomedical', 'environmental', 'exposure', 'clinical' ],
      classifiers = [ ],
    )
