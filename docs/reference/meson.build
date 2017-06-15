subdir('xml')

private_headers = [
  'dh-app.h',
  'dh-assistant.h',
  'dh-enum-types-app.h',
  'dh-error.h',
  'dh-language.h',
  'dh-parser.h',
  'dh-preferences.h',
  'dh-settings.h',
  'dh-util.h',
  'dh-window.h'
]

webkit_prefix = webkit2gtk_dep.get_pkgconfig_variable('prefix')
webkit_doc_path = join_paths(webkit_prefix, 'share', 'gtk-doc', 'html')

doc_path = join_paths(devhelp_datadir, 'gtk-doc', 'html', libdevhelp_name)

gnome.gtkdoc(
  devhelp_name,
  main_xml: devhelp_name + '-docs.xml',
  src_dir: src_inc,
  dependencies: libdevhelp_dep,
  scan_args: [
    '--rebuild-types',
    '--ignore-headers=' + ' '.join(private_headers)
  ],
  mkdb_args: [
    '--xml-mode',
    '--output-format=xml'
  ],
  gobject_typesfile: devhelp_name + '.types',
  fixxref_args: '--extra-dir=' + join_paths(webkit_doc_path, 'webkit2gtk-4.0'),
  install: true,
  install_dir: doc_path
)
