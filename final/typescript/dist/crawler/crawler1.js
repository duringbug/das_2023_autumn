"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getNew1 = void 0;
/*
 * @Description:
 * @Author: 唐健峰
 * @Date: 2023-07-07 03:48:19
 * @LastEditors: ${author}
 * @LastEditTime: 2023-12-13 11:08:42
 */
const axios_1 = __importDefault(require("axios"));
const cheerio_1 = require("cheerio");
const newsList = [];
const regex = /^(https?|http):\/\/www\.chinanews\.com/;
function getNew1() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve, reject) => __awaiter(this, void 0, void 0, function* () {
            console.log('开始进行一次新闻爬取');
            const timeout = new Promise((resolve, reject) => {
                setTimeout(() => {
                    reject(new Error('请求超时'));
                }, 10000); // 设置超时时间为5秒
            });
            try {
                const res = yield Promise.race([
                    (0, axios_1.default)({
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
                        console.error(e);
                        console.error("爬取失败");
                        // 打印请求信息
                        console.log("请求配置:", e.config);
                        console.log("请求响应状态码:", e.response.status);
                        console.log("请求响应头:", e.response.headers);
                        resolve(newsList);
                    }),
                    timeout
                ]);
                let html = null;
                try {
                    html = res.data;
                }
                catch (error) {
                    resolve(newsList);
                }
                const $ = (0, cheerio_1.load)(html);
                const promises = [];
                $('a').each((index, element) => {
                    const title = $(element).text().trim();
                    const link = $(element).attr('href');
                    if (title && link && regex.test(link)) {
                        promises.push((0, axios_1.default)({
                            method: 'get',
                            url: link,
                            timeout: 5000,
                            headers: {
                                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36'
                            }
                        }).then((res) => {
                            const html = res.data;
                            const $ = (0, cheerio_1.load)(html);
                            const dec = $('.left_zw p').text().trim() || $('content_desc p').eq(0).text().trim() || $('.left.desc p').eq(0).text().trim();
                            const currentImg = $('.current_img img').attr('src') || $('.left_ph img').attr('src') || $('.left_zw img').attr('src');
                            let time;
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
                            }
                            else {
                                const img = "";
                                newsList.push({ title, link, dec, img, time, auth });
                            }
                        }).catch((e) => {
                            resolve(newsList);
                        }));
                    }
                });
                yield Promise.all(promises);
                const data = newsList.reduce((result, news) => {
                    const { link } = news;
                    const jsonString = JSON.stringify(news, null, 2);
                    result[link] = jsonString;
                    return result;
                }, {});
            }
            catch (error) {
                console.error('An error occurred while crawling Baidu news:', error);
                resolve(newsList);
            }
        }));
    });
}
exports.getNew1 = getNew1;
