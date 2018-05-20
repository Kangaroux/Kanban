const { spawn } = require("child_process");
const autoprefixer = require("gulp-autoprefixer");
const concat = require("gulp-concat");
const gulp = require("gulp");
const sass = require("gulp-sass");

///////////////////
// Options
///////////////////
const dirs = {
  build: "build/",
  css: "app/static/",
};

dirs.watch = {
  css: dirs.css + "**/*.scss"
};

function webpack(opts) {
  return spawn("webpack", opts, { stdio: "inherit" });
}

///////////////////
// Tasks
///////////////////
gulp.task("css", function() {
  return gulp.src(dirs.watch.css)
    .pipe(concat("style.css"))
    .pipe(sass({
        outputStyle: "compressed",
        includePaths: ["node_modules"],
      }).on("error", sass.logError))
    .pipe(autoprefixer({
      browsers: ["last 2 versions", "> 1%"],
      cascade: false,
    }))
    .pipe(gulp.dest(dirs.build));
});

gulp.task("js", function() {
  webpack(["-d"]);
});

gulp.task("css:watch", function() {
  gulp.watch(dirs.watch.css, ["css"]);
});

gulp.task("js:watch", function() {
  webpack(["-d", "--watch"])
});

gulp.task("default", ["css", "js"]);
gulp.task("watch", ["css:watch", "js:watch"]);