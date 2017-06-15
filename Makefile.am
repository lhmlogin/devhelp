SUBDIRS = po src data misc contrib docs

AM_DISTCHECK_CONFIGURE_FLAGS =	\
	--enable-gtk-doc	\
	--enable-introspection	\
	--enable-appstream-util

EXTRA_DIST = \
	devhelp.doap \
	meson.build \
	meson_options.txt \
	meson_post_install.py \
	po/meson.build

MAINTAINERCLEANFILES = \
	$(GITIGNORE_MAINTAINERCLEANFILES_TOPLEVEL) \
	$(GITIGNORE_MAINTAINERCLEANFILES_MAKEFILE_IN) \
	$(GITIGNORE_MAINTAINERCLEANFILES_M4_GETTEXT) \
	$(GITIGNORE_MAINTAINERCLEANFILES_M4_LIBTOOL) \
	gtk-doc.make \
	py-compile

-include $(top_srcdir)/git.mk
