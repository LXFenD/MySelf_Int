<template>
    <div class="bg_detail">
      <MA_TOP></MA_TOP>
      <BG_DE_Content></BG_DE_Content>
      <BG_Footer></BG_Footer>
    </div>
</template>

<script>
  import MA_TOP from './main/MA_NAV'
  import BG_Footer from './blog/BG_Footer'
  import BG_DE_Content from './blog/BG-DE/BG_DE_Content'
    export default {
        name: "BG_Detail",
      components:{
          MA_TOP,BG_Footer,BG_DE_Content
        }
    }
</script>

<style scoped>

</style>
