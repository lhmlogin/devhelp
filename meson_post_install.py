#!/usr/bin/env python3

import os
import subprocess
import sys

if not os.environ.get('DESTDIR'):
  icondir = os.path.join(sys.argv[1], 'icons', 'hicolor')
  print('Update icon cache...')
  subprocess.call(['gtk-update-icon-cache', '-f', '-t', icondir])

  schemadir = os.path.join(sys.argv[1], 'glib-2.0', 'schemas')
  print('Compiling gsettings schemas...')
  subprocess.call(['glib-compile-schemas', schemadir])

  install_prefix = os.environ['MESON_INSTALL_PREFIX']
  print('Byte-compiling python modules...')
  subprocess.call(['pycompile', install_prefix])
  subprocess.call(['python', '-O', '-m', 'compileall', '-f', '-q', install_prefix])
