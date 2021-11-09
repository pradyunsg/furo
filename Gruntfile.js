const sass = require("sass");

const asset_path = "src/furo/assets/";

const theme_static_path = "src/furo/theme/furo/static/";
const theme_css = theme_static_path + "styles/furo.css";
const extensions_css = theme_static_path + "styles/furo-extensions.css";
const theme_js = theme_static_path + "scripts/furo.js";

module.exports = function (grunt) {
  grunt.initConfig({
    sass: {
      options: {
        implementation: sass,
        sourceMap: true,
      },
      dist: {
        files: {
          [theme_css]: asset_path + "styles/furo.sass",
          [extensions_css]: asset_path + "styles/furo-extensions.sass",
        },
      },
    },
    autoprefixer: {
      dist: {
        files: {
          [theme_css]: [theme_css],
        },
      },
    },
    browserify: {
      dist: {
        files: {
          [theme_js]: asset_path + "scripts/**.js",
        },
        options: {
          browserifyOptions: {
            plugin: ["tinyify"],
            debug: true,
          },
        },
      },
    },
    exorcise: {
      bundle: {
        options: {},
        files: {
          [theme_js + ".map"]: theme_js,
        },
      },
    },
    concurrent: {
      all: [
        ["browserify", "exorcise"],
        ["sass", "autoprefixer"],
      ],
    },
  });

  grunt.loadNpmTasks("grunt-autoprefixer");
  grunt.loadNpmTasks("grunt-browserify");
  grunt.loadNpmTasks("grunt-concurrent");
  grunt.loadNpmTasks("grunt-exorcise");
  grunt.loadNpmTasks("grunt-sass");

  grunt.registerTask("default", ["concurrent:all"]);
};
