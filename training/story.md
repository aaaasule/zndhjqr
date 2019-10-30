## Generated Story taskts_1
* task_require_1
    - utter_task_id_1
    - utter_input_number
* task_require_id{"task_idcard":"110227199601173810"}
    - action_check_tel
* confirm
    - utter_task_id_3
* task_require_3
    - utter_task_id_4
* task_require_4
    - utter_task_id_5
    - utter_ask_morehelp
    - action_restart

## Generated Story taskts_2
* task_require_1
    - utter_task_id_1
* task_require_5
    - utter_task_id_6
    - utter_input_number
* task_require_id{"task_idcard":"110227199601173810"}
    - action_check_tel
* confirm
    - utter_task_id_3
    - utter_ask_morehelp
    - action_restart


## Generated Story taskts_3
* task_require_1
    - utter_task_id_1
    - utter_input_number
* task_require_id{"task_idcard":"110227199601173811"}
    - action_check_tel
* deny OR not_is
    - utter_task_id_8
    - utter_input_number
* task_require_id{"task_idcard":"110227199601173812"}
    - action_check_tel
    - utter_task_topeople
    - utter_ask_morehelp
    - action_restart

## Generated Story taskts_4
* task_require_1
    - utter_task_id_1
* task_require_5
    - utter_task_id_6
    - utter_input_number
* task_require_id{"task_idcard":"110227199601173811"}
    - action_check_tel
* deny OR not_is
    - utter_task_id_8
    - utter_input_number
* task_require_id{"task_idcard":"110227199601173812"}
    - action_check_tel
    - utter_task_topeople
    - action_restart


## Generated Story taskts_5
* task_require_1
    - utter_task_id_1
    - utter_input_number
* task_require_id{"task_idcard":"110227199601173811"}
    - action_check_tel
* deny OR not_is
    - utter_task_id_8
    - utter_input_number
* task_require_id{"task_idcard":"110227199601173810"}
    - action_check_tel
* confirm
    - utter_task_id_3
    - utter_ask_morehelp
    - action_restart


## Generated Story taskts_6
* task_check_weather_1
    - utter_ask_weather
* task_check_weather_2{"task_check_city":"北京"}
    - action_check_weather
    - utter_ask_morehelp
    - action_restart

## Generated Story taskts_7
* task_check_weather_1
    - utter_ask_weather
* task_check_weather_2{"task_check_city":"天津"}
    - action_check_weather
    - utter_ask_morehelp
    - action_restart
    
 ## Generated Story taskts_8
* task_check_weather_1
    - utter_ask_weather
* task_check_weather_2{"task_check_city":"石家庄"}
    - action_check_weather
    - utter_ask_morehelp
    - action_restart
    
 ## Generated Story taskts_9
* task_check_weather_1
    - utter_ask_weather
* task_check_weather_2{"task_check_city":"武汉"}
    - action_check_weather
    - utter_ask_morehelp
    - action_restart

 ## Generated Story taskts_10
* task_check_weather_1
    - utter_ask_weather
* task_check_weather_2{"task_check_city":"太原"}
    - action_check_weather
    - utter_ask_morehelp
    - action_restart

## Generated Story taskts_11
* request_search{"task_item":"消费"}
    - utter_ask_time
* inform_time{"task_time":"一月的"}
    - utter_wait
    - utter_reply
* thanks
    - utter_thanks
    - utter_ask_morehelp
    - action_restart
    

    
## Generated Story baoxiu_taskts_1
* task_require_TV
    - utter_task_id_10
* task_require_signal
    - utter_task_id_7
* task_require_useless
    - utter_task_id_11 
    - utter_input_number
* task_fillin_tel{"fillin_tel":"15166515951"}
    - action_fillin_tel
* confirm
    - utter_end
    - utter_ask_morehelp
    - action_restart

## Generated Story baoxiu_taskts_2
* task_require_TV
    - utter_task_id_10
* task_require_signal
    - utter_task_id_7
* goodbye
    - utter_goodbye
    - utter_ask_morehelp
    - action_restart

## Generated Story baoxiu_taskts_3
* task_require_TV
    - utter_task_id_10
* task_require_signal
    - utter_task_id_7
* task_require_useless
    - utter_task_id_11
    - utter_input_number 
* task_fillin_tel{"fillin_tel":"15166516666"}
    - action_fillin_tel
* deny OR not_is
    - utter_re_input
* task_fillin_tel{"fillin_tel":"15166515951"}
    - action_fillin_tel
* confirm
    - utter_end
    - utter_ask_morehelp
    - action_restart

## Generated Story baoxiu_taskts_4
* task_require_TV
    - utter_task_id_10
* task_require_signal
    - utter_task_id_7
* task_require_useless
    - utter_task_id_11
    - utter_input_number 
* task_fillin_tel{"fillin_tel":"15166516666"}
    - action_fillin_tel
* deny OR not_is
    - utter_re_input
* task_fillin_tel{"fillin_tel":"15166517777"}
    - action_fillin_tel
* deny OR not_is
    - utter_no_answer
    - utter_task_topeople
    - action_restart

## Generated Story baoxiu_taskts_5
* task_require_TV
    - utter_task_id_10
* task_require_signal
    - utter_task_id_7
* task_require_useless
    - utter_task_id_11
    - utter_input_number 
* task_fillin_tel{"fillin_tel":"15166518888"}
    - action_fillin_tel
* task_fillin_tel{"fillin_tel":"15166515951"}
    - action_fillin_tel
* confirm
    - utter_end
    - utter_ask_morehelp
    - action_restart


## Generated Story baoxiu_taskts_6
* task_require_TV
    - utter_task_id_10
* task_require_signal
    - utter_task_id_7
* task_require_useless
    - utter_task_id_11 
    - utter_input_number
* task_fillin_tel{"fillin_tel":"15166518888"}
    - action_fillin_tel
* task_fillin_tel{"fillin_tel":"15166517777"}
    - action_fillin_tel
* deny OR not_is
    - utter_no_answer
    - utter_task_topeople
    - action_restart

## Generated Story baoxiu_taskts_7
* task_require_signal
    - utter_task_id_7
* task_require_useless
    - utter_task_id_11 
    - utter_input_number
* task_fillin_tel{"fillin_tel":"15166515951"}
    - action_fillin_tel
* confirm
    - utter_end
    - utter_ask_morehelp
    - action_restart
    
## Generated Story baoxiu_taskts_8
* task_require_signal
    - utter_task_id_7
* goodbye
    - utter_goodbye
    - utter_ask_morehelp
    - action_restart  

## Generated Story baoxiu_taskts_9
* task_require_signal
    - utter_task_id_7
* task_require_useless
    - utter_task_id_11 
    - utter_input_number
* task_fillin_tel{"fillin_tel":"15166516666"}
    - action_fillin_tel
* deny OR not_is
    - utter_re_input
* task_fillin_tel{"fillin_tel":"15166515951"}
    - action_fillin_tel
* confirm
    - utter_end
    - utter_ask_morehelp
    - action_restart
    
## Generated Story baoxiu_taskts_10
* task_require_signal
    - utter_task_id_7
* task_require_useless
    - utter_task_id_11 
    - utter_input_number
* task_fillin_tel{"fillin_tel":"15166516666"}
    - action_fillin_tel
* deny OR not_is
    - utter_re_input
* task_fillin_tel{"fillin_tel":"15166517777"}
    - action_fillin_tel
* deny OR not_is
    - utter_no_answer
    - utter_task_topeople
    - action_restart

## Generated Story baoxiu_taskts_11
* task_require_signal
    - utter_task_id_7
* task_require_useless
    - utter_task_id_11 
    - utter_input_number
* task_fillin_tel{"fillin_tel":"15166518888"}
    - action_fillin_tel
* task_fillin_tel{"fillin_tel":"15166515951"}
    - action_fillin_tel
* confirm
    - utter_end
    - utter_ask_morehelp
    - action_restart
    
## Generated Story baoxiu_taskts_12
* task_require_signal
    - utter_task_id_7
* task_require_useless
    - utter_task_id_11
    - utter_input_number
* task_fillin_tel{"fillin_tel":"15166518888"}
    - action_fillin_tel
* task_fillin_tel{"fillin_tel":"15166517777"}
    - action_fillin_tel
* deny OR not_is
    - utter_no_answer
    - utter_task_topeople
    - action_restart

## Generated Story baoxiu_yanshi
* task_baoxiu_kouling
    - utter_task_baoxiu_kouling    
* task_require_TV    
    - utter_task_baoxiu1
* task_baoxiu1
    - utter_task_baoxiu2
* task_require_useless
    - utter_task_baoxiu3
* task_baoxiu2
    - utter_task_id_11
    - utter_input_number
* task_fillin_tel{"fillin_tel":"15166515951"}
    - action_fillin_tel
* confirm
    - utter_end
    - utter_ask_morehelp
    - action_restart


## Generated Story kuandai_guzhang_hao_lianxi_manyi_yuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_hao
    - utter_kuandai_huifang2
* task_kuandai_lianxi
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* task_kuandai_yuding
    - utter_kuandai_jieshu_confirm
    - action_restart
    
## Generated Story kuandai_guzhang_hao_lianxi_manyi_buyuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_hao
    - utter_kuandai_huifang2
* task_kuandai_lianxi
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* deny
    - utter_kuandai_jieshu_not_satisfied
    - action_restart
    
## Generated Story kuandai_guzhang_hao_lianxi_bumanyi
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_hao
    - utter_kuandai_huifang2
* task_kuandai_lianxi
    - utter_kuandai_huifang3
* task_kuandai_bumanyi
    - utter_kuandai_jieshu_not_satisfied
    - action_restart
    
## Generated Story kuandai_guzhang_hao_shi_manyi_yuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_hao
    - utter_kuandai_huifang2
* confirm
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* task_kuandai_yuding
    - utter_kuandai_jieshu_confirm
    - action_restart

## Generated Story kuandai_guzhang_hao_shi_manyi_buyuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_hao
    - utter_kuandai_huifang2
* confirm
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* deny
    - utter_kuandai_jieshu_not_satisfied
    - action_restart    
    
## Generated Story kuandai_guzhang_hao_shi_bumanyi
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_hao
    - utter_kuandai_huifang2
* confirm
    - utter_kuandai_huifang3
* task_kuandai_bumanyi
    - utter_kuandai_jieshu_not_satisfied 
    - action_restart


## Generated Story kuandai_guzhang_hao_meilianxi
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_hao
    - utter_kuandai_huifang2
* task_kuandai_meilianxi 
    - utter_kuandai_jieshu_not_satisfied  
    - action_restart  
    
    
## Generated Story kuandai_guzhang_hao_bushi
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_hao
    - utter_kuandai_huifang2
* not_is
    - utter_kuandai_jieshu_not_satisfied  
    - action_restart  
    
    
## Generated Story kuandai_guzhang_hao_buzhidao
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_hao
    - utter_kuandai_huifang2
* do_not_know
    - utter_kuandai_jieshu_not_satisfied   
    - action_restart

## Generated Story kuandai_guzhang_buzhidao_lianxi_manyi_yuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* do_not_know
    - utter_kuandai_huifang2
* task_kuandai_lianxi
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* task_kuandai_yuding
    - utter_kuandai_jieshu_confirm
    - action_restart
    
## Generated Story kuandai_guzhang_buzhidao_lianxi_manyi_buyuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* do_not_know
    - utter_kuandai_huifang2
* task_kuandai_lianxi
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* deny
    - utter_kuandai_jieshu_not_satisfied
    - action_restart
    
## Generated Story kuandai_guzhang_buzhidao_lianxi_bumanyi
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* do_not_know
    - utter_kuandai_huifang2
* task_kuandai_lianxi
    - utter_kuandai_huifang3
* task_kuandai_bumanyi
    - utter_kuandai_jieshu_not_satisfied
    - action_restart
    
## Generated Story kuandai_guzhang_buzhidao_shi_manyi_yuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* do_not_know
    - utter_kuandai_huifang2
* confirm
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* task_kuandai_yuding
    - utter_kuandai_jieshu_confirm
    - action_restart
    
## Generated Story kuandai_guzhang_buzhidao_shi_manyi_buyuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* do_not_know
    - utter_kuandai_huifang2
* confirm
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* deny
    - utter_kuandai_jieshu_not_satisfied
    - action_restart
    
## Generated Story kuandai_guzhang_buzhidao_shi_bumanyi
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* do_not_know
    - utter_kuandai_huifang2
* confirm
    - utter_kuandai_huifang3
* task_kuandai_bumanyi
    - utter_kuandai_jieshu_not_satisfied
    - action_restart
    
## Generated Story kuandai_guzhang_buzhidao_meilianxi
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* do_not_know
    - utter_kuandai_huifang2
* task_kuandai_meilianxi
    - utter_kuandai_jieshu_not_satisfied    
    - action_restart  
    
    
## Generated Story kuandai_guzhang_buzhidao_not_is
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* do_not_know
    - utter_kuandai_huifang2
* not_is
    - utter_kuandai_jieshu_not_satisfied  
    - action_restart  
    
## Generated Story kuandai_guzhang_buzhidao_buzhidao
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* do_not_know
    - utter_kuandai_huifang2
* do_not_know
    - utter_kuandai_jieshu_not_satisfied  
    - action_restart


## Generated Story kuandai_guzhang_buzaijia_lianxi_manyi_yuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_buzaijia
    - utter_kuandai_huifang2
* task_kuandai_lianxi
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* task_kuandai_yuding
    - utter_kuandai_jieshu_confirm
    - action_restart
    
## Generated Story kuandai_guzhang_buzaijia_lianxi_manyi_buyuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_buzaijia
    - utter_kuandai_huifang2
* task_kuandai_lianxi
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* deny
    - utter_kuandai_jieshu_not_satisfied
    - action_restart
    
## Generated Story kuandai_guzhang_buzaijia_lianxi_bumanyi
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_buzaijia
    - utter_kuandai_huifang2
* task_kuandai_lianxi
    - utter_kuandai_huifang3
* task_kuandai_bumanyi
    - utter_kuandai_jieshu_not_satisfied
    - action_restart
    
## Generated Story kuandai_guzhang_buzaijia_shi_manyi_yuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_buzaijia
    - utter_kuandai_huifang2
* confirm
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* task_kuandai_yuding
    - utter_kuandai_jieshu_confirm
    - action_restart
    
## Generated Story kuandai_guzhang_buzaijia_shi_manyi_buyuding
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_buzaijia
    - utter_kuandai_huifang2
* confirm
    - utter_kuandai_huifang3
* task_kuandai_manyi OR confirm
    - utter_kuandai_huifang
* deny
    - utter_kuandai_jieshu_not_satisfied
    - action_restart


## Generated Story kuandai_guzhang_buzaijia_shi_bumanyi
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_buzaijia
    - utter_kuandai_huifang2
* confirm
    - utter_kuandai_huifang3
* task_kuandai_bumanyi
    - utter_kuandai_jieshu_not_satisfied
    - action_restart


## Generated Story kuandai_guzhang_buzaijia_meilianxi
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_buzaijia
    - utter_kuandai_huifang2
* task_kuandai_meilianxi
    - utter_kuandai_jieshu_not_satisfied
    - action_restart
    

## Generated Story kuandai_guzhang_buzaijia_not_is
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_buzaijia
    - utter_kuandai_huifang2
* not_is
    - utter_kuandai_jieshu_not_satisfied  
    - action_restart  
    
    
## Generated Story kuandai_guzhang_buzaijia_buzhidao
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_buzaijia
    - utter_kuandai_huifang2
* do_not_know
    - utter_kuandai_jieshu_not_satisfied
    - action_restart



## Generated Story kuandai_guzhang_buhao
* task_kouling_huifang
    - utter_kuandai_huifang_huanying
* task_kuandai_buhao
    - utter_kuandai_jieshu_not_satisfied
    - action_restart
    

## Generated Story sifayuanzhu_kouling
* task_kouling_sifayuanzhu
    - utter_sifayuanzhu
    - action_restart

## Generated Story sifayuanzhu1
* task_sifayuanzhu1
    - utter_task_sifayuanzhu1
    - utter_ask_morehelp
    - action_restart

## Generated Story sifayuanzhu2
* task_sifayuanzhu2
    - utter_task_sifayuanzhu2
    - utter_ask_morehelp
    - action_restart

## Generated Story sifayuanzhu3
* task_sifayuanzhu3
    - utter_task_sifayuanzhu3
    - utter_ask_morehelp
    - action_restart

## Generated Story sifayuanzhu4
* task_sifayuanzhu4
    - utter_task_sifayuanzhu4
    - utter_ask_morehelp
    - action_restart
    
## Generated Story jiehaizi
* task_kouling_zhiyuanzhe
    - utter_task_zhiyuanzhe
* task_jiehaizi
    - utter_task_jiehaizi
    - utter_task_jiehaizi1
* task_jiehaizi1
    - utter_task_jiehaizi2
* task_jiehaizi2
    - utter_task_jiehaizi3
* task_jiehaizi3
    - utter_task_jiehaizi4
* task_jiehaizi4
    - utter_task_jiehaizi5
    - action_restart
    
    
## Generated Story jiayou
* task_kouling_zhiyuanzhe
    - utter_task_zhiyuanzhe
* task_jiayou1
    - utter_task_jiayou1
* task_jiayou2
    - utter_task_jiayou2
* task_jiayou3
    - utter_task_jiayou3
* task_jiayou4
    - utter_task_jiayou4
    - action_restart
    
## Generated Story handan_huru  
* task_handan_kouling
    - utter_handan_huru
    - action_restart

## Generated Story usual_task_1
* greet
    - utter_greet
    - action_restart


## Generated Story usual_task_2
* goodbye
    - utter_goodbye
    - action_restart
 
## Generated Story usual_task_3
* confirm
    - utter_greet
    - action_restart
    
## Generated Story usual_task_4
* deny
    - utter_greet
    - action_restart
    
## Generated Story usual_task_5
* unknown_intent
    - utter_greet
    - action_restart
