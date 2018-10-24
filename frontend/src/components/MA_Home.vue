<template>

  <div class="ma">
    <MA_TOP></MA_TOP>
    <MA_CONTENT></MA_CONTENT>
    <MA_BLOG></MA_BLOG>
    <MA_FOOTER></MA_FOOTER>
    <MA_Solider></MA_Solider>
  </div>
</template>

<script>

  import MA_TOP from './main/MA_TOP'
  import MA_CONTENT from './main/MA_CONTENT'
  import MA_BLOG from './main/MA_BLOG'
  import MA_FOOTER from './main/MA_FOOTER'
  import MA_Solider from './main/MA_Solider'

    export default {
        name: "Home",
      components:{MA_TOP,MA_CONTENT,MA_BLOG,MA_FOOTER,MA_Solider},
    }
</script>

<style scoped>
    .ma{
      z-index: -1;
    }
</style>
