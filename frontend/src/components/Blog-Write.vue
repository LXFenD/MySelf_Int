<template>
    <div class="blog-write">
      <MA_TOP></MA_TOP>
      <Content></Content>
      <BG_Footer></BG_Footer>
    </div>
</template>

<script>
  import Content from '../components/blog/blog-write/Content'
  import MA_TOP from './main/MA_NAV'
  import BG_Footer from './blog/BG_Footer'
    export default {
        name: "Blog-Write",
        components:{
          Content,MA_TOP,BG_Footer
        }
    }
</script>

<style scoped>

</style>
