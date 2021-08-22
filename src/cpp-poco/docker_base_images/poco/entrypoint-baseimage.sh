#!/bin/bash
# update system and install git
apt-get -y update
apt-get -y install -y git
# cd to external src dir
cd /src
# git clone poco project
if [ ! -d ./poco ]; then
	git clone https://github.com/pocoproject/poco
fi
cd poco
git checkout $POCO_GIT_BRANCH
git pull

# copy external configs (output of configure)
cp /config.make ./
cp /config.build ./

apt-get install -qq -y libpcre3-dev libssl-dev libexpat1-dev \
                       libpq-dev unixodbc-dev libmysqlclient-dev \
                       libsqlite3-dev wget make sloccount cppcheck

add-apt-repository -y ppa:ubuntu-toolchain-r/test
apt-get update
if [ "$CC" == "gcc" ]; then
	apt-get install -y ${CC}-${POCO_COMPILER_VERSION} ${CXX}-${POCO_COMPILER_VERSION}
	update-alternatives --install /usr/bin/${CC} ${CC} /usr/bin/${CC}-${POCO_COMPILER_VERSION} 60 \
						--slave /usr/bin/${CXX} ${CXX} /usr/bin/${CXX}-${POCO_COMPILER_VERSION}
elif [ "$CC" == "clang" ]; then
	if [ -z `grep "http://llvm.org/apt/" /etc/apt/sources.list` ]; then
		bash -c "cat >> /etc/apt/sources.list" < build/script/clang.apt
	fi
	wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key|apt-key add -
	apt-get update  -qq
	apt-get install -qq -y ${CC}-${POCO_COMPILER_VERSION} lldb-${POCO_COMPILER_VERSION} libc++-dev libc++abi-dev
fi

export CC="${CC}-${POCO_COMPILER_VERSION}"
export CXX="${CXX}-${POCO_COMPILER_VERSION}"

function recreate_file {
	file="$1"
	if [ -f $file ]; then
		rm $file;
	fi
	touch $file;
}

prefix=/out/$CONTAINER_NAME

CFGOUTFILE="$prefix.config.out"
recreate_file $CFGOUTFILE

BLDOUTFILE="$prefix.build.out"
recreate_file $BLDOUTFILE

TSTOUTFILE="$prefix.test.out"
recreate_file $TSTOUTFILE

$CXX --version | tee $OUTFILE

export HOME="/root"
export POCO_BASE=`pwd`

make -s -j4 clean | tee $BLDOUTFILE
make -s -j4 distclean | tee $BLDOUTFILE
make -s -j4 | tee $BLDOUTFILE
build/script/runtests.sh | tee $TSTOUTFILE

function spin {
    echo "Idle script (to keep container up) running."

    cleanup ()
    {
        kill -s SIGTERM $!
        exit 0
    }

    trap cleanup SIGINT SIGTERM

    while [ 1 ]
    do
        sleep 60 &
        wait $!
    done
}
