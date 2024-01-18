/*
 * @Description: 
 * @Author: 唐健峰
 * @Date: 2023-12-13 11:02:56
 * @LastEditors: ${author}
 * @LastEditTime: 2023-12-22 10:03:45
 */
import { getNew1 } from "./crawler1";
import { getNew2 } from "./crawler2";
import { getNew3 } from "./crawler3";
import { getNew4 } from "./crawler4";

import { indexInit } from "../redis";

interface News {
    title: string;
    link: string;
    dec: string;
    img: string;
    time: string;
    auth: string;
}

export async function NewsProcessor(): Promise<boolean> {
    return new Promise<boolean>(async (resolve, reject) => {
        const [news1, news2, news3, news4] = await Promise.all([getNew1(), getNew2(), getNew3(), getNew4()]) as News[][];
        if (await indexInit(news1.concat(news2, news3, news4))) {
            console.log("成功")
            resolve(true)
        } else {
            resolve(false)
        }
    })
}
