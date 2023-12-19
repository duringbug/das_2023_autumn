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
Object.defineProperty(exports, "__esModule", { value: true });
exports.NewsProcessor = void 0;
/*
 * @Description:
 * @Author: 唐健峰
 * @Date: 2023-12-13 11:02:56
 * @LastEditors: ${author}
 * @LastEditTime: 2023-12-14 09:58:42
 */
const crawler1_1 = require("./crawler1");
const crawler2_1 = require("./crawler2");
const crawler3_1 = require("./crawler3");
const redis_1 = require("../redis");
function NewsProcessor() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve, reject) => __awaiter(this, void 0, void 0, function* () {
            const [news1, news2, news3] = yield Promise.all([(0, crawler1_1.getNew1)(), (0, crawler2_1.getNew2)(), (0, crawler3_1.getNew3)()]);
            if (yield (0, redis_1.indexInit)(news1.concat(news2, news3))) {
                console.log("成功");
                resolve(true);
            }
            else {
                resolve(false);
            }
        }));
    });
}
exports.NewsProcessor = NewsProcessor;
