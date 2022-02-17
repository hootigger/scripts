/*
 * @Project: scripts
 * @File: /sendWrapper.js
 * @Created Date: 2022-02-16 16:52:23
 * @Last Modified: 2022-02-16 16:52:23
 * @Author: Hootigger
 * 
 * Copyright (c) 2022 Hootigger
 */

const send = require('./sendNotify')

async function sendNotify(text, ...desp) {
    desp = desp.join('\n')
    await send.sendNotify(text, desp)
}

module.exports = {
    sendNotify
}