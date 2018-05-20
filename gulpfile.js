const gulp = require("gulp");
const concat = require("gulp-concat");
const sass = require("gulp-sass");

const BUILD_DIR = "./build/";


gulp.task("css", function() {
  return gulp.src("./app/**/*.scss")
    .pipe(sass({ outputStyle: "compressed" }).on("error", sass.logError))
    .pipe(concat("style.css"))
    .pipe(gulp.dest(BUILD_DIR));
});

gulp.task("css:watch", function() {
  gulp.watch("./app/**/*.scss", ["css"]);
});