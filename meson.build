project(
  'Devhelp', 'c',
  version: '3.26.0',
  license: 'GPL2+',
  default_options: [
    'b_lundef=true',
    'buildtype=debugoptimized',
    'warning_level=1'
  ],
  meson_version: '>= 0.42.0'
)

devhelp_name = meson.project_name().to_lower()

devhelp_version = meson.project_version()
version_array = devhelp_version.split('.')
devhelp_major_version = version_array[0].to_int()
devhelp_minor_version = version_array[1].to_int()
devhelp_micro_version = version_array[2].to_int()

devhelp_api_version = '@0@.0'.format(devhelp_major_version)
devhelp_api_name = '@0@-@1@'.format(devhelp_name, devhelp_api_version)

devhelp_gir_version = '1.0'

devhelp_prefix = get_option('prefix')
devhelp_bindir = join_paths(devhelp_prefix, get_option('bindir'))
devhelp_datadir = join_paths(devhelp_prefix, get_option('datadir'))
devhelp_includedir = join_paths(devhelp_prefix, get_option('includedir'))
devhelp_libdir = join_paths(devhelp_prefix, get_option('libdir'))
devhelp_localedir = join_paths(devhelp_prefix, get_option('localedir'))
devhelp_mandir = join_paths(devhelp_prefix, get_option('mandir'))

devhelp_pkgdatadir = join_paths(devhelp_datadir, devhelp_name)
devhelp_pkgincludedir = join_paths(devhelp_includedir, devhelp_api_name)

# LT Version numbers, remember to change them just *before* a release.
# A good time to update it is for the GNOME x.y.90 version, at API freeze,
# so that packagers have the time to update the package.
#   (Interfaces removed:    CURRENT++, AGE=0, REVISION=0)
#   (Interfaces added:      CURRENT++, AGE++, REVISION=0)
#   (No interfaces changed:                   REVISION++)
libdevhelp_current = 4
libdevhelp_revision = 0
libdevhelp_age = 0
libdevhelp_version = '@0@.@1@.@2@'.format(libdevhelp_current, libdevhelp_revision, libdevhelp_age)

libdevhelp_name = '@0@-@1@'.format(devhelp_name, devhelp_major_version)

devhelp_debug = get_option('buildtype').contains('debug')

# package
package = devhelp_name
package_bugreport = 'http://bugzilla.gnome.org/enter_bug.cgi?product=' + meson.project_name()
package_name = meson.project_name()
package_string = '@0@ @1@'.format(meson.project_name(), devhelp_version)
package_tarname = devhelp_name
package_url = 'https://wiki.gnome.org/Apps/Devhelp'
package_version = devhelp_version

cc = meson.get_compiler('c')

config_h = configuration_data()

# defines
set_defines = [
  # package
  ['PACKAGE', package],
  ['PACKAGE_BUGREPORT', package_bugreport],
  ['PACKAGE_NAME', package_name],
  ['PACKAGE_STRING', package_string],
  ['PACKAGE_TARNAME', package_tarname],
  ['PACKAGE_URL', package_url],
  ['PACKAGE_VERSION', package_version],
  ['VERSION', package_version],
  # i18n
  ['GETTEXT_PACKAGE', devhelp_name]
]

foreach define: set_defines
  config_h.set_quoted(define[0], define[1])
endforeach

# headers
check_headers = [
  ['HAVE_DLFCN_H', 'dlfcn.h'],
  ['HAVE_INTTYPES_H', 'inttypes.h'],
  ['HAVE_MEMORY_H', 'memory.h'],
  ['HAVE_STDINT_H', 'stdint.h'],
  ['HAVE_STDLIB_H', 'stdlib.h'],
  ['HAVE_STRINGS_H', 'strings.h'],
  ['HAVE_STRING_H', 'string.h'],
  ['HAVE_SYS_STAT_H', 'sys/stat.h'],
  ['HAVE_SYS_TYPES_H', 'sys/types.h'],
  ['HAVE_UNISTD_H', 'unistd.h']
]

foreach header: check_headers
  config_h.set(header[0], cc.has_header(header[1]))
endforeach

# functions
check_functions = [
  # i18n
  ['HAVE_DCGETTEXT', 'dcgettext'],
  ['HAVE_GETTEXT', 'gettext'],
  ['HAVE_ICONV', 'iconv']
]

if host_machine.system().contains('darwin')
  check_functions += [
    ['HAVE_CFLOCALECOPYCURRENT', 'CFLocaleCopyCurrent'],
    ['HAVE_CFPREFERENCESCOPYAPPVALUE', 'CFPreferencesCopyAppValue']
  ]
endif

foreach func: check_functions
  config_h.set(func[0], cc.has_function(func[1]))
endforeach

# compiler flags
common_flags = ['-DHAVE_CONFIG_H']

if devhelp_debug
  test_cflags = [
    '-fno-strict-aliasing',
    '-Wcast-align',
    '-Wdeclaration-after-statement',
    '-Wformat-nonliteral',
    '-Wformat=2',
    '-Winit-self',
    '-Winline',
    '-Wmissing-declarations',
    '-Wmissing-format-attribute',
    '-Wmissing-include-dirs',
    '-Wmissing-noreturn',
    '-Wmissing-prototypes',
    '-Wnested-externs',
    '-Wno-error=missing-field-initializers',
    '-Wno-error=unused-parameter',
    '-Wno-missing-field-initializers',
    '-Wno-unused-parameter',
    '-Wold-style-definition',
    '-Wpacked',
    '-Wpointer-arith',
    '-Wredundant-decls',
    '-Wshadow',
    '-Wstrict-prototypes',
    '-Wswitch-enum',
    '-Wundef',
    '-Wunused-but-set-variable',
    '-Wwrite-strings'
  ]

  foreach cflag: test_cflags
    if cc.has_argument(cflag)
      common_flags += [cflag]
    endif
  endforeach
endif

add_project_arguments(common_flags, language: 'c')

gio_req_version = '>= 2.38'
gtk_req_version = '>= 3.22'
webkit2gtk_req_version = '>= 2.6'

webkit2gtk_dep = dependency('webkit2gtk-4.0', version: webkit2gtk_req_version)

devhelp_deps = [
  webkit2gtk_dep,
  dependency('gio-2.0', version: gio_req_version),
  dependency('gsettings-desktop-schemas'),
  dependency('gtk+-3.0', version: gtk_req_version),
  cc.find_library('m', required: true)
]

enable_introspection = get_option('enable-introspection')

configure_file(
  output: 'config.h',
  configuration: config_h
)

gnome = import('gnome')
i18n = import('i18n')
pkg = import('pkgconfig')

po_dir = join_paths(meson.source_root(), 'po')

top_inc = include_directories('.')

subdir('po')
subdir('src')
subdir('data')

subdir('misc/gedit-plugin')

enable_gtk_doc = get_option('enable-gtk-doc')
if enable_gtk_doc
  subdir('docs/reference')
endif

meson.add_install_script(
  'meson_post_install.py',
  devhelp_datadir
)

# Print a summary of the configuration
output = 'Configuration:\n\n'
output += '        ' + meson.project_name() +  ' version ' + devhelp_version + '\n\n'
output += '        Source code location:  ' + meson.source_root() + '\n'
output += '        Prefix:                ' + devhelp_prefix + '\n'
output += '        Compiler:              ' + cc.get_id() + '\n'
output += '        API documentation:     ' + enable_gtk_doc.to_string() + '\n'
output += '        GObject introspection: ' + enable_introspection.to_string()
message(output)
