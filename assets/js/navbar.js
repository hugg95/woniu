require('expose?$!expose?jQuery!jquery');

let Navbar = {

    // mark the current route in navigation
    markCurrentUrl: function() {
        const navbars = $('ul.navbar-nav>li>a');
        const currentPathName = window.location.pathname;
        navbars.each(function(index, item) {
            item = $(item);
            if (item.attr('href') === currentPathName)
                item.css({'background-color': '#006699', 'color': '#fff'});
        });
    }

}

module.exports = Navbar;

