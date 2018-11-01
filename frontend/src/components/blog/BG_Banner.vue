<template>
  <div class="banner">
    <div class="content">
      <div class="con-l">
        <div class="ban-ss" v-for="bs in blogs" v-if="blogs!=null">
          <img :src="bs.blog_image" alt="">
          <div class="cont-t">
            <p class="biaoqian">{{bs.blog_cate.cate_name}}<span class="xian"></span></p>
            <h3 class="title">{{bs.blog_name}}</h3>
            <p class="detail">{{bs.blog_detail}}.</p>
          </div>
        </div>
      </div>
      <div class="con-r">
        <div class="r-l">
          <p class="r-l-title">站长推荐<span class="xian"></span></p>
          <ul class="ul-zh">
            <li v-for="blog in blogs" v-if="blogs!=null"><a href="javascript:void(0)" class="active">
             <span>today, 10:11</span><br>
              {{blog.blog_detail}}
            </a>
            </li>

          </ul>
        </div>
      </div>
    </div>
    <div class="conten-bot">
      <div class="bot-t">
          <h3>odinh-Title<span class="xian xian-l"></span></h3>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from "jquery"
  import {zhan_remember} from "../../request/api";

  function sub() {
    var y = 100;
    var indecx =0;
    var left_ul = $('.con-l');
    var li_lists = $('.ban-ss');
    var list_length = li_lists.length;
    let first_li = li_lists.eq(0).clone();
    let last_li = li_lists.eq(list_length - 1).clone();
    left_ul.append(first_li);
    left_ul.prepend(last_li);
    setInterval(function () {
      if (indecx > list_length) {
        left_ul.css({'top': '-' + 100 + '%'});
        indecx = 2;
      } else {
        indecx++;
      }
      left_ul.animate({'top': '-' + indecx * y + '%'}, 1000);

    }, 6000);
    $('.ul-zh').children('li').click(function () {
         let index = $(this).index();
         indecx = index;
          left_ul.animate({'top': '-' + index * y + '%'}, 1000);
    })
  }
  export default {
    name: "BG_Banner",
  data(){
      return{
        blogs:null
      }
  },
    updated(){
      sub()
    },
    created(){
        zhan_remember().then(res=>{
          this.blogs = res.data.data
        })
    }
  }
</script>

<style scoped>
  .banner {
    width: 100%;
    background: #303d4a;
    height: 500px;
    border-top: 3px solid #f9e188;
    z-index: 1;
  }

  .content {
    width: 75%;
    height: 100%;
    margin: 0 auto;
    position: relative;
    /*box-sizing: border-box;*/
    overflow: hidden;
    z-index: 2;
  }

  .con-l {
    width: 65%;
    height: 1000%;
    background: #303d4a;
    position: absolute;
    float: left;
    top: -100%;
  }

  .con-l .ban-ss:first-of-type {
    margin-top: 0;
  }

  .con-l .ban-ss {
    width: 100%;
    height: 10%;
    position: relative;
  }

  .con-l .ban-ss > img {
    width: 100%;
    height: 100%;
  }

  .cont-t {
    position: absolute;
    width: 60%;
    height: 50%;
    bottom: 50px;
    left: 50px;
  }

  .biaoqian {
    text-transform: uppercase;
    text-space: 2px;
    color: #f9e188;;
    position: relative;
    margin-top: 50px;
  }

  .xian {
    width: 20px;
    height: 1px;
    background: #f9e188;
    position: absolute;
    bottom: -3px;
    left: 0;
    display: block;
  }

  .title {

    color: white;
    font-size: 25px;
    font-weight: bold;
    padding-top: 20px;
  }

  .detail {
    color: white;
  }

  .con-r {
    float: right;
    width: 35%;
    height: 100%;
    z-index: 3;
    border-right: 1px solid #ff6357;
    border-left: 1px solid #ff6357;
    background: rgba(0,0,0,.2);
  }

  .r-l {
    width: 100%;
    height: 100%;
    padding: 20px;
    z-index: 4;
  }

  .r-l-title {
    width: 100%;
    font-size: 20px;
    color: white;
    text-transform: uppercase;
    position: relative;
  }

  .ul-zh {
    width: 100%;
    border-left: 3px solid #888;
    z-index: 5;
  }

  .ul-zh > li {
    width: 100%;
    margin: 10px;
    padding: 20px 30px 20px 10px;
  }
  .ul-zh > li >a{
    font-size: 15px;
    color: white;
    text-decoration: none;
    outline: none;
    display: block;
    line-height: 30px;
    height: 60px;
  }
  .ul-zh > li >a>span{
    color: black;
    position: relative;
  }
  .ul-zh > li >a>span:before{
    content: "";
    position: absolute;
    left: -29px;
    top: 0;
    display: block;
    width: 15px;
    height: 15px;
    /*background: white;*/
    background-image: url("../../assets/BLOG/png-sprite/96dpi/sprite.png");
    background-repeat: no-repeat;
    background-position: -117px -64px;
    border-radius: 50%;

  }
  .ul-zh > li >a:hover {
    color: crimson;
  }

    .ul-zh > li >a:focus span:before{
      background-position: -49px -93px;
    }
  .ul-zh > li >a:focus{
    color: crimson;
  }

  .conten-bot{
    width: 100%;
    height: 70px;
    border-top: 1px solid #888;
    box-shadow: 5px 5px 5px rgba(0,0,0,.05);
  }
.conten-bot .bot-t{
  width: 75%;
  height: 100%;

  margin: 0 auto;
  line-height: 50px;
}
  .conten-bot .bot-t h3{
    color: black;
    text-transform: uppercase;
    line-height: 70px;
    padding: 0;
    margin: 0;
    position: relative;
  }
  .xian-l{
    bottom: 20px;
    width: 50px;
  }
</style>
