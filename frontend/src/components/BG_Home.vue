<template>
  <div class="bg-home">
    <!--<BG_nav></BG_nav>-->
    <!--<BG_Nav_L></BG_Nav_L>-->
    <MA_TOP></MA_TOP>
    <BG_Banner></BG_Banner>
    <BG_Content></BG_Content>
    <BG_Detail></BG_Detail>
    <BG_Pbl></BG_Pbl>
    <BG_Footer></BG_Footer>
    <MA_Solider></MA_Solider>
  </div>

</template>

<script>
  import BG_nav from './blog/BG_nav'
  import BG_Nav_L from './blog/BG_Nav_L'
  import BG_Banner from './blog/BG_Banner'
  import BG_Content from './blog/BG_Content'
  import BG_Detail from './blog/BG_Detail'
  import BG_Pbl from './blog/BG_Pbl'
  import BG_Footer from './blog/BG_Footer'
  import MA_TOP from './main/MA_NAV'
  import MA_Solider from './main/MA_Solider'
    export default {
        name: "Home",
        components:{BG_nav,BG_Nav_L,BG_Banner,BG_Content,BG_Detail,BG_Pbl,BG_Footer,MA_TOP,MA_Solider},
    }
</script>

<style scoped>
    .bg-home{
      z-index: -1;
    }
</style>
