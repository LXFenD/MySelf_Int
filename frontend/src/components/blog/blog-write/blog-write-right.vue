<template>
  <div class="right-detail">
    <div class="detail-right-top">
      <input type="text" placeholder="请输入标题" ref="blog_title">
    </div>
    <div class="detail-right-top jianjie">
      <input type="text" placeholder="请输入简介" ref="blog_detail">
    </div>
    <div class="detail_i">
      <div class="im">
        <span>简介图片：</span>
        <input type="file" placeholder="请输入简介" @change="load_img_aliyun" id="blog_img" ref="blog_img">
      </div>

      <div class="show-img">
        <img src="" style="width: 100%;height: 100%;" alt="">
      </div>
    </div>
    <div class="img-url">
      <span>图片地址：</span>
      <span class="img_url_show"><a href="javascript:void (0)" target="_blank">地址</a></span>
    </div>
    <div class="detail-right-content">
      <div id="div1" class="toolbar"></div>
      <div style="padding: 5px 0; color: #ccc"></div>
      <div id="div2" class="text"></div>
    </div>
    <div class="detail-right-category">
      <div class="left-category">
          <span class="title">
              文章分类:
          </span>
        <select name="blog-wen" ref="blog_cate_id" id="blog-cate">
          <option value="1">原创</option>
          <option value="2">转载</option>
        </select>
      </div>
      <div class="right-category">
      <span class="title">
            博客分类:
      </span>
        <select name="blog-cate" id="blog-ccc" ref="blog_category_id">
          <option v-for="cate in cates" :value="cate.id">
            {{cate.cate_name}}
          </option>
        </select>
      </div>
      <div class="sub-save">
        <button class="btn btn-default" v-on:click="save_content">保存博客</button>
      </div>
    </div>
  </div>
</template>

<script>
  import E from 'wangeditor'
  import $ from 'jquery'
  import {get_all_cate} from "../../../request/api";
  import {post_load_img} from "../../../request/api";
  import {post_qiniu_img} from "../../../request/api";
  import {post_qinniu} from "../../../request/api";
  import {post_blog} from "../../../request/api";
  import {default as swal} from 'sweetalert2'
  import {load_img_aliyun} from "../../../request/api";
  // var qiniu =  require('qiniu-js');
  export default {
    name: "blog-write-left"
    , data() {
      return {
        cates: '',
        editor: null,
        img_url: ''
      }
    },

    created() {
      // //获取分类数据
      get_all_cate().then(res => {
        this.cates = res.data.data;
      })
    },
    mounted() {
      //创建富文本
      this.editor = new E('#div1', '#div2');
      this.editor.customConfig.zIndex = 10;
      this.editor.create();
    }
    , methods: {
      // 获取数据  post请求发送
      save_content: function () {
        let parms = {
          'blog_title': this.$refs.blog_title.value,
          'blog_detail': this.$refs.blog_detail.value,
          'blog_content': this.editor.txt.html(),
          'blog_text_content': this.editor.txt.text(),
          'blog_category_id': this.$refs.blog_category_id.value,
          'blog_img': this.img_url,

        };
        post_blog(parms).then(data => {
          swal("太棒了","你的博客保存了",'success')
        })
      },
      upload_img: function () {
        //上传文件到本地
        var self = this;
        let files = this.$refs.blog_img.files;
        let data = new FormData();
        data.append('file', files[0]);
        post_load_img(data).then(res => {
          self.img_url = res.data.data.img_url;
          $('.img_url_show a').attr('href', self.img_url).html(self.img_url);
          $('.show-img img').attr('src', self.img_url)
        })

      },

      upload_qiniu_img: function () {
        //上传文件到七牛云这里使用的是qiniusdk
        var files = this.$refs.blog_img.files[0];
        var data = new FormData();
        data.append('file', files);
        post_qiniu_img().then(res => {
          data.append('token', res.data.data.token);
          let key = new Date().getTime() + '.' + files.name.split('.')[1];
          let token = res.data.data.token;  //后端上传过来的token验证值
          let putExtra = {
            fname: key,//文件名
            params: {}, //自定义参数
            mimeType: ["image/png", "image/jpeg", "image/gif", 'image/jpg']//mime的上传文件的类型
          };
          let config = {
            useCdnDomain: true, //是否使用cdn加速
            region: qiniu.region.z0,
            retryCount: 6  //失败上传次数
          };
          let observable = qiniu.upload(files, key, token, putExtra, config);
          observable.subscribe({
            'next': function (next) {

            },
            'error': function (error) {
              console.log(error)
            },
            'complete': function (com) {
              this.img_url = res.data.data.url + '/' + key;
              $('.img_url_show a').attr('href', this.img_url).html(this.img_url);
              $('.show-img img').attr('src', this.img_url)
            }
          });
        })
      },
      load_img_aliyun(){
        var self = this;
        let files = this.$refs.blog_img.files;
        let data = new FormData();
        data.append('file', files[0]);
        load_img_aliyun(data).then(res => {
          self.img_url = res.data.data.img_url;
          $('.img_url_show a').attr('href', self.img_url).html(self.img_url);
          $('.show-img img').attr('src', self.img_url)
        })
      }
      ,
    },


  }
</script>

<style scoped>
  .right-detail {
    width: 100%;
    background: #fff;
    padding: 10px;
    box-sizing: border-box;
  }

  .jianjie {
    margin-top: 10px;
  }

  .detail_i {

    width: 100%;
    margin-top: 10px;
    padding: 10px;
  }

  .detail_i .im > span {
    color: black;
    font-size: 15px;
  }

  .detail_i .im > input {
    display: inline;
    color: black;
  }

  .detail_i::after {
    content: "";
    display: block;
    visibility: hidden;
    height: 0;
    clear: both;
  }

  .img-url {
    width: 100%;
    padding: 10px;
  }

  .img-url > span {
    color: black;
    font-size: 15px;
  }

  .detail_i .im {
    width: 33%;
    float: left;
  }

  .detail_i .show-img {
    width: 50%;
    height: 300px;
    float: right;
  }

  .detail-right-top {
    width: 100%;

  }

  .detail-right-top input {
    width: 100%;
    height: 40px;
    padding: 10px;
    color: #fff;
    background: #bbb;
    border-radius: 0;
    border: none;
    font-size: 16px;
  }

  .detail-right-content {
    width: 100%;
    color: #000;

  }

  .toolbar {
    border: 1px solid #ccc;
    z-index: 1;
  }

  .text {
    border: 1px solid #ccc;
    min-height: 500px;
    z-index: 2;
  }

  .detail-right-category {
    width: 100%;
    margin-top: 20px;
    color: #888;
    overflow: hidden;
  }

  .detail-right-category:after {
    content: '';
    display: block;
    visibility: hidden;
    height: 0;
    clear: both;
  }

  .left-category {
    width: 50%;
    float: left;
  }

  .title {
    font-size: 16px;
    color: black;
    padding-right: 10px;
  }

  .right-category {
    width: 50%;
    float: right;
  }

  .sub-save {
    width: 100%;

    padding-top: 30px;
    text-align: left;

  }

  .btn {
    margin-top: 20px;
    margin-left: 80px;
    color: crimson;
    border-color: #ff6357;
  }

</style>
