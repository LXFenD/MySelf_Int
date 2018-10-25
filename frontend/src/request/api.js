
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
