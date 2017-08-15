module.exports = function(grunt) {
    grunt.initConfig({
        
        // Grunt-sass 
        // sass (libsass) config
        sass: {
            options: {
                sourceMap: true,
                relativeAssets: false,
                outputStyle: 'compressed',
                sassDir: 'src/scss',
                cssDir: 'assets/css',
                includePaths: [
                    'node_modules/foundation-sites/scss',
                    'node_modules/font-awesome/scss',
                ]
            },
            build: {
                files: [{
                    expand: true,
                    cwd: 'src/scss/',
                    src: ['**/*.scss'],
                    dest: 'assets/css',
                    ext: '.css'
                }]
            }
        },
        
        // Watch a file for changes
        watch: {
            scss: {
                files: ['src/scss/**/*'],
                tasks: ['sass'],
                options: {
                    spawn: false,
                },
            },
            scripts: {
                files: ['src/js/**/*.js'],
                tasks: ['concat',],
                options: {
                    spawn: false,
                },
            },
        },
        
        // Grunt-concat
        concat: {
            options: {
                separator: ';\n\n',
            },
            dist: {
                src: [
                    'node_modules/jquery/dist/jquery.min.js',
                    'node_modules/foundation-sites/dist/js/foundation.min.js', 
                    // 'node_modules/selectize/dist/js/standalone/selectize.min.js',
                    'node_modules/spin.js/spin.min.js',
                    // 'node_modules/leaflet/dist/leaflet.js', 
                    'src/js/app.js'
                ],
                dest: 'assets/js/app.js',
            },
        },    
        copy: {
            main: {
                expand: true,
                src: 'node_modules/jquery/dist/jquery.min.map',
                dest: 'assets/js/jquery.min.map',
            },
        },            
        
    });
    
    
    // Define the modules we need for these tasks:
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-watch');
    
    // Here are our tasks 
    grunt.registerTask('default', [ 'build' ]);
    grunt.registerTask('build', [ 'sass', 'concat']);
    grunt.registerTask('dev', [ 'watch' ]);
    
};