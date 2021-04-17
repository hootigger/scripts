#!/usr/bin/env bash

make_cron() {
    sed -i "1i\/**\n* cron: $1\n*/\n" $2
}

process_chavyleung() {
    local prefix=$1
    sed -i "s/\$.getdata(\$.KEY_mobile)/process.env.MOBILE_10000/" $prefix/10000/10000.js
    sed -i "s/\$.getdata(\$.KEY_signbody)/process.env.SIGNBODY_10000/" $prefix/10000/10000.js
    sed -i "s/\$.msg/require('.\/sendNotify').sendNotify/" $prefix/10000/10000.js
    make_cron "0 7 * * *" $prefix/10000/10000.js

    sed -i "s/\$.getdata('chavy_cookie_tieba')/process.env.TIEBA_COOKIE/" $prefix/tieba/tieba.js
    sed -i "s/\$.msg/require('.\/sendNotify').sendNotify/" $prefix/tieba/tieba.js
    make_cron "1 0 * * *" $prefix/tieba/tieba.js

    sed -i "s/\$.getdata('chavy_cookie_neteasemusic')/process.env.NETEASE_MUSIC_CK/" $prefix/neteasemusic/neteasemusic.js
    sed -i "s/\$.msg/require('.\/sendNotify').sendNotify/" $prefix/neteasemusic/neteasemusic.js
    make_cron "5 7 * * *" $prefix/neteasemusic/neteasemusic.js
    
    sed -i "s/\$.getdata(\$.KEY_signcookie)/process.env.XMLY_CK/" $prefix/ximalaya/ximalaya.js
    sed -i "s/\$.msg/require('.\/sendNotify').sendNotify/" $prefix/ximalaya/ximalaya.js
    make_cron "10 7 * * *" $prefix/ximalaya/ximalaya.js

    cp $prefix/10000/10000.js my/scripts/
    cp $prefix/tieba/tieba.js my/scripts/
    cp $prefix/neteasemusic/neteasemusic.js my/scripts/
    cp $prefix/ximalaya/ximalaya.js my/scripts/
}

main() {
    process_chavyleung $GITHUB_WORKSPACE/chavyleung_scripts
}

main