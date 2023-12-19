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
exports.getNew2 = void 0;
const axios_1 = __importDefault(require("axios"));
const cheerio_1 = require("cheerio");
const iconv_lite_1 = require("iconv-lite");
const newsList = [];
const regex = /^(https?|http):\/\/www\.news\.cn/;
function getNew2() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve, reject) => __awaiter(this, void 0, void 0, function* () {
            console.log('开始进行一次新华网新闻爬取');
            const timeout = new Promise((resolve, reject) => {
                setTimeout(() => {
                    reject(new Error('请求超时'));
                }, 5000); // 设置超时时间为5秒
            });
            try {
                const res = yield Promise.race([
                    (0, axios_1.default)({
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
                        console.error(e);
                        console.error("爬取失败");
                        resolve(newsList);
                    }),
                    timeout
                ]);
                let html = null;
                try {
                    html = (0, iconv_lite_1.decode)(res.data, 'utf-8');
                }
                catch (error) {
                    resolve(newsList);
                }
                const $ = (0, cheerio_1.load)(html);
                const promises = [];
                $('div#head a, div#main a,div#bottom a').each((index, element) => {
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
                            let auth = $('#articleEdit .editor').text().trim();
                            if (auth !== "") {
                                let img = $('#detail img:first').attr('src');
                                let dec = $('#detail p').text().trim();
                                if (img === null || img === void 0 ? void 0 : img.endsWith("space.gif")) {
                                    img = "";
                                }
                                else {
                                    const lastIndex = link.lastIndexOf('/');
                                    img = (link.substring(0, lastIndex)) + "/" + img;
                                }
                                let time = $('.header-time').text().trim() + " " + $('.header-cont .source').text().trim();
                                if (img) {
                                    img = img.replace("https://", "http://");
                                    newsList.push({ title, link, dec, img, time, auth });
                                }
                                else {
                                    const img = "";
                                    newsList.push({ title, link, dec, img, time, auth });
                                }
                            }
                        }).catch((e) => {
                            console.log(e);
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
exports.getNew2 = getNew2;
