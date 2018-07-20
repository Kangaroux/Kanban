const Gulp = require("gulp");
const Autoprefixer = require("gulp-autoprefixer");
const Sass = require("gulp-sass");

const srcDir = "./app/static/";
const dstDir = "./dist/"


function buildStylesheets(prod) {
  const sassOptions = {
    includePaths: [ "node_modules/" ],
    outputStyle: prod ? "compressed" : "nested"
  };

  return Gulp.src(srcDir + "css/*.scss")
    .pipe(Sass(sassOptions).on("error", Sass.logError))
    .pipe(Autoprefixer({
      cascade: false,
      browsers: ["last 2 versions", "> 1%"]
    }))
    .pipe(Gulp.dest(dstDir));
}

Gulp.task("scss", function() {
  buildStylesheets(false);
});

Gulp.task("scss:prod", function() {
  buildStylesheets(true);
});

Gulp.task('scss:watch', function () {
  Gulp.watch(srcDir + "css/**/*.scss", ['scss']);
});

Gulp.task("default", ["scss:prod"]);
Gulp.task("watch", ["scss", "scss:watch"]);