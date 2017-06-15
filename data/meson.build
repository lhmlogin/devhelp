subdir('dtd')
subdir('icons')

info_name = 'org.gnome.Devhelp.metainfo.xml'

i18n.merge_file(
  info_name,
  input: 'org.gnome.Devhelp.appdata.xml.in',
  output: info_name,
  po_dir: po_dir,
  install: true,
  install_dir: join_paths(devhelp_datadir, 'metainfo')
)

desktop = 'org.gnome.Devhelp.desktop'

desktop_conf = configuration_data()
desktop_conf.set('VERSION', devhelp_version)

desktop_in = configure_file(
  input: desktop + '.in.in',
  output: desktop + '.in',
  configuration: desktop_conf
)

i18n.merge_file(
  desktop,
  type: 'desktop',
  input: desktop_in,
  output: desktop,
  po_dir: po_dir,
  install: true,
  install_dir: join_paths(devhelp_datadir, 'applications')
)

service_conf = configuration_data()
service_conf.set('bindir', devhelp_bindir)

service = 'org.gnome.Devhelp.service'

configure_file(
  input: service + '.in',
  output: service,
  install: true,
  install_dir: join_paths(devhelp_datadir, 'dbus-1', 'services'),
  configuration: service_conf
)

assistant_data = files(
  'assistant.js',
  'assistant.css'
)

install_data(
  assistant_data,
  install_dir: join_paths(devhelp_pkgdatadir, 'assistant')
)

install_data(
  'org.gnome.devhelp.gschema.xml',
  install_dir: join_paths(devhelp_datadir, 'glib-2.0', 'schemas')
)

install_data(
  'devhelp.convert',
  install_dir: join_paths(devhelp_datadir, 'GConf', 'gsettings')
)

install_data(
  'devhelp.1',
  install_dir: join_paths(devhelp_mandir, 'man1')
)
