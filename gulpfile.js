const gulp = require("gulp");
const sass = require("gulp-sass");

const BUILD_DIR = "./build/";


gulp.task("css", function() {
  return gulp.src("./app/css/**/*.scss")
    .pipe(sass({ outputStyle: "compressed" }).on("error", sass.logError))
    .pipe(gulp.dest(BUILD_DIR + "css/"));
});

gulp.task("css:watch", function() {
  gulp.watch("./app/css/**/*.scss", ["css"]);
});