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
exports.indexInit = void 0;
const ioredis_1 = __importDefault(require("ioredis"));
function indexInit(news) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve, reject) => __awaiter(this, void 0, void 0, function* () {
            const redis = new ioredis_1.default({
                host: process.env.REDIS_HOST ? process.env.REDIS_HOST : '127.0.0.1',
                port: process.env.REDIS_PORT ? parseInt(process.env.REDIS_PORT) : 6379,
                password: process.env.REDIS_PASSWORD ? process.env.REDIS_PASSWORD : 'Tjf04712',
                db: process.env.REDIS_DB ? parseInt(process.env.REDIS_DB) : 6,
            });
            // 在连接成功时执行操作
            redis.on('connect', () => {
                console.log('Connected to Redis');
            });
            // 在连接错误时处理错误
            redis.on('error', (error) => {
                redis.quit();
                console.error('Redis connection error:', error);
                reject(false);
            });
            const pipeline = redis.pipeline();
            news.forEach((item) => {
                const index = `news:${item.link}`;
                pipeline.hmset(index, item);
            });
            pipeline.exec((error, results) => {
                if (error) {
                    console.error('Redis pipeline error:', error);
                    reject(false);
                }
                else {
                    console.log('News data uploaded to Redis successfully');
                    resolve(true);
                }
                redis.quit();
            });
        }));
    });
}
exports.indexInit = indexInit;
