import os
from jenkinsutils import BuildHelper

package = 'TemplatingBWC'
type = 'install'

bh = BuildHelper(package, type)

# delete & re-create the venv
bh.venv_create()

# install package
bh.vecall('pip', 'install', package)

# change directory to one up so that we don't import the relative directory
# with our "test" below
os.chdir('..')

# import module as our "test"
bh.vecall('python', '-c', 'import templatingbwc')
