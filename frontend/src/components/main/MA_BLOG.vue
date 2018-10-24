<template>
    <div class="blog_ma">
      <div class="blog">
          <div class="blog-top">
            <p class="blog-title">最新文章 <span class="xia"></span></p>
            <div class="flexs ">
              <ul >
                <li v-for="blog in blogs" v-if="blogs!=null">
                  <div class="u-l-d">
                    <img :src="blog.blog_image" alt="">
                    <div class="boot">
                      <p class="title">分类：<span class="xian xian-l"><i>{{blog.blog_cate.cate_name}}</i></span></p>
                      <p class="t-titt">{{blog.blog_name}}<span class="xxx"></span></p>
                      <p class="p-de">{{blog.blog_detail}}</p>
                    </div>
                  </div>
                </li>

              </ul>
            </div>
          </div>
      </div>
    </div>
</template>

<script>
  import {get_six_blog} from "../../request/api";
  import $ from "jquery"
    export default {
        name: "MA_BLOG",
      data(){
        return{
          blogs:null
        }
      },
      created(){
     get_six_blog().then(res=>{
       this.blogs=res.data.data
     })
    },
      mounted(){
           $(window).scroll(function () {
        let sc = $(this).scrollTop();
        if (sc > 1200) {
          $(' .flexs ul li').animate({'height': '300px'},500);
          $(' .u-l-d img').animate({'height': '300px'},500);
          $('.flexs').addClass("animated lightSpeedIn")
        }
           })
      }
    }
</script>

<style scoped>
  .blog_ma{
    width: 100%;
    margin-top: 20px;
  }
  .blog{
    width: 75%;
    height: 750px;
    margin: 0 auto;

  }
  .blog-top{
    text-align: center;
    height: 70px;
    line-height: 70px;

  }
  .xia{
    position: absolute;
    width: 100px;
    height: 3px;
    top: 10px;
    left: 46%;
    background: crimson;

  }
  .blog-title{
    font-size: 25px;
    color: black;
    position: relative;
  }
  .flexs{
    width: 100%;
    height: 0px;
  }
  .flexs ul{
    width: 100%;
    padding: 0;
    list-style-type: none;
    display: flex;
    flex-wrap: wrap;
  }
  .flexs ul li{
    flex-basis: 30%;
    flex-grow: 1;
    margin: 10px;
    overflow: hidden;
  }
  .u-l-d{
    width: 100%;
    position: relative;
  }
  .u-l-d img{
    width: 100%;
  }
  .flexs ul li:hover img{
    transform: scale(1.05);
    transition: all .5s ease;
  }
  .u-l-d .boot{
    width: 100%;
    position: absolute;
    height: 50%;
    left: 0;
    bottom: 0;
    background: rgba(0,0,0,.5);
    padding: 10px;
  }

  .u-l-d .boot .title{
    margin: 0;
    text-align: left;
    color: goldenrod;
    text-transform: uppercase;
    line-height: 30px;
  }
  .u-l-d .boot .t-titt{
    color: white;
    font-size: 20px;
    text-align: left;
    position: relative;
    cursor: pointer;
    line-height: 30px;
    max-height: 30px;
    overflow: hidden;
  }
  .xxx{
    content: "";
    position: absolute;
    height: 2px;
    width: 0;
    background: white;
    bottom: 0;
    left: 0;

  }
  .p-de{
    line-height: 22px;
    text-align: left;
  }
.u-l-d .boot .t-titt:hover .xxx{
  width: 50%;
  transition: width 1s ease;
}
</style>
