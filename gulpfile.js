// Only used to build our CSS/JS. We use sphinx-autobuild to actually
// serve the generated Sphinx documentation during development.

var gulp = require("gulp");
var concat = require('gulp-concat');
var postcss = require('gulp-postcss');
var rename = require("gulp-rename");
var sass = require("gulp-sass");
var uglify = require('gulp-uglify');

var Fiber = require('fibers');
sass.compiler = require('sass');

var autoprefixer = require("autoprefixer");
var cssnano = require("cssnano");
var easyImport = require("postcss-easy-import");

var plugins = [
  easyImport(),
  autoprefixer(),
  cssnano(),
];
var src_path = "./src/mawek/assets/";
var dest_path = "./src/mawek/theme/static";


function css() {
  return gulp
    .src(src_path + "styles/[!_]*.scss")
    .pipe(sass({fiber: Fiber}).on('error', sass.logError))
    .pipe(postcss(plugins))
    .pipe(rename({dirname: "styles", extname: ".css"}))
    .pipe(gulp.dest(dest_path));
}

function javascript(cb) {
  return gulp
    .src(src_path + "scripts/[!_]*.js")
    .pipe(concat('scripts/main.js'))
    .pipe(uglify())
    .pipe(gulp.dest(dest_path));
}

exports.build = gulp.parallel(javascript, css);
