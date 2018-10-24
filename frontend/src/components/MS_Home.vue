<template>
    <div class="ms_home">
      <MA_TOP></MA_TOP>
      <MS_Top></MS_Top>
      <MS_Banner></MS_Banner>
      <MS_Banner_Img></MS_Banner_Img>
      <Ms_Flex></Ms_Flex>
      <MS_Detail></MS_Detail>
      <MS_Bottom></MS_Bottom>
      <MA_Solider></MA_Solider>
      <div class="ddd"  @click="ddd">
        <img src="../assets/myself/backtop.png" alt="">
      </div>
    </div>
</template>

<script>
  import $ from "jquery"
  import MA_TOP from './main/MA_NAV'
  import MS_Top from './myself/MS_Top'
  import MS_Banner from './myself/MS_Banner'
  import MS_Banner_Img from './myself/MS_Banner_Img'
  import Ms_Flex from './myself/MS_Flex'
  import MS_Detail from './myself/MS_Detail'
  import MS_Bottom from './myself/MS_Bottom'
  import MA_Solider from './main/MA_Solider'
    export default {
        name: "Home",
      components:{
          MS_Top,MS_Banner,MS_Banner_Img,Ms_Flex,MS_Detail,MS_Bottom,MA_TOP,MA_Solider
      },methods:{
          ddd(){
            $('body,html').animate({'scrollTop':'0'},2000)
          }
      }

    }
</script>

<style scoped>

.ddd{
  width: 50px;
  height: 50px;
  position: fixed;
  right: 10px;
  bottom: 10px;
  border: 1px solid #ffe922;
  text-align: center;
      line-height: 50px;
  cursor: pointer;
}
  .ddd img{
    width: 60%;
    height: 60%;
  }
</style>
