const { spawn } = require("child_process");
const autoprefixer = require("gulp-autoprefixer");
const concat = require("gulp-concat");
const gulp = require("gulp");
const sass = require("gulp-sass");

const dirs = {
  build: "build/",
  css: "app/static/",
};

dirs.watch = {
  css: dirs.css + "**/*.scss"
};

gulp.task("css", function() {
  return gulp.src(dirs.watch.css)
    .pipe(sass({
        outputStyle: "compressed",
        includePaths: ["node_modules"],
      }).on("error", sass.logError))
    .pipe(autoprefixer({
      browsers: ["last 2 versions", "> 1%"],
      cascade: false,
    }))
    .pipe(concat("style.css"))
    .pipe(gulp.dest(dirs.build));
});

gulp.task("js", function() {
  spawn("webpack");
});

gulp.task("css:watch", function() {
  gulp.watch(dirs.watch.css, ["css"]);
});

gulp.task("js:watch", function() {
  spawn("webpack", ["--watch"])
});

gulp.task("default", ["css", "js"]);
gulp.task("watch", ["css:watch", "js:watch"]);