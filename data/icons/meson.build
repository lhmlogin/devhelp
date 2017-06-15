icons = [
  ['16x16', 'devhelp.png'],
  ['22x22', 'devhelp.png'],
  ['24x24', 'devhelp.png'],
  ['32x32', 'devhelp.png'],
  ['48x48', 'devhelp.png'],
  ['256x256', 'devhelp.png'],
  ['symbolic', 'devhelp-symbolic.svg']
]

foreach icon: icons
  install_data(
    join_paths(icon[0], icon[1]),
    install_dir: join_paths(devhelp_datadir, 'icons', 'hicolor', icon[0], 'apps')
  )
endforeach
