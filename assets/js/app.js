/**
 * App entry
 *
 * @author victor
 * @date 2015/10/07
 */

'use strict'

require('expose?$!expose?jQuery!jquery');
//require("bootstrap-webpack");
//require('!style!css!less!../less/style.less');
const Navbar = require('./navbar.js');

Navbar.markCurrentUrl();

