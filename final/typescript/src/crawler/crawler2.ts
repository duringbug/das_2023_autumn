import axios from 'axios';
import { load } from 'cheerio';
import { decode } from 'iconv-lite';

interface News {
    title: string;
    link: string;
    dec: string;
    img: string;
    time: string;
    auth: string;
}

const newsList: News[] = [];
const regex = /^(https?|http):\/\/www\.news\.cn/;

export async function getNew2(): Promise<News[]> {
    return new Promise<News[]>(async (resolve, reject) => {
        console.log('开始进行一次新华网新闻爬取')
        const timeout = new Promise((resolve, reject) => {
            setTimeout(() => {
                reject(new Error('请求超时'));
            }, 5000); // 设置超时时间为5秒
        });

        try {
            const res: any = await Promise.race([
                axios({
                    method: 'get',
                    url: "http://www.news.cn/",
                    headers: {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                        'Server': 'nginx',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'Accept-Language': 'zh-CN,zh;q=0.9'
                    },
                    responseType: 'arraybuffer'
                }).catch((e) => {
                    console.error(e)
                    console.error("爬取失败")
                    resolve(newsList)
                }),
                timeout
            ]);

            let html = null;
            try {
                html = decode(res.data, 'utf-8') as string;
            } catch (error) {
                resolve(newsList);
            }

            const $ = load(html as string);

            const promises: Promise<void>[] = [];

            $('div#head a, div#main a,div#bottom a').each((index, element) => {
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
                            let auth = $('#articleEdit .editor').text().trim();
                            if (auth !== "") {
                                let img = $('#detail img:first').attr('src');
                                let dec = $('#detail p').text().trim();
                                if (img?.endsWith("space.gif")) {
                                    img = ""
                                } else {
                                    const lastIndex = link.lastIndexOf('/');
                                    img = (link.substring(0, lastIndex)) + "/" + img;
                                }
                                let time = $('.header-time').text().trim() + " " + $('.header-cont .source').text().trim();
                                if (img) {
                                    img = img.replace("https://", "http://")
                                    newsList.push({ title, link, dec, img, time, auth });
                                } else {
                                    const img = "";
                                    newsList.push({ title, link, dec, img, time, auth });
                                }
                            }
                        }).catch((e) => {
                            console.log(e)
                            resolve(newsList)
                        })
                    );

                }
            });
            await Promise.all(promises);
            resolve(newsList)
        } catch (error) {
            console.error('An error occurred while crawling Baidu news:', error);
            resolve(newsList)
        }
    });
}
