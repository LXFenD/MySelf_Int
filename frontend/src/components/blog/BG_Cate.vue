<template>
  <div class="bg_cate">
    <div class="bg-cate-s">
      <div class="bg-cate-l">
        <p class="title"><span class="glyphicon glyphicon-list"></span>博客分类</p>
        <ul class="bg_cate_lists">
          <li>
            <span class="glyphicon glyphicon-time"></span>
            <span class="cate-li">时间分类</span>
            <span class="fa fa-arrow-right"></span>
          </li>
          <li><span class="glyphicon glyphicon-book"></span>
            <span class="cate-li">博客类型</span>
            <span class="fa fa-arrow-right"></span></li>
          <li><span class="glyphicon glyphicon-eye-open"></span>
            <span class="cate-li">观看最多</span>
            <span class="fa fa-arrow-right"></span>
          </li>
          <li><span class="glyphicon glyphicon-thumbs-up"></span>
            <span class="cate-li">喜欢最多</span>
            <span class="fa fa-arrow-right"></span>
          </li>
        </ul>
      </div>

      <div class="bg-cate-conts">
        <div class="bg-cate-conts-top">
          <span class="glyphicon glyphicon-remove"></span>
        </div>
        <div class="bg-cate-conts-cont">
          <div class="cont-top">
            <h4><span class="glyphicon glyphicon-triangle-right"></span>时间分类</h4>
            <ul class="cate-fen">
              <li v-if="times!=null" v-for="t in times">
                <span>{{t[0]}}年{{t[1]}}月</span><span>({{t[2]}})篇</span>
              </li>
            </ul>
            <h4><span class="glyphicon glyphicon-triangle-right"></span>时间热度文章</h4>
            <ul class="cate-re">
              <li v-for="sort in time_sorts" @click="link_sub(sort.id,sort.blog_video_url)">
                <img :src="sort.blog_image" alt="">
                <div class="cate-po">
                  <p>分类：<i><span class="categoty-fen">{{sort.blog_cate.cate_name}}</span></i></p>
                  <p>标题：<span class="categoty-title">{{sort.blog_name}}</span></p>
                  <p>简介：<span class="categoty-detail">{{sort.blog_detail}}</span></p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="bg-cate-conts">
        <div class="bg-cate-conts-top">
          <span class="glyphicon glyphicon-remove"></span>
        </div>
        <div class="bg-cate-conts-cont">
          <div class="cont-top">
            <h4><span class="glyphicon glyphicon-triangle-right"></span>类型分类</h4>
            <ul class="cate-fen">
              <li v-if="cates!=null" v-for="cate in cates">
                <span>{{cate.cate_name}}</span>
                <span>({{cate.num}})篇</span>
              </li>
            </ul>
            <h4><span class="glyphicon glyphicon-triangle-right"></span>时间热度文章</h4>
            <ul class="cate-re">
              <li v-for="sort in time_sorts" @click="link_sub(sort.id,sort.blog_video_url)">
                <img :src="sort.blog_image" alt="">
                <div class="cate-po">
                  <p>分类：<i><span class="categoty-fen">{{sort.blog_cate.cate_name}}</span></i></p>
                  <p>标题：<span class="categoty-title">{{sort.blog_name}}</span></p>
                  <p>简介：<span class="categoty-detail">{{sort.blog_detail}}</span></p>
                </div>
              </li>

            </ul>
          </div>
        </div>
      </div>
      <div class="bg-cate-conts">
        <div class="bg-cate-conts-top">
          <span class="glyphicon glyphicon-remove"></span>
        </div>
        <div class="bg-cate-conts-cont">
          <div class="cont-top">
            <h4><span class="glyphicon glyphicon-triangle-right"></span>观看最多</h4>
            <ul class="cate-fen">
              <li v-for="re in re_rems" v-if="re_rems!=null" >

                <span class="blog_name">{{re.blog_name}}</span>
                <span class="glyphicon glyphicon-eye-open">({{re.blog_zan}})</span>
              </li>

            </ul>
            <h4><span class="glyphicon glyphicon-triangle-right"></span>时间热度文章</h4>
            <ul class="cate-re">
              <li v-for="re in re_rems" v-if="re_rems!=null" @click="link_sub(re.id,re.blog_video_url)">
                <img :src="re.blog_image" alt="">
                <div class="cate-po">
                  <p>分类：<i><span class="categoty-fen">{{re.blog_cate.cate_name}}</span></i></p>
                  <p>标题：<span class="categoty-title">{{re.blog_name}}</span></p>
                  <p>简介：<span class="categoty-detail">{{re.blog_detail}}</span></p>
                </div>
              </li>

            </ul>
          </div>
        </div>
      </div>
      <div class="bg-cate-conts">
        <div class="bg-cate-conts-top">
          <span class="glyphicon glyphicon-remove"></span>
        </div>
        <div class="bg-cate-conts-cont">
          <div class="cont-top">
            <h4><span class="glyphicon glyphicon-triangle-right"></span>喜欢最多</h4>
            <ul class="cate-fen">
              <li v-for="lv in lv_rems" v-if="lv_rems!=null" >
                <span class="blog_name">{{lv.blog_name}}</span>
                <span class="glyphicon glyphicon-thumbs-up">({{lv.blog_zan}})</span>
              </li>
            </ul>
            <h4><span class="glyphicon glyphicon-triangle-right"></span>排行</h4>
            <ul class="cate-re">
              <li  v-for="lv in lv_rems" v-if="lv_rems!=null" @click="link_sub(lv.id,lv.blog_video_url)">
                <img :src="lv.blog_image" alt="">
                <div class="cate-po">
                  <p>分类：<i><span class="categoty-fen">{{lv.blog_cate.cate_name}}</span></i></p>
                  <p>标题：<span class="categoty-title">{{lv.blog_name}}</span></p>
                  <p>简介：<span class="categoty-detail">{{lv.blog_detail}}</span></p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import $ from 'jquery'
  import {month_blog} from "../../request/api";
  import {cate_blog_num} from "../../request/api";
  import {mmm} from "../../request/api";
  import {time_sort} from "../../request/api";
  import {re_rem} from "../../request/api";
  import {lv_rem} from "../../request/api";

  export default {
    name: "BG_Cate",
    data() {
      return {
        cates: null,
        times: null,
        time_sorts: null,
        re_rems: null,
        lv_rems: null,
      }
    },
    created() {
      mmm().then(res => {
        this.times = res.data.data
      });
      cate_blog_num().then(res => {
        this.cates = res.data.data;
      });
      time_sort().then(res => {
        this.time_sorts = res.data.data
      });
      re_rem().then(res => {
        this.re_rems = res.data.data
      });
      lv_rem().then(res => {
        this.lv_rems = res.data.data
      });
    },
    mounted() {
      $('.bg_cate_lists li').click(function () {
        let conts = $('.bg-cate-conts');
        conts.hide();
        conts.eq($(this).index()).show()
      });
      $('.bg_cate').hover(function () {
        $('.bg-cate-l').animate({'width': '150px'}, 1000)
      }, function () {
        $('.bg-cate-conts').hide();
        $('.bg-cate-l').animate({'width': '40px'}, 1000);
      });
      $('.glyphicon-remove').click(function () {
        $('.bg-cate-conts').hide();
      })

    },
     methods:{
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
  }
</script>

<style scoped>
  .title {
    text-align: left;
    width: 100%;
    height: 40px;
    line-height: 40px;
    color: white;
    font-size: 16px;
    border-left: 3px crimson solid;
    overflow: hidden;
  }

  .bg-cate-l {
    width: 40px;
  }

  .bg-cate-s {
    height: 100%;
    float: right;
  }

  .blog_name{
    width: 70%;
    overflow: hidden;
    
  }
  .title span {
    color: white;
    padding: 0 10px;
  }

  .bg_cate {
    position: fixed;
    left: 0;
    top: 9%;
    height: 100%;
    background: linear-gradient(to bottom, #000, #3c3c3c);
    z-index: 88;
    box-sizing: border-box;
    border-top: 1px solid #fff;
    text-align: center;
    cursor: pointer;
  }

  .bg-cate-l {
    float: left;
  }

  .bg_cate_lists {
    width: 100%;
    padding: 0;
    margin: 0;
  }

  .bg_cate_lists > li {
    width: 100%;
    color: white;
    overflow: hidden;
    height: 40px;
    line-height: 40px;
    border-bottom: 1px solid #fff;

  }

  .bg_cate_lists > li span {
    color: white;

  }

  .cate-li {
    margin-left: 15px;
  }

  .bg_cate_lists > li:hover {
    background: linear-gradient(#2c2c2c, #444);
    transition: all .7s ease;
  }

  .bg_cate_lists > li:hover .bg-cate-conts {
    display: block;
  }

  .bg-cate-conts {
    float: right;
    width: 500px;
    display: none;
    height: 100%;
    overflow: hidden;
    background: #eeeeee;
  }

  .bg-cate-conts-top {
    width: 100%;
    height: 40px;
    text-align: right;
    box-sizing: border-box;
    line-height: 40px;
    overflow: hidden;
  }

  .bg-cate-conts-top span {
    color: #888;
    font-size: 18px;
    padding: 10px;
  }

  .bg-cate-conts-cont {
    width: 100%;
  }

  .bg-cate-conts-cont .cont-top {
    width: 100%;
    box-sizing: border-box;
    padding: 10px 20px;
    text-align: left;

  }

  .bg-cate-conts-cont .cont-top h4 {
    border-left: 5px solid crimson;
    padding-left: 10px;
  }

  .cate-fen {
    width: 100%;
    padding: 0;
    margin: 0;
    display: flex;
    flex-wrap: wrap;
  }

  .cate-fen li {
    flex-grow: 1;
    flex-basis: 50%;
    height: 20px;
    overflow: hidden;
    text-align: center;
  }

  .cate-re {
    width: 100%;
    padding: 0;
    margin: 0;
    display: flex;
    flex-wrap: wrap;
  }

  .cate-re li {
    flex-grow: 1;
    flex-basis: 45%;
    margin: 10px;
    background: crimson;
    height: 150px;
    overflow: hidden;
    position: relative;
  }

  .cate-re li img {
    width: 100%;
    height: 100%;

  }

  .cate-po {
    position: absolute;
    width: 100%;
    height: 50%;
    background: rgba(0, 0, 0, .5);
    left: 0;
    bottom: 0;
  }

  .cate-po p {
    font-size: 14px;
    color: white;
    height: 16px;
    line-height: 16px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
  }

  .cate-po span {
    font-size: 14px;
    color: white;
  }

  .categoty-fen {
    text-transform: uppercase;
    color: goldenrod !important;
  }
</style>
