<test>
  <h1>Hi, { getName() }!</h1>

  <script>
    this.getName = () => this.opts.name;
  </script>
</test>