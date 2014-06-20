SUBDIRS = streamteam

bin_SCRIPTS = arduino-stream-team
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = arduino-stream-team.in

do_substitution = sed -e "s,[@]pythondir[@],$(pythondir),g"\ 
	-e "s,[@]PACKAGE[@],$(PACKAGE),g" \ 
	-e "s,[@]VERSION[@],$(VERSION),g" 

arduino-stream-team: arduino-stream-team.in Makefile
	$(do_substitution) < $(srcdir)/arduino-stream-team.in > arduino-stream-team
	chmod +x arduino-stream-team