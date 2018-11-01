
import axios from './http'
import QS from 'qs'


export const get_all_blog = param => axios.get('/blog/all/',param);


export const get_all_cate = param => axios.get('/blog/cate/all/',param);

export const post_load_img = param =>axios.post('/blog/load/img/',param);

export const post_qiniu_img = param =>axios.post('/blog/qiniu/img/',param);

export const post_blog = param =>axios.post('/blog/save/',QS.stringify(param));

export const get_six_blog = param =>axios.get('/blog/six_bg/',param);

export const get_play_info = param =>axios.get('/blog/play_info/',{params:param});


export const get_play_auth = param =>axios.get('/blog/play_id/',param);

export const load_img_aliyun = param =>axios.post('/blog/save_img/',param);


export const zhan_remember = param => axios.get('/blog/zan_rem/',param);

export const month_blog = param => axios.get('/blog/month_blog/',param);

export const cate_blog_num = param => axios.get('/blog/cate_blog_num/',param);

export const mmm = param => axios.get('/blog/mmm/',param);

export  const time_sort = parma => axios.get('/blog/time_sort/',parma);

export  const re_rem = parma => axios.get('/blog/re_rem/',parma);

export  const lv_rem = parma => axios.get('/blog/lv_rem/',parma);

export  const cate_id_bg = parma => axios.get('/blog/cate_id_bg/',{params:parma});

export  const create_upload_video = parma => axios.get('/blog/create_upload_video/',{params:parma});

export  const get_id_bg = parma => axios.get('/blog/get_id_bg/',{params:parma});
