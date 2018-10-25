<template>
  <div class="bg_content">
    <div class="content-c">
      <div class="cont-l">
        <div class="lll">
          <div class="top">
            <img src="../../assets/BLOG/content/news1.jpg" alt="">
          </div>
          <div class="detail-l">
            <p class="title">Title<span class="xian xian-l"></span></p>
            <a href="">The dollar has broken all records of positive change
              in the world and in the galaxy</a>

            <p class="ddd_de">Lorem ipsum dolor sit amet, consectetur adipiscing elit,
              sed do eiusmod tempor incididunt ut labore et dolore magna
              aliqua. Ut enim ad minim veniam, quis nostrud exercitation
              ullamco laboris nisi ut aliquip ex ea commodo consequat.
              Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>

            <div class="ddd-bot">
              <div class="ddd-l">Today 15:40</div>
              <div class="ddd-r"><span class="fa fa-eye"></span>10k</div>
            </div>

          </div>
        </div>
        <div class="lists">
          <div class="l_l_l">
            <div class="top_tt">
              <div class="top top_l">
                <img src="../../assets/BLOG/content/news2.jpg" alt="">
              </div>
              <div class="detail-l">
                <p class="title">Title<span class="xian xian-l"></span>
                  <i class="paly_ss"><span class="fa fa-play"></span>
                  </i></p>
                <p class="title_detail">The dollar has broken all records of positive change
                  in the world and in the galaxy</p>

                <div class="ddd-bot">
                  <div class="ddd-l">Today 15:40</div>
                  <div class="ddd-r"><span class="fa fa-eye"></span>10k</div>
                </div>

              </div>
            </div>

          </div>
          <div class="l_l_r">
            <div class="top_tt">
              <div class="top top_l">
                <img src="../../assets/BLOG/content/news3.jpg" alt="">
              </div>
              <div class="detail-l">
                <p class="title">Title<span class="xian xian-l"></span>
                  <i class="paly_ss"><span class="fa fa-play"></span>
                  </i></p>
                <p class="title_detail">The dollar has broken all records of positive change
                  in the world and in the galaxy</p>

                <div class="ddd-bot">
                  <div class="ddd-l">Today 15:40</div>
                  <div class="ddd-r"><span class="fa fa-eye"></span>10k</div>
                </div>

              </div>
            </div>
          </div>
        </div>

      </div>
      <div class="cont-r">
        <ul class="cont-ul">
          <li v-for="blog in blog_sixs" v-if="blog_sixs!=null">
            <div class="top_tt">
              <div class="top top_l">
                <img :src="blog.blog_image" alt="">
              </div>
              <div class="detail-l">
                <p class="title">{{blog.blog_name}}<span class="xian xian-l"></span>
                  <i class="paly_ss" @click="paly_open"  v-if="blog.blog_video_url" :data-blog_video_url="blog.blog_video_url"><span
                    class="fa fa-play"></span>
                  </i></p>
                <p class="title_detail">{{blog.blog_detail}}</p>

                <div class="ddd-bot">
                  <div class="ddd-l">{{blog.blog_date|dates}}</div>
                  <div class="ddd-r"><span class="fa fa-eye"></span>{{blog.blog_readnum}}</div>
                </div>

              </div>
            </div>
          </li>

        </ul>
      </div>
    </div>
    <div class="load_more">
      <span class="load">
        <span class="fa fa-link"><span class="iii"></span>load more</span>
      </span>
    </div>
  </div>
</template>

<script>
  import {get_six_blog} from "../../request/api";

  import $ from 'jquery'
  export default {
    name: "BG_Content",
    data() {
      return {
        vid: null,
        blog_sixs: null,
        video_id :null,
      }
    }, created() {
      get_six_blog().then(res => {
        this.blog_sixs = res.data.data
      })
    },methods:{
      paly_open(blog_video_url){
          this.video_id = blog_video_url.explicitOriginalTarget.attributes[1].nodeValue;
          console.log(this.video_id);
            if(this.video_id){
              this.$router.push({
                path:'/bv/',
                name:'blog_video',
                params:{'video_id':this.video_id}
              })
            }
      }
    }
    ,
    filters: {
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
  .prism-player {
    margin: 0 auto;
  }

  .load {
    position: relative;
  }

  .load_more {
    width: 75%;
    height: 70px;
    margin: auto;
    text-align: center;
  }

  .load_more > span {
    width: 14%;
    display: inline-block;
    height: 50px;
    background: white;
    line-height: 50px;
    text-transform: uppercase;
    cursor: pointer;
  }

  .bg_content {
    width: 100%;
    margin-top: 100px;
  }

  .content-c {
    width: 75%;
    height: 100%;
    margin: 0 auto;
    overflow: hidden;
  }

  .content-c .cont-l {
    width: 49%;
    float: left;

  }

  .title_detail {
    height: 72px;
    overflow: hidden;
    font-size: 14px;

  }

  .lll {
    width: 100%;
    background: white;
  }

  .content-c .cont-l .top {
    width: 100%;
    height: 332px;

  }

  .content-c .cont-l .top img {
    height: 100%;
    width: 100%;
  }

  .content-c .cont-r {
    width: 49%;
    float: right;
    height: 100%;
  }

  .detail-l {
    box-sizing: border-box;
    padding: 10px;
    position: relative;
  }

  .detail-l .lll a {
    display: block;
    font-size: 19px;
    margin-top: 30px;
    font-weight: 300;
    color: black;
  }

  .title {
    text-transform: uppercase;
    font-size: 20px;
    color: sandybrown;
    max-height: 25px;
    overflow: hidden;
  }

  .detail-l a {

  }

  .xian {
    width: 20px;
    height: 2px;
    background: #f9e188;
    position: absolute;
    top: 30%;
    left: 10px;
    display: block;
  }

  .ddd_de {
    margin-top: 20px;

  }

  .paly_ss .fa-play {
    color: white;
    display: block;
    font-size: 30px;
  }

  .lll .ddd-bot {
    margin-top: 100px;
    width: 100%;
    overflow: hidden;
  }

  .top_tt {
    width: 100%;
  }

  .lll .ddd-bot .ddd-l {
    width: 50%;
    float: left;
    box-sizing: border-box;
    padding: 10px;
  }

  .lll .ddd-bot .ddd-r {
    width: 50%;
    float: right;
    text-align: right;
    box-sizing: border-box;
    padding: 10px;
  }

  .lists {
    width: 100%;
    margin-top: 30px;
    overflow: hidden;
  }

  .l_l_l {
    width: 49%;
    height: 100%;
    background: white;
    float: left;

  }

  .l_l_r {
    width: 49%;
    height: 100%;
    background: white;
    float: right;
  }

  .top_l {
    height: 140px !important;
    overflow: hidden;
  }

  .top_tt :hover img {
    transform: scale(1.05);
    transition: all .5s ease-out .1s;
  }

  .top_tt {
    background: white;
    overflow: hidden;
  }

  .detail-l .ddd-bot .ddd-l {
    width: 50%;
    float: left;
    box-sizing: border-box;
    padding: 10px;
    padding-left: 0;
  }

  .paly_ss {
    cursor: pointer;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: #fff url("../../assets/play-1.png");
    display: block;
    position: absolute;
    /*background: white;*/
    right: 0;
    top: -15%;
    line-height: 55px;
    text-align: center;

  }

  .top_tt:hover .paly_ss {
    transform: translateX(-100px) translateY(-75px);
    transition: all 1s;
  }

  .top_tt:hover .fa-play {
    transform: rotate(360deg);
    transition: all 1s;
  }

  .ddd-bot .ddd-r {
    width: 50%;
    float: right;
    text-align: right;
    box-sizing: border-box;
    padding: 10px;
  }

  .cont-ul {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    height: 999px;
    padding: 0;
    margin: 0;
    list-style-type: none;
  }

  .cont-ul li {
    height: 300px;
    flex-grow: 1;
    flex-basis: 40%;
    width: 50%;
    margin: 10px;
  }

  img {
    width: 100%;
    height: 100%;
  }
</style>
