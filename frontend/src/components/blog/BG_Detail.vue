<template>
  <div class="bg_detail">
    <div class="bg-d">
      <div class="bg-d-l">
        <div class="top" v-if="blogs!=null">
          <div class="top-l" @click="link_sub(blogs[3].id,blogs[2].blog_video_url)" >
            <img :src="blogs[3].blog_image" alt="">
            <div class="top-detail">
              <p class="title">{{blogs[3].blog_name}}<span class="xian xian-l"></span></p>
              <p>
                <a href="">{{blogs[3].blog_detail}}</a>
              </p>
            </div>
          </div>
          <div class="top-r " @click="link_sub(blogs[4].id,blogs[2].blog_video_url)">
            <img :src="blogs[4].blog_image" alt="">
            <div class="top-detail">
              <p class="title">{{blogs[4].blog_name}}<span class="xian xian-l"></span></p>
              <p>
                <a href="">{{blogs[4].blog_detail}}</a>
              </p>
            </div>
          </div>
        </div>
        <div class="top_l " v-if="blogs!=null">
          <div class="top-l-l " @click="link_sub(blogs[1].id,blogs[2].blog_video_url)">
            <img :src="blogs[1].blog_image" alt="">
            <div class="top-detail">
              <p class="title">{{blogs[1].blog_name}}<span class="xian xian-l"></span></p>
              <p>
                <a href="">{{blogs[1].blog_detail}}</a>
              </p>
            </div>
          </div>
          <div class="top-l-r " @click="link_sub(blogs[2].id,blogs[2].blog_video_url)">
            <img :src="blogs[2].blog_image" alt="">
            <div class="top-detail">
              <p class="title">{{blogs[2].blog_name}}<span class="xian xian-l"></span></p>
              <p>
                <a href="">{{blogs[2].blog_detai}}l</a>
              </p>
            </div>
          </div>
        </div>
        <div class="d_l" v-if="blogs!=null" @click="link_sub(blogs[5].id,blogs[5].blog_video_url)">
          <img :src="blogs[5].blog_image" alt="">
          <div class="top-detail">
            <p class="title">{{blogs[5].blog_name}}<span class="xian xian-l"></span></p>
            <p>
              <a href="">{{blogs[5].blog_detail}}</a>
            </p>
          </div>
        </div>
      </div>
      <div class="bg-d-r">
        <p class="title">最新文章<span class="xian xian-l"></span></p>
        <ul>
          <li v-for="b in blogs">
            <h4 class="hhhd">{{b.blog_name}}</h4>
            <p class="title-l">
              {{b.blog_detail}}
            </p>
            <div class="dett">
              <p class="fass-times"><span class="fa fa-share"></span>{{b.blog_date|dates}}</p>
              <p class="zhuan" @click="link_sub(b.id,b.blog_video_url)"><span class="fa fa-arrow-right"></span>转到</p>
            </div>

          </li>

        </ul>
      </div>
    </div>

  </div>
</template>

<script>
  import {get_six_blog} from "../../request/api";

  export default {
    name: "BG_Detail",

    data(){
      return{
        blogs:null
      }
    },methods:{
      link_sub(blog_id,vid_url){
        if(vid_url){
          this.$router.push({
              path:'/bg_detail/',
              name:'BG_Detail',
              params:{
                'blog_id':blog_id,
                'vid_url':vid_url
              }
            })
        }else {
         this.$router.push({
              path:'/bg_detail/',
              name:'BG_Detail',
              params:{
                'blog_id':blog_id,
              }
            })
        }

      }
    }
    ,
    created(){
     get_six_blog().then(res=>{
       this.blogs=res.data.data
     })
    },filters: {
      dates: function (mydate) {
        let titm = new Date(mydate).getTime();
        let sc = parseInt((new Date().getTime() - titm) / 1000);
        let index = "";
        if (sc > 0 && sc < 60) {
          return "刚刚发布"
        } else if (sc / 60 > 0 && sc / 60 < 60) {
          index = parseInt(sc / 60);
          return index + '分钟前发布'
        }
        else if (sc / 3600 > 0 && sc / 3600 < 24) {
          index = parseInt(sc / 3600);
          return index + "小时前发布"
        } else if (sc / (3600 * 24) > 0 && sc / (3600 * 24) < 30) {
          index = parseInt(sc / (3600 * 24));
          return index + '天前发布'
        } else {
          let d = new Date(mydate);
          let year = d.getFullYear();
          let m = d.getMonth() + 1;
          let dy = d.getDate();
          return year + '-' + m + '-' + dy + ' ' + '发布'
        }
      }
    }
  }
</script>

<style scoped>
  .bg_detail {
    width: 100%;
  }

  .hhhd{
    max-height: 20px;
    overflow: hidden;
  }
  li p {
    padding: 0;
    margin: 0
  }

  .dett {
    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;

  }

  .dett .zhuan {
    width: 50%;
    display: inline-block;
    text-align: right;
    font-size: 14px;

    cursor: pointer;
    color: goldenrod;

    float: right;
  }

  .dett .fass-times {
    width: 50%;
    float: left;
    font-size: 14px;
  }

  .title-l {
    max-height: 53px;
    overflow: hidden;
    font-size: 14px;
  }

  .bg_detail .bg-d {
    width: 75%;
    height: 100%;
    overflow: hidden;
    margin: 0 auto;
  }

  .bg_detail .bg-d .bg-d-l {
    width: 73%;
    height: 100%;
    float: left;
  }

  .bg_detail .bg-d .bg-d-l .top {
    width: 100%;
    overflow: hidden;
    height: 300px;

  }

  .bg_detail .bg-d .bg-d-l .top .top-l {
    width: 67%;
    height: 100%;
    float: left;
    position: relative;
  }

  img {
    height: 100%;
    width: 100%;
  }

  .top-detail {
    position: absolute;
    width: 100%;
    height: 50%;
    background: rgba(0, 0, 0, .5);
    left: 0;
    bottom: 0;
    padding: 20px;
    overflow: hidden;
  }

  .title {
    font-size: 18px;
    color: goldenrod;
    text-transform: uppercase;
    position: relative;
    cursor: pointer;
    max-height: 23px;
    overflow: hidden;
  }

  .xian {
    width: 20px;
    height: 2px;
    background: #f9e188;
    position: absolute;
    bottom: -3px;
    left: 0;
    display: block;
  }

  .bg_detail .bg-d .bg-d-l .top .top-r {
    width: 32%;
    height: 100%;
    float: right;
    position: relative;
  }

  .bg_detail .bg-d .bg-d-l .top_l {
    margin-top: 20px;
    width: 100%;
    overflow: hidden;
    height: 300px;
  }

  .bg_detail .bg-d .bg-d-l .top_l .top-l-l {
    width: 32%;
    height: 100%;
    float: left;
    position: relative;
  }

  .bg_detail .bg-d .bg-d-l .top_l .top-l-r {
    width: 67%;
    height: 100%;
    float: right;
    position: relative;
  }

  .bg_detail .bg-d .bg-d-l .d_l {
    margin-top: 20px;
    width: 100%;
    height: 300px;
    position: relative;
  }

  .bg_detail .bg-d .bg-d-r {
    width: 25%;
    height: 100%;
    float: right;
    background: white;
    padding: 10px;
  }

  .bg_detail .bg-d .bg-d-r .title {
    font-size: 20px;
    cursor: pointer;
  }

  .bg_detail .bg-d .bg-d-r .title:hover .xian {
    width: 100%;
    transition: all 0.5s ease;
  }

  .bg_detail .bg-d .bg-d-r ul {
    padding: 0;
    list-style-type: none;
    width: 100%;
  }

  .bg_detail .bg-d .bg-d-r ul li {
    width: 100%;
    height: 125px;
    margin-bottom: 13px;
    overflow: hidden;
    border-bottom: 1px dashed darkorange;
    margin-top: 20px;
  }

  .bg_detail .bg-d .bg-d-r ul li{
    text-space: 2px;
    text-overflow: ellipsis;
  }
  @keyframes spin {
    from {
      transform: translateX(-10px);
    }
    to {
      transform: translateX(0px);
    }

  }

  .fa-arrow-right {
    animation: spin 2s infinite;
  }
</style>
