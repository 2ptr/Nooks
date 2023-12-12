#!/bin/python

import os

startscreen = """
=====================================================
	 _ _            _                  _    
	| \ | ___  ___ | |__ ___      _ _ / |
	|   |/ . \/ . \| / /<_-<     | | || |
	|_\_|\___/\___/|_\_\/__/     |__/ |_|

                written by twopoint
                             
=====================================================
"""

# Generated with find /dir/ -maxdepth 3 2>/dev/null

normalfiles = """
/var/
/var/backups
/var/backups/apt.extended_states.4.gz
/var/backups/dpkg.status.0
/var/backups/dpkg.arch.1.gz
/var/backups/apt.extended_states.3.gz
/var/backups/apt.extended_states.6.gz
/var/backups/apt.extended_states.0
/var/backups/apt.extended_states.5.gz
/var/backups/dpkg.statoverride.1.gz
/var/backups/apt.extended_states.1.gz
/var/backups/alternatives.tar.0
/var/backups/dpkg.arch.0
/var/backups/dpkg.statoverride.0
/var/backups/dpkg.diversions.1.gz
/var/backups/dpkg.diversions.0
/var/backups/apt.extended_states.2.gz
/var/backups/alternatives.tar.1.gz
/var/backups/dpkg.status.1.gz
/var/cache
/var/cache/lightdm
/var/cache/system-tools-backends
/var/cache/apache2
/var/cache/apache2/mod_cache_disk
/var/cache/ldconfig
/var/cache/private
/var/cache/postgresql
/var/cache/postgresql/dicts
/var/cache/man
/var/cache/apparmor
/var/cache/apparmor/4256d98f.0
/var/cache/apparmor/8541e87b.0
/var/cache/apparmor/c08a2770.0
/var/cache/lighttpd
/var/cache/samba
/var/cache/fontconfig
/var/cache/fontconfig/3a954118-e368-4f79-b2f4-a3ca2290f0c1-le64.cache-7
/var/cache/fontconfig/eccfcd38-9d01-4c69-879a-2f40e093065d-le64.cache-7
/var/cache/fontconfig/269c13cf-f9d1-44ce-b5d3-a27cac39cb38-le64.cache-7
/var/cache/fontconfig/e00d7bd6-3c61-4b3b-8851-ee030c4c820c-le64.cache-7
/var/cache/fontconfig/91852b0c-4d46-49ce-bb2c-49923483d236-le64.cache-7
/var/cache/fontconfig/aaf63e17-cdfe-44f9-b48d-fbe165ec7cb3-le64.cache-7
/var/cache/fontconfig/d07b89bd-7ed8-44da-a6ae-e93504616dae-le64.cache-7
/var/cache/fontconfig/708f4748-a7e7-4a57-90b2-224c0346ef15-le64.cache-7
/var/cache/fontconfig/f52c6916-1692-4d02-a4eb-d7040cf3a4e3-le64.cache-7
/var/cache/fontconfig/f94eddfa-d667-4a38-aa70-0bebb4e12ad9-le64.cache-7
/var/cache/fontconfig/46d41f29-30a4-459b-98ab-69a1f0bcafbe-le64.cache-7
/var/cache/fontconfig/d6b96743-73a9-4cab-88e5-70b71e0f687a-le64.cache-7
/var/cache/fontconfig/71400758-0315-47b5-8fc5-b91ca1220940-le64.cache-7
/var/cache/fontconfig/a8d32ec6-669e-474a-8d93-837e7a7b3aeb-le64.cache-7
/var/cache/fontconfig/9b6fbf9a-d08d-49a9-968f-656b5fb5668f-le64.cache-7
/var/cache/fontconfig/29547c81-9ab6-418c-9797-ddd7275759ab-le64.cache-7
/var/cache/fontconfig/47682db5-e437-465b-883c-6de78b8d060a-le64.cache-7
/var/cache/fontconfig/6b03722d-4eec-469d-81af-445e0bf6cf08-le64.cache-7
/var/cache/fontconfig/353742a3-f8a7-4233-9c0c-3789a0f0b53f-le64.cache-7
/var/cache/fontconfig/cb4c6a60-ced0-465b-b432-36bca1f962b6-le64.cache-7
/var/cache/fontconfig/9198e801-6386-4abf-928d-210dcbece6ef-le64.cache-7
/var/cache/fontconfig/f14f635e-fba6-45c2-811b-dbe9319fe29c-le64.cache-7
/var/cache/fontconfig/e5a0a264-24d0-41a6-8581-e839ceb4338d-le64.cache-7
/var/cache/fontconfig/b4666964-22cb-42f4-960e-c1709782153e-le64.cache-7
/var/cache/fontconfig/0ec1eefd-6444-4c8e-b624-501d63e25896-le64.cache-7
/var/cache/fontconfig/b6b7785b-c822-4958-82d8-8061eb8a0048-le64.cache-7
/var/cache/fontconfig/e96c34b9-08f6-4188-87a9-f52a5e475783-le64.cache-7
/var/cache/fontconfig/f4a558fd-d2c6-4344-9c85-d10dac9fef82-le64.cache-7
/var/cache/fontconfig/8f45e246-ffac-4d36-b858-775d6fca238c-le64.cache-7
/var/cache/fontconfig/93fc58d7-0201-4442-abf3-7b24094cede3-le64.cache-7
/var/cache/fontconfig/3443ea99-a7fe-4c49-8d9e-3ce39a32f1f4-le64.cache-7
/var/cache/fontconfig/4a70553d-3817-483c-a65b-b02e6f73f223-le64.cache-7
/var/cache/fontconfig/c4f8e1b0-f8ab-4b7d-bcc3-022f0e6ff6f2-le64.cache-7
/var/cache/fontconfig/5cfd5ac0-1324-438f-a540-585fa1677128-le64.cache-7
/var/cache/fontconfig/4b78f342-6070-4625-b113-a6fd22282fc2-le64.cache-7
/var/cache/fontconfig/CACHEDIR.TAG
/var/cache/fontconfig/92e05cc2-9d27-4fd7-a1b1-09e9b969270d-le64.cache-7
/var/cache/fontconfig/3b6f9c4a-0957-4d14-a57c-bd273d8b818f-le64.cache-7
/var/cache/fontconfig/a3129d27-d33e-4283-8639-ce91e00ac5c5-le64.cache-7
/var/cache/fontconfig/06a39c1f-6d7a-4b62-9198-27f019d88e1a-le64.cache-7
/var/cache/fontconfig/1ecaac6a-eb31-4a9a-b9ac-b8cde3c669b0-le64.cache-7
/var/cache/fontconfig/76c5d183-667c-4da0-8498-c0df014dd4c7-le64.cache-7
/var/cache/fontconfig/501092ec-95c0-4e05-8d7d-3b30a1c1ae96-le64.cache-7
/var/cache/fontconfig/99ac7365-3366-4740-9371-f039c570b43c-le64.cache-7
/var/cache/locate
/var/cache/locate/locatedb
/var/cache/dictionaries-common
/var/cache/dictionaries-common/hunspell.db
/var/cache/dictionaries-common/ispell-dicts-list.txt
/var/cache/dictionaries-common/emacsen-ispell-default.el
/var/cache/dictionaries-common/sqspell.php
/var/cache/dictionaries-common/aspell.db
/var/cache/dictionaries-common/ispell.db
/var/cache/dictionaries-common/emacsen-ispell-dicts.el
/var/cache/dictionaries-common/jed-ispell-dicts.sl
/var/cache/dictionaries-common/wordlist.db
/var/cache/dictionaries-common/wordlist-default
/var/cache/cracklib
/var/cache/cracklib/cracklib_dict.pwi
/var/cache/cracklib/cracklib_dict.pwd
/var/cache/cracklib/src-dicts
/var/cache/cracklib/cracklib_dict.hwm
/var/cache/debconf
/var/cache/debconf/config.dat
/var/cache/debconf/templates.dat-old
/var/cache/debconf/passwords.dat
/var/cache/debconf/templates.dat
/var/cache/debconf/config.dat-old
/var/cache/apt
/var/cache/apt/srcpkgcache.bin
/var/cache/apt/pkgcache.bin
/var/cache/apt/archives
/var/lock
/var/lol.txt
/var/log
/var/log/syslog.1
/var/log/macchanger.log.1.gz
/var/log/openvpn
/var/log/openvpn/htb.log
/var/log/auth.log.1
/var/log/stunnel4
/var/log/lightdm
/var/log/opensnitchd.log
/var/log/redis
/var/log/apache2
/var/log/kern.log
/var/log/nginx
/var/log/journal
/var/log/journal/8ffe0e0c1f022ae6513bf3be64636102
/var/log/journal/d6548e065640c98a3e972fde6405b7a7
/var/log/journal/ddbbca336d764dd1c4e640ca645b6ebc
/var/log/journal/6c15e29cca4fc4052d0e6a33645ba198
/var/log/btmp
/var/log/wtmp
/var/log/README
/var/log/boot.log.1
/var/log/chkrootkit
/var/log/boot.log
/var/log/cron.log
/var/log/gvm
/var/log/private
/var/log/postgresql
/var/log/runit
/var/log/runit/dnsmasq
/var/log/runit/ssh
/var/log/user.log
/var/log/ntpstats
/var/log/Xorg.0.log
/var/log/apparmor
/var/log/btmp.1
/var/log/lighttpd
/var/log/samba
/var/log/kern.log.1
/var/log/cloud-init.log
/var/log/sysstat
/var/log/sysstat/sa12
/var/log/inetsim
/var/log/i2p
/var/log/apt
/var/log/user.log.1
/var/log/lastlog
/var/log/syslog
/var/log/cloud-init-output.log
/var/log/exim4
/var/log/droplet-agent.update.log
/var/log/cron.log.1
/var/log/neo4j
/var/log/auth.log
/var/www
/var/www/html
/var/www/html/index.html
/var/www/html/index.nginx-debian.html
/var/lib
/var/lib/resolvconf
/var/lib/resolvconf/linkified
/var/lib/gconf
/var/lib/gconf/debian.defaults
/var/lib/gconf/debian.mandatory
/var/lib/gconf/defaults
/var/lib/openvpn
/var/lib/openvpn/chroot
/var/lib/stunnel4
/var/lib/grub
/var/lib/grub/ucf
/var/lib/lightdm
/var/lib/sudo
/var/lib/sudo/lectured
/var/lib/openvas
/var/lib/openvas/gvm-checking
/var/lib/openvas/gvm-helping
/var/lib/openvas/gvm-serving
/var/lib/openvas/gvm-migrating
/var/lib/redis
/var/lib/apache2
/var/lib/apache2/conf
/var/lib/apache2/site
/var/lib/apache2/module
/var/lib/systemd
/var/lib/systemd/deb-systemd-helper-masked
/var/lib/systemd/deb-systemd-user-helper-enabled
/var/lib/systemd/timers
/var/lib/systemd/random-seed
/var/lib/systemd/coredump
/var/lib/systemd/pstore
/var/lib/systemd/linger
/var/lib/systemd/deb-systemd-helper-enabled
/var/lib/systemd/catalog
/var/lib/systemd/rfkill
/var/lib/nginx
/var/lib/php
/var/lib/php/sessions
/var/lib/php/modules
/var/lib/snmp
/var/lib/snmp/cert_indexes
/var/lib/reaver
/var/lib/update-rc.d
/var/lib/os-prober
/var/lib/dpkg
/var/lib/dpkg/available
/var/lib/dpkg/statoverride-old
/var/lib/dpkg/parts
/var/lib/dpkg/lock
/var/lib/dpkg/updates
/var/lib/dpkg/diversions-old
/var/lib/dpkg/status
/var/lib/dpkg/cmethopt
/var/lib/dpkg/alternatives
/var/lib/dpkg/diversions
/var/lib/dpkg/status-old
/var/lib/dpkg/statoverride
/var/lib/dpkg/lock-frontend
/var/lib/dpkg/triggers
/var/lib/dpkg/info
/var/lib/ucf
/var/lib/ucf/cache
/var/lib/ucf/hashfile.2
/var/lib/ucf/registry.3
/var/lib/ucf/hashfile.7
/var/lib/ucf/registry.7
/var/lib/ucf/hashfile.3
/var/lib/ucf/registry
/var/lib/ucf/hashfile
/var/lib/ucf/hashfile.6
/var/lib/ucf/hashfile.4
/var/lib/ucf/registry.5
/var/lib/ucf/hashfile.1
/var/lib/ucf/registry.6
/var/lib/ucf/registry.0
/var/lib/ucf/registry.2
/var/lib/ucf/hashfile.0
/var/lib/ucf/registry.1
/var/lib/ucf/registry.4
/var/lib/ucf/hashfile.5
/var/lib/king-phisher
/var/lib/king-phisher/www
/var/lib/bluetooth
/var/lib/strongswan
/var/lib/private
/var/lib/dbus
/var/lib/dbus/machine-id
/var/lib/synaptic
/var/lib/libxml-sax-perl
/var/lib/libxml-sax-perl/ParserDetails.d
/var/lib/ntp
/var/lib/postgresql
/var/lib/postgresql/13
/var/lib/pam
/var/lib/pam/seen
/var/lib/pam/auth
/var/lib/pam/session
/var/lib/pam/account
/var/lib/pam/session-noninteractive
/var/lib/pam/password
/var/lib/nikto
/var/lib/nikto/templates
/var/lib/nikto/databases
/var/lib/nikto/plugins
/var/lib/nikto/docs
/var/lib/nikto/nikto.pl
/var/lib/nikto/replay.pl
/var/lib/nikto/nikto.conf.default
/var/lib/upower
/var/lib/NetworkManager-fortisslvpn
/var/lib/xml-core
/var/lib/xml-core/docbook-xsl
/var/lib/xml-core/xml-core
/var/lib/xml-core/docbook-xml
/var/lib/xml-core/docutils-common
/var/lib/xml-core/sgml-data
/var/lib/xml-core/catalog
/var/lib/gems
/var/lib/gems/2.7.0
/var/lib/vim
/var/lib/vim/addons
/var/lib/nfs
/var/lib/nfs/sm.bak
/var/lib/nfs/sm
/var/lib/nfs/state
/var/lib/shellinabox
/var/lib/selinux
/var/lib/selinux/final
/var/lib/selinux/default
/var/lib/git
/var/lib/rkhunter
/var/lib/rkhunter/tmp
/var/lib/rkhunter/db
/var/lib/ispell
/var/lib/ispell/README
/var/lib/python
/var/lib/python/python3.9_installed
/var/lib/colord
/var/lib/colord/icc
/var/lib/smartmontools
/var/lib/smartmontools/drivedb
/var/lib/NetworkManager
/var/lib/AccountsService
/var/lib/AccountsService/users
/var/lib/AccountsService/icons
/var/lib/samba
/var/lib/samba/dhcp.conf
/var/lib/samba/private
/var/lib/samba/printers
/var/lib/samba/usershares
/var/lib/ghostscript
/var/lib/ghostscript/CMap
/var/lib/ghostscript/fonts
/var/lib/polkit-1
/var/lib/binfmts
/var/lib/binfmts/llvm-9-runtime.binfmt
/var/lib/binfmts/jarwrapper
/var/lib/binfmts/python3.9
/var/lib/binfmts/python2.7
/var/lib/binfmts/jar
/var/lib/dictionaries-common
/var/lib/dictionaries-common/wordlist
/var/lib/dictionaries-common/aspell
/var/lib/dictionaries-common/hunspell
/var/lib/autopsy
/var/lib/arpwatch
/var/lib/plymouth
/var/lib/plymouth/boot-duration
/var/lib/sntp
/var/lib/sntp/kod
/var/lib/udisks2
/var/lib/inetsim
/var/lib/inetsim/quotd
/var/lib/inetsim/pop3
/var/lib/inetsim/http
/var/lib/inetsim/tftp
/var/lib/inetsim/certs
/var/lib/inetsim/smtp
/var/lib/inetsim/finger
/var/lib/inetsim/ftp
/var/lib/i2p
/var/lib/apt
/var/lib/apt/extended_states
/var/lib/apt/mirrors
/var/lib/apt/lists
/var/lib/apt/daily_lock
/var/lib/apt/periodic
/var/lib/apt/listchanges.db
/var/lib/apt/listchanges-old.db
/var/lib/misc
/var/lib/sgml-base
/var/lib/sgml-base/supercatalog
/var/lib/sgml-base/supercatalog.old
/var/lib/usbutils
/var/lib/usbutils/usb.ids
/var/lib/cloud
/var/lib/cloud/sem
/var/lib/cloud/handlers
/var/lib/cloud/seed
/var/lib/cloud/data
/var/lib/cloud/instances
/var/lib/cloud/scripts
/var/lib/cloud/instance
/var/lib/tpm
/var/lib/xfonts
/var/lib/xfonts/excluded-aliases
/var/lib/blueman
/var/lib/geoclue
/var/lib/dhcp
/var/lib/dhcp/dhclient.eth1.leases
/var/lib/dhcp/dhclient.eth0.leases
/var/lib/xkb
/var/lib/xkb/README.compiled
/var/lib/exim4
/var/lib/exim4/berkeleydbvers.txt
/var/lib/exim4/config.autogenerated
/var/lib/man-db
/var/lib/man-db/auto-update
/var/lib/doc-base
/var/lib/doc-base/documents
/var/lib/doc-base/info
/var/lib/menu-xdg
/var/lib/menu-xdg/menus
/var/lib/menu-xdg/desktop-directories
/var/lib/menu-xdg/applications
/var/lib/aspell
/var/lib/aspell/en_AU-variant_1.rws
/var/lib/aspell/en_CA-wo_accents-only.rws
/var/lib/aspell/en_CA-variant_0.rws
/var/lib/aspell/en-variant_0.rws
/var/lib/aspell/en-w_accents-only.rws
/var/lib/aspell/en_GB-ise-w_accents-only.rws
/var/lib/aspell/en_GB-variant_0.rws
/var/lib/aspell/README
/var/lib/aspell/en-variant_2.rws
/var/lib/aspell/en_GB-ise-wo_accents-only.rws
/var/lib/aspell/en.compat
/var/lib/aspell/en_US-wo_accents-only.rws
/var/lib/aspell/en-variant_1.rws
/var/lib/aspell/en_AU-wo_accents-only.rws
/var/lib/aspell/en_CA-variant_1.rws
/var/lib/aspell/en-wo_accents-only.rws
/var/lib/aspell/en_US-w_accents-only.rws
/var/lib/aspell/en_GB-ize-w_accents-only.rws
/var/lib/aspell/en-common.rws
/var/lib/aspell/en_AU-w_accents-only.rws
/var/lib/aspell/en_AU-variant_0.rws
/var/lib/aspell/en.remove
/var/lib/aspell/en_CA-w_accents-only.rws
/var/lib/aspell/en_GB-variant_1.rws
/var/lib/aspell/en_GB-ize-wo_accents-only.rws
/var/lib/alsa
/var/lib/alsa/asound.state
/var/lib/logrotate
/var/lib/logrotate/status
/var/lib/GeoIP
/var/lib/neo4j
/var/lib/neo4j/certificates
/var/lib/neo4j/import
/var/lib/neo4j/labs
/var/lib/neo4j/plugins
/var/lib/neo4j/licenses
/var/lib/neo4j/data
/var/lib/neo4j/run
/var/lib/darkstat
/var/lib/emacsen-common
/var/lib/emacsen-common/state
/var/lib/ieee-data
/var/lib/ieee-data/mam.txt
/var/lib/ieee-data/oui36.csv
/var/lib/ieee-data/.lastupdate
/var/lib/ieee-data/oui36.txt
/var/lib/ieee-data/update.d
/var/lib/ieee-data/iab.txt
/var/lib/ieee-data/oui.txt
/var/lib/ieee-data/iab.csv
/var/lib/ieee-data/oui.csv
/var/lib/ieee-data/mam.csv
/var/lib/vmware
/var/lib/vmware/VGAuth
/var/tmp
/var/tmp/systemd-private-5628d4bba9d74f2cb472f4f276ac89d7-systemd-logind.service-KXwLBh
/var/tmp/cloud-init
/var/tmp/systemd-private-5628d4bba9d74f2cb472f4f276ac89d7-haveged.service-H98ogh
/var/tmp/systemd-private-5628d4bba9d74f2cb472f4f276ac89d7-upower.service-MRk5Ef
/var/tmp/systemd-private-5628d4bba9d74f2cb472f4f276ac89d7-openvpn@htb-twopoint.service-OqzYdf
/var/tmp/systemd-private-5628d4bba9d74f2cb472f4f276ac89d7-do-agent.service-mBBBfg
/var/NX
/var/NX/nx
/var/run
/var/local
/var/mail
/var/mail/mail
/var/spool
/var/spool/rsyslog
/var/spool/cron
/var/spool/cron/crontabs
/var/spool/mail
/var/spool/exim4
/var/opt
/var/unicornscan
/home/
/home/htb-twopoint
/home/htb-twopoint/.cloud-locale-test.skip
/home/htb-twopoint/.gtkrc-2.0
/home/htb-twopoint/.zshrc
/home/htb-twopoint/.kde
/home/htb-twopoint/.kde/share
/home/htb-twopoint/.emacs
/home/htb-twopoint/.msf4
/home/htb-twopoint/.msf4/config
/home/htb-twopoint/.bashrc
/home/htb-twopoint/.profile
/home/htb-twopoint/.BurpSuite
/home/htb-twopoint/.BurpSuite/UserConfigCommunity.json
/home/htb-twopoint/.cache
/home/htb-twopoint/.cache/event-sound-cache.tdb.43e7a36bdbec60c5337902dd657898a0.x86_64-pc-linux-gnu
/home/htb-twopoint/.cache/mesa_shader_cache
/home/htb-twopoint/.cache/mate
/home/htb-twopoint/.cache/at-spi
/home/htb-twopoint/.cache/fontconfig
/home/htb-twopoint/.cache/mozilla
/home/htb-twopoint/.cache/doc
/home/htb-twopoint/.cache/gvfs
/home/htb-twopoint/.cache/keyring-S27QF2
/home/htb-twopoint/.cache/dconf
/home/htb-twopoint/Templates
/home/htb-twopoint/Templates/web
/home/htb-twopoint/Templates/text
/home/htb-twopoint/Templates/prog
/home/htb-twopoint/.ICEauthority
/home/htb-twopoint/.mozilla
/home/htb-twopoint/.mozilla/extensions
/home/htb-twopoint/.mozilla/firefox
/home/htb-twopoint/1
/home/htb-twopoint/.xsession-errors
/home/htb-twopoint/.vimrc
/home/htb-twopoint/Desktop
/home/htb-twopoint/Desktop/normalfiles.txt
/home/htb-twopoint/Desktop/normaldirs.txt
/home/htb-twopoint/Desktop/my_credentials.txt
/home/htb-twopoint/Desktop/README.license
/home/htb-twopoint/Desktop/nooks.py
/home/htb-twopoint/Desktop/htb_vpn_logs.log
/home/htb-twopoint/Desktop/my_data
/home/htb-twopoint/Desktop/normal.txt
/home/htb-twopoint/.config
/home/htb-twopoint/.config/ksplashrc
/home/htb-twopoint/.config/touchpadrc
/home/htb-twopoint/.config/kactivitymanagerd-statsrc
/home/htb-twopoint/.config/nano
/home/htb-twopoint/.config/KDE
/home/htb-twopoint/.config/clipit
/home/htb-twopoint/.config/katevirc
/home/htb-twopoint/.config/kwinrc
/home/htb-twopoint/.config/bleachbit
/home/htb-twopoint/.config/nvim
/home/htb-twopoint/.config/user-dirs.locale
/home/htb-twopoint/.config/katepartrc
/home/htb-twopoint/.config/ksmserverrc
/home/htb-twopoint/.config/openbox
/home/htb-twopoint/.config/kgammarc
/home/htb-twopoint/.config/lxterminal
/home/htb-twopoint/.config/lxpanel
/home/htb-twopoint/.config/VSCodium
/home/htb-twopoint/.config/gtk-3.0
/home/htb-twopoint/.config/kscreenlockerrc
/home/htb-twopoint/.config/polybar
/home/htb-twopoint/.config/khotkeysrc
/home/htb-twopoint/.config/fish
/home/htb-twopoint/.config/geany
/home/htb-twopoint/.config/kateschemarc
/home/htb-twopoint/.config/menus
/home/htb-twopoint/.config/xfce4
/home/htb-twopoint/.config/kded5rc
/home/htb-twopoint/.config/kdeglobals
/home/htb-twopoint/.config/mate
/home/htb-twopoint/.config/i3
/home/htb-twopoint/.config/spectaclerc
/home/htb-twopoint/.config/plasma-org.kde.plasma.desktop-appletsrc
/home/htb-twopoint/.config/katesyntaxhighlightingrc
/home/htb-twopoint/.config/user-dirs.dirs
/home/htb-twopoint/.config/pulse
/home/htb-twopoint/.config/keepassxc
/home/htb-twopoint/.config/caja
/home/htb-twopoint/.config/pcmanfm
/home/htb-twopoint/.config/akregatorrc
/home/htb-twopoint/.config/plasmarc
/home/htb-twopoint/.config/autostart
/home/htb-twopoint/.config/mimeapps.list
/home/htb-twopoint/.config/bloodhound
/home/htb-twopoint/.config/konsolerc
/home/htb-twopoint/.config/breezerc
/home/htb-twopoint/.config/caja-actions
/home/htb-twopoint/.config/kwalletrc
/home/htb-twopoint/.config/startupconfig
/home/htb-twopoint/.config/powershell
/home/htb-twopoint/.config/gtk-2.0
/home/htb-twopoint/.config/mate-menu
/home/htb-twopoint/.config/kcminputrc
/home/htb-twopoint/.config/kcmdisplayrc
/home/htb-twopoint/.config/kconf_updaterc
/home/htb-twopoint/.config/klaunchrc
/home/htb-twopoint/.config/Trolltech.conf
/home/htb-twopoint/.config/plasmashellrc
/home/htb-twopoint/.config/enchant
/home/htb-twopoint/.config/kglobalshortcutsrc
/home/htb-twopoint/.config/dconf
/home/htb-twopoint/.dbeaver4
/home/htb-twopoint/.dbeaver4/.metadata
/home/htb-twopoint/.pwnbox_version
/home/htb-twopoint/my_data
/home/htb-twopoint/.Xauthority
/home/htb-twopoint/.local
/home/htb-twopoint/.local/share
/home/htb-twopoint/.dbus
/home/htb-twopoint/.dbus/session-bus
/home/htb-twopoint/.vnc
/home/htb-twopoint/.vnc/passwd
/home/htb-twopoint/.vnc/htb-fkv2ywlxfi.htb-cloud.com:5901.pid
/home/htb-twopoint/.vnc/htb-fkv2ywlxfi.htb-cloud.com:5901.log
/mnt/
/tmp/
/tmp/.X1-lock
/tmp/systemd-private-5628d4bba9d74f2cb472f4f276ac89d7-haveged.service-1xyrij
/tmp/systemd-private-5628d4bba9d74f2cb472f4f276ac89d7-upower.service-vT3heg
/tmp/.X0-lock
/tmp/dbus-xAbyZHVIbk
/tmp/systemd-private-5628d4bba9d74f2cb472f4f276ac89d7-openvpn@htb-twopoint.service-Gcu81i
/tmp/Temp-11a7508e-f94f-45d1-9102-013a05849416
/tmp/.font-unix
/tmp/.XIM-unix
/tmp/my_data.tar.gz
/tmp/pulse-PKdhtXMmr18n
/tmp/pluma.htb-twopoint.2015855360
/tmp/tmpaddon
/tmp/.X11-unix
/tmp/.X11-unix/X0
/tmp/.X11-unix/X1
/tmp/dbus-ZItD88MeCj
/tmp/ssh-RgXXMXJXN4iW
/tmp/ssh-RgXXMXJXN4iW/agent.13177
/tmp/systemd-private-5628d4bba9d74f2cb472f4f276ac89d7-do-agent.service-lWG7wi
/tmp/systemd-private-5628d4bba9d74f2cb472f4f276ac89d7-systemd-logind.service-IRWRxg
/tmp/.ICE-unix
/tmp/.ICE-unix/13177
/media/
/media/nomachine
"""

def detectServices ():

    services = {
    3306: "MySQL",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP",
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    110: "POP3",
    143: "IMAP"
    }
    liveServices = []

    stdout = str(os.popen('netstat -aln | grep -e 0.0.0.0 -e 127.0 | cut -d : -f2 | cut -d " " -f 1').read())
    stdout = stdout.split("\n")
    
    for line in stdout:
        for port in services.keys():
            if str(port) == line and services[port] not in liveServices:
                liveServices.append(services[port])
    
    for port in liveServices:
        print("\t\t [+] " + port + " possibly detected!")
            

def sysline(cmd, tabs):
    stdout = str(os.popen("("+cmd+")" + " 2>/dev/null").read())
    stdout = stdout.split("\n")
    for line in stdout:
        print("\t"*tabs + line)

def sysInfo():
    print("[*] System Info [*]\n")
    
    print("\t==> CPU Information")
    sysline("lscpu | head -n 4",1)
    
    print("\t==> Kernel and OS")
    sysline("uname -o && uname -v", 1)
    
    print("\t==> Listening Ports")
    sysline("netstat -aln | grep -e 0.0.0.0 -e 127.0 -e Address | cut -f 2", 1)
    detectServices()
    
def searchUnique():
    print("\n[*] Finding interesting files and directories... [*]")
    dirnames = ["var","home","mnt","tmp","media"]
    sysFiles = []
    
    for name in dirnames:
        find = str(os.popen('find /'+name+'/ -maxdepth 2 2>/dev/null').read())
        find = find.split("\n")
        sysFiles = sysFiles + find
        
    for line in sysFiles:
        if line not in normalfiles:
            print("\t"+line)
   

print(startscreen)
sysInfo()
searchUnique()