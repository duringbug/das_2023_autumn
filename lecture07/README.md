<!--
 * @Description: 
 * @Author: 唐健峰
 * @Date: 2023-11-07 18:28:32
 * @LastEditors: ${author}
 * @LastEditTime: 2023-11-21 18:06:55
-->
# [第一题](./Dockerfile)

# [第二题](./2.sh)

以下是针对每个问题的 SQL 查询语句：

# 第三题
创建 user 表并插入数据：

```sql
CREATE TABLE user (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    sex VARCHAR(10),
    age INT,
    phone VARCHAR(20)
);

INSERT INTO user (id, name, sex, age, phone) VALUES
(1, '张三', '男', 25, '1234567890'),
(2, '李四', '女', 22, '9876543210'),
(3, '王五', '男', 28, '4567890123');
```

# 第四题
查询年龄在 20 到 30 范围内的用户：

```sql
SELECT * FROM user WHERE age BETWEEN 20 AND 30;
```
# 第五题
删除名字包含“张”的用户：

```sql
DELETE FROM user WHERE name LIKE '%张%';
```

# 第六题
计算所有用户的平均年龄：

```sql
SELECT AVG(age) AS average_age FROM user;
```

# 第七题
查询年龄在 20 到 30 范围内、名字包含“张”的用户，并按照年龄从大到小排序：

```sql
SELECT * FROM user WHERE age BETWEEN 20 AND 30 AND name LIKE '%张%' ORDER BY age DESC;
```

# 第八题
创建 team 表和 score 表：

```sql
CREATE TABLE team (
    id INT PRIMARY KEY,
    teamName VARCHAR(255)
);

CREATE TABLE score (
    id INT PRIMARY KEY,
    teamid INT,
    userid INT,
    score INT,
    FOREIGN KEY (teamid) REFERENCES team(id),
    FOREIGN KEY (userid) REFERENCES user(id)
);
```

# 第九题
查询 teamName 为“ECNU”中年龄小于 20 的用户：

```sql
SELECT u.* FROM user u
JOIN score s ON u.id = s.userid
JOIN team t ON s.teamid = t.id
WHERE t.teamName = 'ECNU' AND u.age < 20;
```

# 第十题
计算 teamName 为“ECNU”的总分：

```sql
SELECT t.teamName, SUM(s.score) AS total_score
FROM team t
JOIN score s ON t.id = s.teamid
WHERE t.teamName = 'ECNU'
GROUP BY t.teamName;
```
