module.exports = function(grunt) {
    grunt.initConfig({
        less: {
            development: {
                options: {
                    paths: ['assets/less']
                },
                files: {
                    'assets/css/style.css': 'assets/less/style.less',
                    'assets/css/login.css': 'assets/less/login.less'
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-less');
};
