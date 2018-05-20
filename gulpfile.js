const gulp = require("gulp");
const concat = require("gulp-concat");
const sass = require("gulp-sass");

const dirs = {
  build: "./build/",
  css: "./app/static/",
};

dirs.watch = {
  css: dirs.css + "**/*.scss"
};


gulp.task("css", function() {
  return gulp.src(dirs.watch.css)
    .pipe(sass({ outputStyle: "compressed" }).on("error", sass.logError))
    .pipe(concat("style.css"))
    .pipe(gulp.dest(dirs.build));
});

gulp.task("css:watch", function() {
  gulp.watch(dirs.watch.css, ["css"]);
});

gulp.task("default", ["css"]);
gulp.task("watch", ["css:watch"]);