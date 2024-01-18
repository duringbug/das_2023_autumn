/*
 * @Description: 
 * @Author: 唐健峰
 * @Date: 2023-12-14 09:51:40
 * @LastEditors: ${author}
 * @LastEditTime: 2023-12-22 09:59:44
 */
interface News {
    title: string;
    link: string;
    dec: string;
    img: string;
    time: string;
    auth: string;
}
import Redis from 'ioredis';
export async function indexInit(news: News[]): Promise<boolean> {
    return new Promise<boolean>(async (resolve, reject) => {
        const redis = new Redis({
            host: process.env.REDIS_HOST ? process.env.REDIS_HOST : '127.0.0.1', // Redis 服务器的主机地址
            port: process.env.REDIS_PORT ? parseInt(process.env.REDIS_PORT) : 6379, // Redis 服务器的端口号
            password: process.env.REDIS_PASSWORD ? process.env.REDIS_PASSWORD : 'Tjf04712', // Redis 服务器的密码（如果有的话）
            db: process.env.REDIS_DB ? parseInt(process.env.REDIS_DB) : 6,
        });
        // 在连接成功时执行操作
        redis.on('connect', () => {
            console.log('Connected to Redis');
        });
        // 在连接错误时处理错误
        redis.on('error', (error) => {
            redis.quit()
            console.error('Redis connection error:', error);
            reject(false);
        });

        // 清空 6 号库
        redis.select(6, (selectErr) => {
            if (selectErr) {
                console.error('选择数据库时发生错误:', selectErr);
                redis.quit();
                reject(false);
            } else {
                redis.flushdb((flushErr) => {
                    if (flushErr) {
                        console.error('清空数据库时发生错误:', flushErr);
                        redis.quit();
                        reject(false);
                    } else {
                        console.log('成功清空 6 号数据库');
                        insertData();
                    }
                });
            }
        });

        function insertData() {
            const pipeline = redis.pipeline();

            news.forEach((item) => {
                const index = `news:${item.link}`;
                pipeline.hmset(index, item);
            });

            pipeline.exec((error, results) => {
                if (error) {
                    console.error('Redis pipeline error:', error);
                    reject(false);
                } else {
                    console.log('News data uploaded to Redis successfully');
                    resolve(true);
                }

                redis.quit();
            });
        }
    })
}