SRCS    := $(shell ls ../*.py ../rfgengou* ../README*)
SERIES  := lucid precise
NAME    := $(shell cat $(PARENT)../setup.py | grep name    | awk -F \" '{print $$2}')
VERSION := $(shell cat $(PARENT)../setup.py | grep version | awk -F \" '{print $$2}')
DIR     := $(NAME)-$(VERSION)
ZIP     := $(NAME)-$(VERSION).zip
TBZ     := python-rfgengou_$(VERSION).orig.tar.bz2

all: $(SERIES)

clean:
	rm -rf $(SERIES)

$(SERIES): $(TBZ)
	rm -rf $@
	mkdir  $@
	ln -s ../$(TBZ) $@/$(TBZ)
	cd $@ && tar jxf $(TBZ)
	cp -pr debian $@/$(DIR)
	cat debian/changelog | sed -e "s/@@SERIES@@/$@/g" > $@/$(DIR)/debian/changelog
	cd $@/$(DIR) && debuild -uc -us
	cd $@/$(DIR) && debuild -S  -sa
	@echo eput ppa:h-rayflood/python2 $@/*_source.changes

$(TBZ):
	@echo make orig $(TBZ)
	rm -f $(ZIP) $(TBZ)
	mkdir -p $(DIR)
	cp -p  $(SRCS) $(DIR)
	zip -r  $(ZIP) $(DIR)
	tar jcf $(TBZ) $(DIR)
	rm -r   $(DIR)

.PHONY: all $(SERIES)
