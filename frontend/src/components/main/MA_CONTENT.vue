<template>
  <div class="content">
    <div class="top">
      <div class="top-title">
        <p class="title">爱上时尚，爱尚Style <span class="xian"></span></p>
      </div>
    </div>

    <div class="user-detail">
      <p class="zhan-detail "><b>站长信息</b></p>
      <div class="user-d-con">
        <div class="user-d-l">
          <p class="user-t"><b>个人简介:</b></p>
          <div class="user-t-l">
            <p>姓名：</p>
            <p>性别：</p>
            <p>身高：</p>
            <p>体重：</p>
            <p>职业：</p>
            <p>技能：</p>
            <p>工作经验：</p>
          </div>
          <div class="user-t-r">

          </div>
          <div class="user-t-s">
            <i>别跟你的领导顶嘴，评判你说明你做的还不到位，
              先找找自己的原因再说。这点可以有些人不爱听，
              很多时候领导要的是结果，而不是过程；没有结果，
              只能说你的工作没有把过程做好。
              切忌：工作没有做好给领导摆客观原因，那样只能说你的责任心不强。</i>
          </div>
        </div>
        <div class="user-d-r">
          <p class="user-t"><b>自我描述:</b></p>
          <div>
            本人性格热情开朗，待人友好，为人诚实谦虚。工作勤奋，认真负责，
            能吃苦耐劳，尽职尽责，有耐心。具有亲和力，平易近人，善于与人沟通。
            学习刻苦认真，成绩优秀，名列前茅。品学兼优，连续三年获得学院奖学金。
            曾担任系学生会外联部干部、系团总支组织部副部长、班级生活委员等，
            在学生工作和外出拉赞助与商家联系的过程中，大大提高了自己的办事和处事能力。
            此外，还积极参加课外文体活动，各种社会实践活动和兼职工作等，
            以增加自己的阅历，提高自己的能力。在工作中体会办事方式，锻炼口才和人际交往能力。
            曾连续两年获得学院“暑期社会实践积极分子”，“学生会优秀干事”等荣誉称号。
            在平时学校生活中，做过很多兼职。例如：家教、电话访问员、酒楼服务员、派传单、问卷调查，
            还到工厂打过暑期工，亲身体会了各种工作的不同运作程序和处事方法，
            锻炼成了吃苦耐劳的精神，并从工作中体会到乐趣，尽心尽力。
            四年的大学生涯，让我的组织协调能力、管理能力、应变能力等大大提升，使我具备良好的心理素质，让
            我在竞争中拥有更大的优势，让我在人生事业中走得更高更远。获得了“优秀大学生”和“优秀毕业生”的称号。
          </div>
          <a class="btn btn-default" href="/ms/">详情</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "MA_CONTENT",
    mounted() {
      $(window).scroll(function () {
        let sc = $(this).scrollTop();
        if (sc > 200) {
          $('.title').animate({'opacity': '1', 'margin-left': '0'}, 2000)
        }
        if (sc > 400) {
          $('.user-d-l').animate({'left': '0'}, 2000);
          $('.user-d-r').animate({'right': '0'}, 2000);
          $('.zhan-detail').addClass("animated bounceInUp")
        }
      })

    }
  }
</script>

<style scoped>
  .content {
    width: 100%;
    background: #eee;

  }

  .xian {
    position: absolute;
    width: 13%;
    height: 2px;
    background: crimson;
    bottom: 20px;
    left: 0;
  }

  .btn-default {
    margin-top: 100px;
  }

  .top {
    width: 100%;
    height: 70px;
    background: #eeeeee;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, .05);
  }

  .top-title {
    width: 75%;
    height: 100%;
    margin: 0 auto;
    text-align: left;
    line-height: 70px;
    overflow: hidden;
    margin-top: 20px;
  }

  .title {
    color: black;
    width: 164px;
    font-size: 17px;
    /*padding-top: 25px;*/
    position: relative;
    cursor: pointer;
    opacity: 0;
    margin-left: -400px;

  }

  .title:hover .xian {
    width: 100%;
    transition: all 0.5s ease;
  }

  .user-detail {
    width: 100%;
    margin-top: 100px;
    height: 580px;
    overflow: hidden;
    position: relative;
    text-align: center;
  }

  .user-detail .user-d-con {
    width: 75%;
    height: 500px;
    margin: 0 auto;
    position: relative;
  }

  .user-d-l {
    box-sizing: border-box;
    padding: 10px;
    width: 49.5%;
    height: 100%;
    transform: skew(-10deg);
    position: absolute;
    margin-top: 20px;
    z-index: 4;
    left: -100%;
    top: 0;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, .06);
  }

  .user-d-r {
    margin-top: 20px;
    width: 49.5%;
    height: 100%;
    position: absolute;
    right: -200%;
    z-index: 3;
    top: 0;
    padding: 10px;
    transform: skew(-10deg);
    box-shadow: 5px 5px 5px rgba(0, 0, 0, .06);
    text-align: right;
  }

  .user-t::before {
    content: "";
    width: calc(500% + 20px);
    height: 2px;
    background: goldenrod;
    position: absolute;
    left: -10px;
    z-index: 2;
    top: -10px
  }

  .user-t {
    position: relative;
    color: black;
    height: 30px;
    font-size: 20px;
    line-height: 30px;
    width: 20%;
    text-align: center;
  }

  .user-d-l:after {
    clear: both;
    display: block;
    height: 0;
    visibility: hidden;
    content: "";

  }

  .zhan-detail {
    width: 5.5%;
    margin: 0 auto;
    font-size: 20px;
    z-index: 1;
    border-bottom: 3px solid slateblue;
  }

  .user-t-l {
    height: 49%;
    width: 49%;
    display: inline-block;
  }

  .user-t-l p {
    margin-top: 15px;
    text-align: initial;
  }

  .user-t-r {
    height: 49%;
    width: 49%;
    display: inline-block;
    box-sizing: border-box;
    border: 10px solid white;
    border-radius: 45%;
    background: url("../../assets/5b604c13c48e5.jpg");
    background-repeat: no-repeat;
    background-size: cover;
  }

  .user-t-s {
    width: 100%;
    height: 50%;
    margin-top: 10px;
    line-height: 20px;
  }
</style>
