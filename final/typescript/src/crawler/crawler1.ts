/*
 * @Description: 
 * @Author: 唐健峰
 * @Date: 2023-07-07 03:48:19
 * @LastEditors: ${author}
 * @LastEditTime: 2023-12-13 11:08:42
 */
import axios from 'axios';
import { load } from 'cheerio';

interface News {
    title: string;
    link: string;
    dec: string;
    img: string;
    time: string;
    auth: string;
}

const newsList: News[] = [];
const regex = /^(https?|http):\/\/www\.chinanews\.com/;

export async function getNew1(): Promise<News[]> {
    return new Promise<News[]>(async (resolve, reject) => {
        console.log('开始进行一次新闻爬取')
        const timeout = new Promise((resolve, reject) => {
            setTimeout(() => {
                reject(new Error('请求超时'));
            }, 10000); // 设置超时时间为5秒
        });

        try {
            const res: any = await Promise.race([
                axios({
                    method: 'get',
                    url: "http://www.chinanews.com.cn/",
                    headers: {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36',
                        'Server': 'nginx',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-CN,zh;q=0.9'
                    },
                }).catch((e) => {
                    console.error(e)
                    console.error("爬取失败")
                    // 打印请求信息
                    console.log("请求配置:", e.config);
                    console.log("请求响应状态码:", e.response.status);
                    console.log("请求响应头:", e.response.headers);
                    resolve(newsList)
                }),
                timeout
            ]);
            let html = null;
            try {
                html = res.data;
            } catch (error) {
                resolve(newsList);
            }

            const $ = load(html);

            const promises: Promise<void>[] = [];

            $('a').each((index, element) => {
                const title = $(element).text().trim();
                const link = $(element).attr('href');
                if (title && link && regex.test(link)) {
                    promises.push(
                        axios({
                            method: 'get',
                            url: link,
                            timeout: 5000,
                            headers: {
                                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36'
                            }
                        }).then((res) => {
                            const html = res.data;
                            const $ = load(html);
                            const dec = $('.left_zw p').text().trim() || $('content_desc p').eq(0).text().trim() || $('.left.desc p').eq(0).text().trim();
                            const currentImg = $('.current_img img').attr('src') || $('.left_ph img').attr('src') || $('.left_zw img').attr('src');
                            let time: string | undefined;
                            time = $('.source_time.left').text().trim() || $('.content_left_time').text().trim();
                            let auth = $('.editor').text().trim() || $('.left_name.right span').text().trim() || $('.content_editor').find('span').contents().text().trim();
                            auth = auth.trim();
                            const spaceIndex = time.indexOf(' ');
                            if (spaceIndex !== -1) {
                                const secondSpaceIndex = time.indexOf(' ', spaceIndex + 1);
                                if (secondSpaceIndex !== -1) {
                                    time = time.substr(0, secondSpaceIndex);
                                }
                            }
                            if (!time.endsWith('中国新闻网\n')) {
                                time = time + '中国新闻网\n';
                            }
                            if (currentImg) {
                                const img = "https:" + currentImg;
                                newsList.push({ title, link, dec, img, time, auth });
                            } else {
                                const img = "";
                                newsList.push({ title, link, dec, img, time, auth });
                            }

                        }).catch((e) => {
                            resolve(newsList)
                        })
                    );
                }
            });
            await Promise.all(promises);
            const data: { [key: string]: string } = newsList.reduce((result: any, news) => {
                const { link } = news;
                const jsonString = JSON.stringify(news, null, 2);
                result[link] = jsonString;
                return result;
            }, {});
        } catch (error) {
            console.error('An error occurred while crawling Baidu news:', error);
            resolve(newsList)
        }
    });
}
