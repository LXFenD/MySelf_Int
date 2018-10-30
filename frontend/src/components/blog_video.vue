<template>
    <div class="video">
      <MA_TOP></MA_TOP>
          <div  class="prism-player" id="J_prismPlayer"></div>
      <BG_Footer></BG_Footer>
    </div>
</template>

<script>
   import MA_TOP from './main/MA_NAV'
    import BG_Footer from './blog/BG_Footer'
    import {get_play_info} from "../request/api";
    export default {
      name: "blog_video",
      data(){
        return{
          vid:""
        }
      },
      components:{
        MA_TOP,BG_Footer
      }
      ,
      created(){
          get_play_info({'video_id':this.$route.params.video_id}).then(res=> {
            this.vid = res.data.data.PlayInfoList.PlayInfo[0].PlayURL;
            new Aliplayer({
                id: 'J_prismPlayer',
                width: '100%',
                height:'600px',
                autoplay: false,
                source : this.vid,
            })
          })

      }
    }
</script>

<style scoped>
    .video{
      width: 100%;

    }
  .prism-player{
      width: 75%;
    height: 600px;
    margin: 30px auto;
    margin-top: 70px;
  }
</style>
