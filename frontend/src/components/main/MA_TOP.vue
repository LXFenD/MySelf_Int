<template>
  <div class="ma-top">
    <nav class="ma-nav">
      <div class="ma-n-con">
        <span></span>
        <ul class="nav-detail">
          <li><router-link to="/">首页</router-link></li>
          <li> <router-link to="/blog/">博客</router-link></li>
          <li>音乐</li>
          <li>视频</li>
          <li><router-link to="/ms/">我</router-link></li>
        </ul>
      </div>

    </nav>
    <div class="b-t">
        <h3 class="t-title animated  bounceInLeft delay-2s">且歌且行且从容，鲜衣怒马少年时</h3>
        <p class="p-tt animated  bounceInDown delay-2s">--且歌</p>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
$(function () {
  $(window).resize(function () {
    let wid = $(window).height();
      $('.ma-top').css('height', wid + 'px')
  })
});
  export default {
    name: "MA_TOP",
    mounted() {
      let wid = $(window).height();
      $('.ma-top').css('height', wid + 'px');
      $('.nav-detail').animate({'margin-right': '0'}, 2000);
      $(window).scroll(function () {
        let sc = $(this).scrollTop();
        if (sc > 10) {
          $('.ma-nav').css({
            'background': 'linear-gradient(to bottom,#303d4a,#3c3c3c)',
            'box-shadow': ' 5px 5px 5px rgba(0,0,0,.05)',
            'position': 'fixed',
            'top': '0',
            'z-index': '99',
          });
          $('.nav-detail li a').css({'color': '#888'})
        }
        if(sc >100){
          $('.t-title').animate({'margin-left':'0'},2000)
        }
        if (sc > 0 && sc <= 10) {
          $('.ma-nav').css({
            'background': 'none',
            'box-shadow': 'none',
            'position': 'initial',
            'top': '0'
          })
           $('.nav-detail li a').css({'color': '#fff'})
        }
      });

    }
  }
</script>

<style scoped>

  .ma-top {
    width: 100%;
    background-image: url("../../assets/5b604c13c48e5.jpg");
    background-repeat: no-repeat;
    background-size: cover;

  }

  .ma-nav {
    width: 100%;
    height: 70px;
  }

  .ma-nav .ma-n-con {
    width: 75%;
    height: 100%;
    margin: 0 auto;
    overflow: hidden;
    line-height: 70px;
  }

  .ma-nav .ma-n-con span {
    margin-top: 5px;
    display: block;
    float: left;
    padding: 20px;
    /*box-sizing: border-box;*/
    width: 20%;
    height: 100%;
    cursor: pointer;
    background: url("../../assets/logo.png.png") no-repeat;
  }

  .ma-nav .ma-n-con ul {
    float: right;
    width: 70%;
    text-align: right;
    overflow: hidden;
    margin-right: -999px;
  }

  .ma-nav .ma-n-con ul li {
    display: inline-block;
    margin: 0;
    line-height: 68px;
    text-align: center;
    padding: 0 30px;

    cursor: pointer;
    border-bottom: 3px solid crimson;
    box-sizing: border-box;
  }
   .ma-nav .ma-n-con ul  li a {
     color: white;
    font-size: 17px;
   }

  .ma-nav .ma-n-con ul li:hover {
    background: black;
  }

  .b-t{
    width: 75%;
    margin: 0 auto;
    margin-top: 70px;
    /*margin-top: 200px;*/
    padding-top: 180px;
    text-align: center;
    overflow: hidden;
  }
  .b-t h3{
    color: white;
    height: 50px;
    font-size: 45px;
    overflow: hidden;
  }
  .b-t .p-tt{
    width: 100%;
    text-align: right;
    font-size: 30px;
    color: crimson;
    padding-right: 10%;
  }
</style>
