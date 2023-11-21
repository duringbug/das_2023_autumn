# 使用官方MySQL 8镜像作为基础镜像
FROM mysql:8.2.0

# 设置MySQL环境变量
ENV MYSQL_ROOT_PASSWORD=password

# 创建数据卷用于存储MySQL数据
VOLUME /var/lib/mysql

# 暴露MySQL默认端口
EXPOSE 3306

# 启动MySQL服务器
CMD ["mysqld"]