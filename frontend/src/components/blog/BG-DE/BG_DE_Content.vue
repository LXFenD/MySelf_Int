<template>
  <div class="bg-de-cont">
    <div class="bg-de-cont-auto">
      <div class="show-detail" v-if="blog!=null">
        <div class="show-de-top">
          <h3 class="title-de">
            <span class="title-l title-logo"></span>
            {{blog.blog_name}}
          </h3>
          <div class="info-de">
            <span class="glyphicon glyphicon-user jie"></span><i>用户</i>
            <span class="glyphicon glyphicon-time jie"></span><i> {{blog.blog_date}}</i>
            <span class="glyphicon glyphicon-eye-open jie"></span><i> {{blog.blog_readnum}}</i>
            <span class="glyphicon glyphicon-heart jie"></span><i> {{blog.blog_zan}}</i>
          </div>

          <div class="deta-de">简介:{{blog.blog_detail}}</div>
           <h4>学习视频：</h4>
        <div class="prism-player" id="J_prismPlayer"></div>
          <h4>笔记编写：</h4>
        </div>
        <div class="show-de-cont">
          <div class="detail-cont" v-html="blog.blog_content">
          </div>
        </div>
      </div>
      <div class="show_list">
        <div class="show-list-top">
          <h4>
            <span class="title-l title-lo"></span>好文章
          </h4>
        </div>
        <ul class="show-list-cont">
          <li @click="sub_show" ref="show_1">
            <span class="trange"></span>
            <img src="../../../assets/5bc7048a38ed3.jpg" alt="">
            <div class="show-de">
              <p>分类：<i class="p-title">PYthon</i></p>
              <p class="p-name">标题：<i>标题：标题：标题：标题：标题：标题：</i></p>
              <p class="p-detail">简介: <i>简介简介简介简介简介简介简介简介简介简介简介：</i></p>
            </div>
          </li>
          <li @click="sub_show">
            <span class="trange" ref="show_1"></span>
            <img src="../../../assets/5bc7048a38ed3.jpg" alt="">
            <div class="show-de">
              <p>分类：<i class="p-title">PYthon</i></p>
              <p class="p-name">标题：<i>标题：标题：标题：标题：标题：标题：</i></p>
              <p class="p-detail">简介: <i>简介简介简介简介简介简介简介简介简介简介简介：</i></p>
            </div>
          </li>
          <li>
          </li>
          <li>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
  import {get_id_bg} from "../../../request/api";
  import {get_play_info} from "../../../request/api";

  export default {
    name: "BG_DE_Content",
    data() {
      return {
        blog: null,
        vid:null,
      }
    },
    created() {
      if (this.$route.params.blog_id) {
        get_id_bg({'blog_id': this.$route.params.blog_id}).then(res => {
          this.blog = res.data.data;
        })
      }
      if(this.$route.params.vid_url){
            get_play_info({'video_id': this.$route.params.vid_url}).then(res => {
            this.vid = res.data.data.PlayInfoList.PlayInfo[0].PlayURL;
            new Aliplayer({
              id: 'J_prismPlayer',
              width: '100%',
              height: '600px',
              autoplay: false,
              source:this.vid,
              //       })
              // })
            })
          })
        }

    },
    methods: {
      sub_show() {
        this.$refs.show_1.children[0].style.display = 'inline-block'
      }

    },
    mounted() {

    }
  }
</script>

<style scoped>
  p {
    color: white;
    font-size: 14px;
  }

  i {
    color: #eeeeee;
  }

  .trange {
    position: absolute;
    border-style: solid;
    border-width: 10px;
    left: -20px;
    top: 50%;
    border-color: transparent black transparent transparent;
    display: none;
  }


  .p-name {
    width: 100%;
    height: 20px;
    line-height: 20px;
    font-size: 14px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .p-detail {
    width: 100%;
    height: 40px;
    line-height: 40px;
    font-size: 14px;
    overflow: hidden;
  }

  .bg-de-cont {
    margin: 20px 0px;
    width: 100%;
  }

  .p-title {
    text-transform: uppercase;
    color: goldenrod;
  }

  .bg-de-cont-auto {
    width: 80%;
    margin: 0 auto;
    box-sizing: border-box;
    padding: 10px;
    overflow: hidden;
  }

  .title-l {
    /*display: inline-block;*/
    width: 30px;
    height: 30px;
    display: inline-block;
    background-size: cover;
    margin-right: 5px;

  }

  .show-detail {
    width: 74.7%;
    height: 100%;
    float: left;
    background: white;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, .07);
  }

  .show_list {
    width: 25%;
    height: 100%;
    float: right;
    padding: 10px;
    padding-left: 0px;
    background: white;
  }

  .show-de-top {
    width: 100%;
    box-sizing: border-box;
    padding: 10px;
  }

  .show-de-top .title-de {
    width: 100%;
    height: 32px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    padding: 0px;
    margin: 0px;
  }

  .show-de-top .title-de .title-logo {

    background: url("../../../assets/title.png") no-repeat;

  }

  .show-de-top .info-de {
    width: 100%;
    margin-top: 10px;
    height: 25px;
    line-height: 25px;
    padding: 0 10px;
  }

  .show-de-top .info-de .jie {
    color: #39b3d7;
    padding: 0 10px;
  }

  .deta-de {
    width: 100%;
    margin-top: 10px;
    padding: 10px;
    color: #fff;
    background: #bbb;
    border-radius: 0;
    border: none;
    font-size: 16px;
  }

  .detail-cont {
    padding: 10px;
    box-sizing: border-box;
  }

  blockquote {
    background: #eeeeee;
  }

  .show-list-top h4 {
    height: 32px;
    line-height: 18px;
  }

  .show-list-top .title-lo {
    background: url("../../../assets/tjks.png") no-repeat;
  }

  .show-list-cont {
    width: 100%;
    padding: 0;
    margin: 0;
  }

  .show-list-cont li {
    width: 100%;
    height: 200px;
    margin-top: 15px;
    background: #39b3d7;
    position: relative;
  }

  .show-list-cont li img {
    width: 100%;
    height: 100%;
  }

  .show-list-cont li .show-de {
    width: 100%;
    height: 50%;
    position: absolute;
    bottom: 0;
    left: 0;
    background: rgba(0, 0, 0, .5);
  }
</style>
