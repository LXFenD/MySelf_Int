<template>

  <div class="nav-list">
    <div class="nav-l">
      <nav class="nav_l_s">
        <ul>
          <li>
            <!--<span class="sss"></span>-->
            <router-link to="/">首页</router-link>
          </li>
          <li>
            <!--<span  class="sss"></span>-->
            <router-link to="/blog/">博客</router-link></li>
          <li>
            <!--<span  class="sss"></span>-->
            <a href="">音乐</a></li>
          <li>
            <!--<span  class="sss"></span>-->
            <router-link to="/ms/">ME</router-link></li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
  export default {
    name: "BG_Nav_L"
  }
</script>

<style scoped>
  .nav-list {
    width: 100%;
    height: 48px;
    background: #eeeeee;
    z-index: 1;
  }

  .nav-list .nav-l {
    width: 75%;
    height: 100%;
    margin: 0 auto;
    z-index: 1;
  }

  .nav_l_s {
    width: 100%;
    height: 100%;

  }

  .nav_l_s ul {
    width: 100%;
    height: 100%;
    padding: 0;
    list-style-type: none;
  }
  .fa-search{
    color: #f9e188;
  }

  .nav_l_s ul li:first-of-type{
    margin-left: 0;
  }
  .nav_l_s ul li {
    width: 9%;
    height: 100%;
    position: relative;
    display: inline-block;
    margin-left: -2px;

  }
.nav_l_s ul li>span{
  position: absolute;
  top: 0;
  width: 100%;
  background: rgba(0,0,0,.2);
  display: none;
  /*animation: lin 4s;*/


}

.nav_l_s ul li:hover .sss {
  display: block;
  height: 100%;
    transition: height 2s;
}


  .nav_l_s ul li > a {
    display: block;
    height: 100%;
    width: 100%;
    color: #000;
    line-height: 48px;
    text-align: center;
    font-size: 16px;
  }

  .nav_l_s ul li:last-of-type {
    width: 25%;

  }
    .nav_l_s ul li:last-of-type>div{
      text-align: center;
      font-size: 16px;
      overflow: hidden;
    }
     .nav_l_s ul li:last-of-type>div:after{
       display: block;
       height: 0;
       clear: both;
     }
  .ss{
    width: 100%;
    height: 100%;
  }
</style>
