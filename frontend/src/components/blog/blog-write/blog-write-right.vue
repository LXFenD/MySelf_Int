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
    <div class="img-url">
      <span>博客视频(可不上传)：</span>
      <div class="detail-right-top">
        <input type="text" placeholder="请输入视频标题" ref="vid_title">
      </div>
      <div class="detail-right-top jianjie">
        <input type="text" placeholder="请输入视频名称" ref="vid_name">
      </div>
      <div class="detail-right-top jianjie">
        <input type="text" placeholder="请输入视频描述" ref="vid_detail">
      </div>
      <div class="detail-right-top jianjie">
        <input type="text" placeholder="请输入标签使用逗号分割" ref="vid_tags">
      </div>
      <div class="detail-right-top jianjie">
        <input type="text" placeholder="设置视频封面" ref="vid_coverurl">
      </div>
      <div class="detail-right-top jianjie">
        <input type="text" placeholder="设置视频封面" ref="vid_coverurl">
      </div>
      <div class="jianjie">
        <input type="file" placeholder="" ref="vid_file" @change="load_vid"/>
      </div>

      <div class="progress jianjie">
        <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100">
          <span class="sr-only"></span>
        </div>
      </div>
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
  import {create_upload_video} from "../../../request/api";
  // var qiniu =  require('qiniu-js');
  export default {
    name: "blog-write-left"
    , data() {
      return {
        cates: '',
        editor: null,
        img_url: '',
        vid: null
      }
    },

    created() {
      // //获取分类数据
      get_all_cate().then(res => {
        this.cates = res.data.data;
      });
      create_upload_video().then(res => {
        this.vid = res.data.data;
      })

    },
    mounted() {
      //创建富文本
      this.editor = new E('#div1', '#div2');
      this.editor.customConfig.zIndex = 10;
      this.editor.create();
    }
    , methods: {
      load_vid: function () {
        // 获取数据  post请求发送
        //
        let self = this;
        var uploader = new AliyunUpload.Vod({
          //分片大小默认1M，不能小于100K
          partSize: 1048576,
          //并行上传分片个数，默认5
          parallel: 5,
          //网络原因失败时，重新上传次数，默认为3
          retryCount: 3,
          //网络原因失败时，重新上传间隔时间，默认为2秒
          retryDuration: 2,
          // 开始上传
          'onUploadstarted': function (uploadInfo) {
            console.log("onUploadStarted:" + uploadInfo.file.name + ", endpoint:" + uploadInfo.endpoint + ", bucket:" + uploadInfo.bucket + ", object:" + uploadInfo.object);
            //上传方式1, 需要根据uploadInfo.videoId是否有值，调用点播的不同接口获取uploadauth和uploadAddress，如果videoId有值，调用刷新视频上传凭证接口，否则调用创建视频上传凭证接口
            uploader.setUploadAuthAndAddress(uploadInfo, self.vid.UploadAuth, self.vid.UploadAddress, self.vid.VideoId);
            //上传方式2
            // uploader.setSTSToken(uploadInfo, accessKeyId, accessKeySecret,secretToken);
            $('.progress').css('display', "block");
          },
          // 文件上传成功
          'onUploadSucceed': function (uploadInfo) {
            console.log("onUploadSucceed: " + uploadInfo.file.name + ", endpoint:" + uploadInfo.endpoint + ", bucket:" + uploadInfo.bucket + ", object:" + uploadInfo.object);
          },
          // 文件上传失败
          'onUploadFailed': function (uploadInfo, code, message) {
            console.log("onUploadFailed: file:" + uploadInfo.file.name + ",code:" + code + ", message:" + message);
          },
          // 文件上传进度，单位：字节
          'onUploadProgress': function (uploadInfo, totalSize, loadedPercent) {
            console.log("onUploadProgress:file:" + uploadInfo.file.name + ", fileSize:" + totalSize + ", percent:" + Math.ceil(loadedPercent * 100) + "%");

            $('.progress-bar').css({'width': Math.ceil(loadedPercent * 100) + "%"})
            $('.sr-only').text(Math.ceil(loadedPercent * 100) + "%")
          },
          // 上传凭证超时
          'onUploadTokenExpired': function (uploadInfo) {
            console.log("onUploadTokenExpired");
            //上传方式1  实现时，根据uploadInfo.videoId调用刷新视频上传凭证接口重新获取UploadAuth
            uploader.resumeUploadWithAuth(uploadAuth);
            // 上传方式2 实现时，从新获取STS临时账号用于恢复上传
            // uploader.resumeUploadWithSTSToken(accessKeyId, accessKeySecret, secretToken, expireTime);
          },
          //全部文件上传结束
          'onUploadEnd': function (uploadInfo) {
            console.log("onUploadEnd: uploaded all the files");
            $('.progress').css('display', "none");
            swal("太棒了", "你的视频上传成功！！", 'success')
          }
        });
        var userData = '{"Vod":{"UserData":{"IsShowWaterMark":"false","Priority":"7"}}}';
        uploader.addFile(self.$refs.vid_file.files[0], null, null, null, userData);
        uploader.startUpload();
      }
      ,
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
          swal("太棒了", "你的博客保存了", 'success')
        })
      }
      ,
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

      }
      ,

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
      }
      ,
      load_img_aliyun() {
        var self = this;
        let files = this.$refs.blog_img.files;
        let data = new FormData();
        data.append('file', files[0]);
        load_img_aliyun(data).then(res => {
          self.img_url = res.data.data.img_url;
          $('.img_url_show a').attr('href', self.img_url).html(self.img_url);
          $('.show-img img').attr('src', self.img_url);
          swal("太棒了", "你的图片上传成功！！", 'success')
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

  .sr-only {
    color: black;
  }

  .progress {
    margin-top: 10px;
    display: none;
  }
</style>
