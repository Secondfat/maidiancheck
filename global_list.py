#coding=utf-8
#Author:Guo Xiangchen

excel_dict = {'iOS':{}, 'Android':{}}
maidian_name = []
phone_info = {}
maidian_all = []
data_is = 0
appinfo = ""
device = ""
osname = ""
excel_value = ""
#excel_dict_temp = {'login_verify_error': '登录-小说验证失败，退出登录时', 'app_login_passportid ': '登录用户passportid', 'concern_daohangcard_recommend': '导航卡片-站点点击', 'personal_mypointcenter_PV': '积分任务页-曝光', 'sign_rule_click': '任务帮助-点击量', 'sign_soudouexchange_click': '积分换搜豆-点击次数', 'personal_mypointcenter_pointshop_click': '积分商城点击', 'personal_mypointcenter_his_click': '积分明细点击', 'personal_mypointcenter_reader': '积分任务页-任务列表-开启阅读器点击量', 'personal_mypointcenter_hidingtask': '积分任务页-任务列表-挑战任务-隐藏任务点击量', 'personal_mypointcenter_search': '积分任务页-任务列表-挑战任务-发起搜索阶梯', 'personal_mypointcenter_readfeed': '积分任务页-任务列表-挑战任务-阅读头条文章阶梯', 'personal_mypointcenter_details_pv': '积分任务详情页展现量', 'personal_mypointcenter_details_click': '任务详情页-去完成点击量', 'personal_mypointcenter_openpush': '积分任务页-任务列表-开启推送', 'personal_mypointcenter_readcartoon': '积分任务页-任务列表-阅读漫画', 'personal_mypointcenter_addconcern': '积分任务页-任务列表-添加关注', 'personal_mypointcenter_addnovel': '积分任务页-任务列表-小说加书架', 'personal_mypointcenter_shareeventshow': '积分任务页-任务列表-分享任务展现', 'personal_mypointcenter_shareeventclick': '积分任务页-任务列表-分享任务点击', 'personal_mypointcenter_shareeventgo': '分享任务详情页-去完成点击', 'sign_game_click': '游戏中心点击PV', 'personal_mypointcenter_banner_click': '积分活动入口点击量', 'personal_mypointcenter_tasktips_open': '任务完成提示开关-打开', 'personal_mypointcenter_tasktips_close': '任务完成提示开关-关闭', 'personal_mypointcenter_sign_auto': '积分任务页-自动签到成功次数', 'personal_mypointcenter_giftcard_false': '签到卡片-未签到状态-点击卡片', 'personal_mypointcenter_giftcard_true': '签到卡片-已签到状态-点击卡片', 'sign_status_show_no1': '签到天数的文案提示展现-首次签到', 'sign_status_show_conti': '签到天数的文案提示展现-连续签到', 'sign_status_show_broke': '签到天数的文案提示展现-断签', 'sign_window_show': '签到弹窗展现', 'sign_window_more_click': '弹窗-去赚取更多积分-点击量', 'sign_window_close': '弹窗-关闭按钮点击', 'personal_mypointcenter_notice_show': '公告栏-展现量', 'personal_mypointcenter_notice_click': '公告栏-点击量'}