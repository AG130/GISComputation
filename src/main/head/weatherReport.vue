<template>
  <div id="he-plugin-simple"></div>
</template>
<script>
export default {
  created() {
    window.WIDGET = {
      CONFIG: {
        modules: "01234",
        background: "4",
        backgroundColor: "66CCFF",
        tmpColor: "FFFFFF",
        tmpSize: "16",
        cityColor: "FFFFFF",
        citySize: "16",
        aqiColor: "FFFFFF",
        aqiSize: "16",
        weatherIconSize: "24",
        alertIconSize: "18",
        padding: "10px 10px 10px 10px",
        shadow: "0",
        language: "auto",
        fixed: "true",
        vertical: "top",
        horizontal: "left",
        right: "8",
        top: "10",
        key: "a1d4db0a75ee4f8fa651a33e1a846db3",
      },
    };
    (function (d) {
      var c = d.createElement("link");
      c.rel = "stylesheet";
      c.href =
        "https://widget.heweather.net/simple/static/css/he-simple.css?v=1.4.0";
      var s = d.createElement("script");
      s.src =
        "https://widget.heweather.net/simple/static/js/he-simple.js?v=1.4.0";
      var sn = d.getElementsByTagName("script")[0];
      sn.parentNode.insertBefore(c, sn);
      sn.parentNode.insertBefore(s, sn);
    })(document);
  },
};
</script>
<style>
</style>