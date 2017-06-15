src_inc = include_directories('.')

libdevhelp_headers = files(
  'devhelp.h',
  'dh-assistant-view.h',
  'dh-book.h',
  'dh-book-manager.h',
  'dh-book-tree.h',
  'dh-init.h',
  'dh-keyword-model.h',
  'dh-link.h',
  'dh-sidebar.h'
)

install_headers(
  libdevhelp_headers,
  subdir: join_paths(devhelp_api_name, devhelp_name)
)

libdevhelp_sources = files(
  'dh-assistant-view.c',
  'dh-book.c',
  'dh-book-manager.c',
  'dh-book-tree.c',
  'dh-init.c',
  'dh-keyword-model.c',
  'dh-link.c',
  'dh-sidebar.c'
)

enum = 'dh-enum-types'

libdevhelp_sources += gnome.mkenums(
  enum,
  sources: libdevhelp_headers,
  c_template: enum + '.c.template',
  h_template: enum + '.h.template',
  install_header: true,
  install_dir: join_paths(devhelp_pkgincludedir, devhelp_name)
)

headers = files(
  'dh-error.h',
  'dh-language.h',
  'dh-parser.h',
  'dh-preferences.h',
  'dh-settings.h',
  'dh-util.h'
)

sources = files(
  'dh-error.c',
  'dh-language.c',
  'dh-parser.c',
  'dh-preferences.c',
  'dh-util.c',
  'dh-settings.c'
)

resource_files = files(
  'devhelp-menu.ui',
  'dh-assistant.ui',
  'dh-preferences.ui',
  'dh-window.ui',
  'help-overlay.ui'
)

sources += gnome.compile_resources(
  'dh-resources',
  'dh.gresource.xml',
  source_dir: '.',
  c_name: 'dh',
  dependencies: resource_files,
  export: true
)

cflags = [
  '-DLOCALEDIR="@0@"'.format(devhelp_localedir),
  '-DDATADIR="@0@"'.format(devhelp_datadir),
  '-DG_LOG_DOMAIN="@0@"'.format(meson.project_name()),
  '-DGDK_PIXBUF_DISABLE_SINGLE_INCLUDES'
]

symbol_map = 'devhelp.map'

test_ldflag = '-Wl,--version-script,@0@/@1@'.format(meson.current_source_dir(), symbol_map)

ldflags = []

if host_machine.system().contains('linux') and cc.has_argument(test_ldflag)
  ldflags += test_ldflag
endif

libdevhelp = shared_library(
  libdevhelp_name,
  sources: libdevhelp_sources + sources,
  version: libdevhelp_version,
  include_directories: top_inc,
  dependencies: devhelp_deps,
  c_args: cflags,
  link_args: ldflags,
  link_depends: symbol_map,
  install: true,
  install_dir: devhelp_libdir
)

libdevhelp_dep = declare_dependency(
  link_with: libdevhelp,
  include_directories: src_inc,
  dependencies: devhelp_deps
)

pkg.generate(
  libraries: libdevhelp,
  version: devhelp_version,
  name: devhelp_name,
  description: devhelp_name,
  filebase: 'lib' + devhelp_api_name,
  subdirs: devhelp_pkgincludedir,
  requires: [
    'gio-2.0 ' + gio_req_version,
    'gtk+-3.0 ' + gtk_req_version,
    'webkit2gtk-4.0 ' + webkit2gtk_req_version
  ],
  requires_private: 'gsettings-desktop-schemas',
  variables: 'exec_prefix=' + devhelp_prefix,
  install_dir: join_paths(devhelp_libdir, 'pkgconfig')
)

headers = files(
  'dh-app.h',
  'dh-assistant.h',
  'dh-window.h'
)

sources = files(
  'dh-app.c',
  'dh-assistant.c',
  'dh-main.c',
  'dh-window.c'
)

enum = 'dh-enum-types-app'

sources += gnome.mkenums(
  enum,
  sources: headers,
  c_template: enum + '.c.template',
  h_template: enum + '.h.template'
)

executable(
  devhelp_name,
  sources,
  include_directories: top_inc,
  dependencies: libdevhelp_dep,
  install: true,
  install_dir: devhelp_bindir
)

if enable_introspection
  gir_incs = [
    'Gtk-3.0',
    'WebKit2-4.0'
  ]

  gir_extra_args = [
    '--c-include="devhelp/devhelp.h"',
    '--warn-all'
  ]

  gir_dir = join_paths(devhelp_datadir, 'gir-' + devhelp_gir_version)
  typelib_dir = join_paths(devhelp_libdir, 'girepository-' + devhelp_gir_version)

  gnome.generate_gir(
    libdevhelp,
    sources: libdevhelp_sources + libdevhelp_headers,
    namespace: meson.project_name(),
    nsversion: devhelp_api_version,
    symbol_prefix: 'dh',
    identifier_prefix: 'Dh',
    export_packages: 'lib' + devhelp_api_name,
    extra_args: gir_extra_args,
    includes: gir_incs,
    include_directories: top_inc,
    install: true,
    install_dir_gir: gir_dir,
    install_dir_typelib: typelib_dir
  )
endif
