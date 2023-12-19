/*
 * @Description: 
 * @Author: 唐健峰
 * @Date: 2023-12-13 11:02:56
 * @LastEditors: ${author}
 * @LastEditTime: 2023-12-14 10:48:24
 */
import { getNew1 } from "./crawler1";
import { getNew2 } from "./crawler2";
import { getNew3 } from "./crawler3";

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
        const [news1, news2, news3] = await Promise.all([getNew1(), getNew2(), getNew3()]) as News[][];
        if (await indexInit(news1.concat(news2, news3))) {
            console.log("成功")
            resolve(true)
        } else {
            resolve(false)
        }
    })
}