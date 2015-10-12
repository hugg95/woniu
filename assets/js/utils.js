/**
 * Utils module
 *
 * @author victor li
 * @date 2015/10/11
 */

let Utils = {};

let cookie = {};

/**
 * add a new cookie
 * @param key value key/name
 * @param value cookie's value
 */
cookie.addCookie = function(key, value, expiresHours) {
    const cookieStr = key + '=' + value;
    let now = new Date();
    if (expiresHours > 0) {
        now.setTime(now.getTime() + expiresHours * 60 * 60 * 1000);
    }
    document.cookie = cookieStr + ';expires=' + now.toGMTString() + ';path=/';
};

Utils.cookie = cookie;

module.exports = Utils;

