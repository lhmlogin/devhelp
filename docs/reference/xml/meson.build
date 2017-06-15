ent_conf = configuration_data()

ent_conf.set('PACKAGE', package)
ent_conf.set('PACKAGE_BUGREPORT', package_bugreport)
ent_conf.set('PACKAGE_NAME', package_name)
ent_conf.set('PACKAGE_STRING', package_string)
ent_conf.set('PACKAGE_TARNAME', package_tarname)
ent_conf.set('PACKAGE_URL', package_url)
ent_conf.set('PACKAGE_VERSION', package_version)

ent = 'gtkdocentities.ent'

configure_file(
  input: ent + '.in',
  output: ent,
  configuration: ent_conf
)
