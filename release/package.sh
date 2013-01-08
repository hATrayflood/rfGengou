#!/bin/sh

CUR=`dirname ${0}`
CUR=`cd ${CUR} && pwd`
cd ${CUR}

NAME=`cat ../setup.py | grep name | awk -F \" '{print $2}'`
VERSION=`cat ../setup.py | grep version | awk -F \" '{print $2}'`
PPANAME=`cat debian/control | grep ^Source: | awk '{print $2}'`
SERIES="lucid precise"
DIR=${NAME}-${VERSION}
ZIP=${NAME}-${VERSION}.zip

archive(){
	cd ${CUR}
	if [ -f "${ZIP}" ] ; then
		return 0
	fi

	SRCS=`ls ../*.py ../README*`
	mkdir -p ${DIR}
	cp -p ${SRCS} ${DIR}
	zip -r ${ZIP} ${DIR}
}

ppa(){
	cd ${CUR}
	archive
	mkdir -p ppa
	cd ppa

	if [ ! -f "${PPANAME}_${VERSION}.orig.tar.gz" ] ; then
		unzip ../${ZIP}
		cd ${DIR}
		cp -pr ../../debian .
		dh_make --createorig -i -p ${PPANAME}
	else
		cd ${DIR}
		rm -rf debian
		cp -pr ../../debian .
	fi

	for S in ${SERIES} ; do
		cat ../../debian/changelog | sed -e "s/@@SERIES@@/${S}/g" > debian/changelog
		debuild -uc -us
		debuild -S -sa
	done
}

ppa_dput(){
	for S in ${SERIES} ; do
		cd ${CUR}
		dput ppa:h-rayflood/python2 ppa/${PPANAME}_${VERSION}-1nmu1ppa1~${S}_source.changes
	done
}

if [ "$1" = "dput" ] ; then
	ppa_dput
elif [ "$1" = "ppa" ] ; then
	ppa
else
	archive
fi
