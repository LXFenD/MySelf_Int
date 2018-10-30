<template>
    <div class="bg-pbl">
      <div class="bg-p-m">
        <div class="bg-top-p">
          <p class="p-title"> <span class="fa fa-book"></span><span class="xian xian-l"></span>全部文章</p>
          <ul>
            <li @click="get_blogs(0)">全部</li>
            <li v-for=" cate in cates" v-if="cates!=null" @click="get_blogs(cate.id)">
              {{cate.cate_name}}
            </li>
          </ul>
        </div>
        <div class="bg-p-m-p">
          <div class="pic" v-for="blog in blogs" v-if="blogs!=null">
            <img :src="blog.blog_image" alt="">
            <p>
              {{blog.blog_detail}}
            </p>
          </div>

        </div>
      </div>
    </div>
</template>

<script>
  import {get_all_blog} from "../../request/api";
  import {get_all_cate} from "../../request/api";
  import {cate_id_bg} from "../../request/api";

  export default {
        name: "BG_Pbl",
      data(){
          return{
            blogs:null,
            cates:null,
          }
      },
      created(){
          get_all_blog().then(res=>{
            this.blogs = res.data.data
          });
          get_all_cate().then(res=>{
            this.cates = res.data.data
          })
      },
    methods:{
          get_blogs(id){
            cate_id_bg({'cate_id':id}).then(res=>{
              this.blogs = res.data.data
            })
          }
    }
    }
</script>

<style scoped>
  .xian {
    width: 20px;
    height: 2px;
    background: #f9e188;
    position: absolute;
    bottom: -3px;
    left: 0;
    display: block;
  }
  .fa-book{
    padding: 3px;
  }
    .bg-pbl{
      width: 100%;
    }
  .bg-p-m{
    width: 75%;
    margin: 40px auto;

  }
  .bg-p-m .bg-top-p {
    width: 100%;
    border-left: 5px solid crimson;
    margin: 0;
    overflow: hidden;
    padding-left: 10px;
    background: white;
    box-shadow: 5px 5px 5px rgba(0,0,0,.06);
  }
  .bg-p-m .bg-top-p p{
    width: 30%;
    line-height: 40px;
    float: left;
    position: relative;
  }
  .bg-p-m .bg-top-p ul{
    float: right;
    overflow: hidden;
    padding: 0;
    margin: 0;
  }
  .bg-p-m .bg-top-p ul li{
    display: inline-block;
    line-height: 40px;
    padding-right: 20px;
    cursor: pointer;
  }
  .bg-p-m .bg-p-m-p{
    width: 100%;
    margin-top: 20px;
    display: flex;
    flex-wrap: wrap;

  }
  .bg-p-m .bg-p-m-p .pic{
    flex-basis: 30%;
    box-sizing: border-box;
    flex-grow: 1;
    margin: 10px;
    width: 30%;
    background: white;
    padding: 20px;
    box-shadow:  0 0 5px rgba(0,0,0,.5);
    margin-bottom: 20px;

  }
   .bg-p-m .bg-p-m-p .pic img{
     width: 100%;
   }

.bg-p-m .bg-p-m-p .pic p{
  margin-top: 10px;
  cursor: pointer;
}


</style>
