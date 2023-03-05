# external
donate_page = 'https://afdian.net/@mengzonefire'
issue_page = 'https://github.com/mengzonefire/twitter-media-downloader/issues'
release_page = 'https://github.com/mengzonefire/twitter-media-downloader/releases'
cookie_tips_page = 'https://git.io/how_to_get_cookies_cn'

# warning text
log_warning = '\r运行错误: log文件已保存到 {}\n'
user_warning = '\r提取失败: 该用户不存在, 若存在, 请前往issue页反馈:\n{}'.format(issue_page)
token_warning = '\r运行失败: guest_token获取失败, 请前往issue页反馈:\n{}'.format(issue_page)
parse_warning = '\r解析失败: 跳过解析此数据, 请带上错误数据信息前往issue页反馈:\n{}\n错误信息: {}'.format(
    issue_page, '{}')
cookie_warning = '\r参数错误: 输入的cookie格式错误, 请参考教程获取cookie:\n{}\n'.format(
    cookie_tips_page)
http_warning = '\r提取失败{}: http访问异常, 状态码: {} -> {}'
timeout_warning = '\r网络超时: 服务器未响应或断开链接, 正在重试...{}'
download_timeout_warning = '\r{} {}{}'
proxy_warning = '\r参数错误: 代理格式错误, 格式: \n [协议]://host:port / [协议]://user:pass@host:port [协议]为http或socks5'
user_unavailable_warning = '\r提取失败: 该用户已锁定/冻结, 访问锁定用户需要设置已关注账号的cookie'
age_restricted_warning = '\r提取失败: 该用户已设置年龄限制, 访问需要设置账号cookie'
network_error_warning = '\r网络连接失败, 请检查代理设置(程序默认使用系统代理)'
proxy_error_warning = '\r代理连接失败, 请检查代理设置是否正确'
input_warning = '\r解析失败: 错误的链接或命令'
check_update_warning = '\r检查更新失败, 程序继续运行, 失败信息:\n{}'
need_cookie_warning = '\r目前访问推特的media列表接口需要登录账号, 故请先设置cookie再爬取'
dl_nothing_warning = '\r未爬取到任何有效数据'
queue_empty_warning = '\r超过30秒未从任务队列中获取到数据'
input_num_warning = '请输入正确数字（回车继续）'

# normal text
task_finish = '\r文件下载任务已完成 {}/{}, 用时 {}s, 保存路径: {}'
fo_Task_finish = '\r关注列表爬取任务已完成, 保存路径: {}'
cookie_purge_success = '自定义cookie清除成功\n'
cookie_success = '\n自定义cookie导入成功\n'
input_cookie_ask = f'请复制cookie并粘贴到下方, 再单击回车确认(留空直接回车为清除cookie)\n* cookie获取教程：{cookie_tips_page}\n'
max_concurrency_ask = '下载线程数过高会使下载变慢，请勿设置过大\n\n' \
                      '0.返回\n\n' \
                      '请输入下载线程数，建议设置1~32之间（默认8）：'
set_type_ask = '输入数字选择，可多选，如“13”就是包含图片和视频\n\n' \
               '0.返回\n' \
               '1.下载图片\n' \
               '2.下载动图\n' \
               '3.下载视频\n' \
               '4.下载文本\n' \
               '5.所有\n\n' \
               '请输入（默认所有）：'
retweeted_status_ask = '是否下载转推\n\n' \
                       '0.返回\n' \
                       '1.是\n' \
                       '2.否\n' \
                       '请输入：\n\n'
quoted_status_ask = '是否下载引用推文\n\n' \
                    '0.返回\n' \
                    '1.是\n' \
                    '2.否\n' \
                    '请输入：\n\n'
media_status_ask = '是否下载非媒体(纯文本)推文\n\n' \
                    '0.返回\n' \
                    '1.是\n' \
                    '2.否\n' \
                    '请输入：\n\n'
download_settings_ask = '输入数字\n\n' \
                        '0.返回\n' \
                        '1.设置下载类型\n' \
                        '2.设置下载线程数\n' \
                        '3.设置是否下载引用推文\n' \
                        '4.设置是否下载转推\n\n' \
                        '5.设置是否下载非媒体\n\n' \
                        '请输入：'
reset_ask = '单击回车键->退出程序, 输入任意内容+回车->重置脚本\n'
continue_ask = '单击回车键->退出程序, 输入任意内容+回车->继续提取\n'
input_ask = '输入命令数字或链接 (支持批量, 一行一条, 双击回车确认)\n\n' \
            '0.退出脚本\n' \
            '1.设置cookie\n' \
            '2.设置网络代理\n' \
            '3.设置下载参数\n\n' \
            '请输入命令或链接：'
exit_ask = '\n单击回车键退出程序\n'
config_info = '已设置cookie: {cookie}, 排除转推: {retweeted}, 排除引用: {quoted}, 排除非媒体: {meida}, 爬取类型: {type}\n' \
              '线程数: {concurrency}, 代理: {proxy}\n' \
              '下载路径: {dl_path}' \
