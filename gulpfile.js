// Only used to build our CSS/JS. We use sphinx-autobuild to actually
// serve the generated Sphinx documentation during development.

var gulp = require("gulp");
var concat = require("gulp-concat");
var postcss = require("gulp-postcss");
var rename = require("gulp-rename");
var sass = require("gulp-sass");
var sourcemaps = require("gulp-sourcemaps");
var uglify = require("gulp-uglify");

var Fiber = require("fibers");
sass.compiler = require("sass");

var autoprefixer = require("autoprefixer");
var cssnano = require("cssnano");
var easyImport = require("postcss-easy-import");

var plugins = [easyImport(), autoprefixer(), cssnano()];
var src_path = "./src/furo/assets/";
var dest_path = "./src/furo/theme/furo/static";

function css() {
  return gulp
    .src(
      src_path + "styles/[!_]*.sass", { since: gulp.lastRun(css) })
    .pipe(sourcemaps.init())
    .pipe(sass({ fiber: Fiber }).on("error", sass.logError))
    .pipe(postcss(plugins))
    .pipe(rename({ dirname: "styles", extname: ".css" }))
    .pipe(sourcemaps.write(""))
    .pipe(gulp.dest(dest_path));
}

function javascript() {
  return gulp
    .src(src_path + "scripts/[!_]*.js", { since: gulp.lastRun(javascript) })
    .pipe(sourcemaps.init())
    .pipe(concat("scripts/main.js"))
    .pipe(uglify())
    .pipe(sourcemaps.write(""))
    .pipe(gulp.dest(dest_path));
}

exports.build = gulp.parallel(javascript, css);
