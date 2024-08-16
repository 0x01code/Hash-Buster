DESTDIR ?= /usr/local/bin

install:
	@sudo cp hash.py $(DESTDIR)/buster
	@sudo cp database.py $(DESTDIR)/database.py
	@sudo chmod +x $(DESTDIR)/buster
	@echo "Installation Successful!"

uninstall:
	@sudo rm -f $(DESTDIR)/buster
	@sudo rm -f $(DESTDIR)/database.py
	@echo "Hash-Buster has been removed"
