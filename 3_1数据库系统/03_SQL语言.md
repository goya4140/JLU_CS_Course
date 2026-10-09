# 第3单元 SQL语言

<!-- toc:start -->
## 知识点索引目录

点击下面的知识点可跳转到对应小节。

- [怎样阅读本章与语法约定](#ch03-s001)
- [1. 【课程总结PPT重点基础】从学生选课问题建立共同数据](#ch03-s002)
  - [1.1 业务背景、字段与约定](#ch03-s003)
  - [1.2 SQL 各类语句分别解决什么问题](#ch03-s004)
- [2. 【课程PPT补充知识点，模拟题相关】先选择合适的数据类型](#ch03-s005)
  - [2.1 文字：CHAR 与 VARCHAR](#ch03-s006)
  - [2.2 数字：整数、精确小数与近似数](#ch03-s007)
  - [2.3 时间与大对象](#ch03-s008)
- [3. 【课程总结PPT重点知识点】建表与完整性约束](#ch03-s009)
  - [3.1 从业务规则写出三张表](#ch03-s010)
  - [3.2 逐条判断什么记录可以写入](#ch03-s011)
  - [3.3 UNIQUE、默认值与引用动作](#ch03-s012)
  - [3.4 ALTER、DROP 与 DELETE 的区别](#ch03-s013)
- [4. 【课程总结PPT重点基础】SELECT—FROM—WHERE：先筛行，再取列](#ch03-s014)
  - [4.1 查计算机系学生](#ch03-s015)
  - [4.2 DISTINCT 对整行输出去重](#ch03-s016)
  - [4.3 条件、括号与 LIKE](#ch03-s017)
  - [4.4 ORDER BY、别名与计算](#ch03-s018)
- [5. 【课程PPT补充知识点，但属于查询基础】连接：按对应编号拼事实](#ch03-s019)
  - [5.1 两张表怎样配对](#ch03-s020)
  - [5.2 先看四条完整匹配结果，再连课程](#ch03-s021)
  - [5.3 左、右、全外连接](#ch03-s022)
- [6. 【课程总结PPT重点知识点】集合查询：合并、求共同与排除](#ch03-s023)
- [7. 【课程总结PPT重点知识点】NULL 与三值逻辑](#ch03-s024)
  - [7.1 空值不等于零，也不等于空文字](#ch03-s025)
  - [7.2 真、假、未知怎样组合](#ch03-s026)
  - [7.3 为什么 NOT IN 会踩坑](#ch03-s027)
- [8. 【课程总结PPT重点知识点】聚集、GROUP BY 与 HAVING](#ch03-s028)
  - [8.1 把几行变成统计值](#ch03-s029)
  - [8.2 GROUP BY 是先分堆](#ch03-s030)
  - [8.3 WHERE 过滤行，HAVING 过滤组](#ch03-s031)
  - [8.4 把零选课课程也数出来](#ch03-s032)
- [9. 【课程总结PPT重点知识点】子查询：先问一个小问题](#ch03-s033)
  - [9.1 IN：把内层结果当名单](#ch03-s034)
  - [9.2 标量子查询、SOME 与 ALL](#ch03-s035)
  - [9.3 相关 EXISTS：逐个学生检查有没有](#ch03-s036)
  - [9.4 双重 NOT EXISTS：把“所有”变成“没有缺项”](#ch03-s037)
  - [9.5 派生表与 WITH：给中间结果起名](#ch03-s038)
  - [9.6 LATERAL 与 UNIQUE 谓词：课件扩展](#ch03-s039)
- [10. 【课程总结PPT重点知识点】INSERT、DELETE、UPDATE 与 CASE](#ch03-s040)
  - [10.1 INSERT：添加一条明确事实](#ch03-s041)
  - [10.2 DELETE：按条件删除行](#ch03-s042)
  - [10.3 UPDATE：改变已有行的值](#ch03-s043)
  - [10.4 CASE：逐行选用不同计算规则](#ch03-s044)
- [11. 【课程总结PPT重点知识点】视图与视图更新](#ch03-s045)
  - [11.1 给一个查询结果长期起名](#ch03-s046)
  - [11.2 为什么不是所有视图都能直接修改](#ch03-s047)
  - [11.3 WITH CHECK OPTION 防止改完跑出视图](#ch03-s048)
- [12. 【课程PPT补充知识点】SQL 中的事务边界](#ch03-s049)
- [13. 【课程PPT补充知识点，模拟题相关】用户定义类型与域](#ch03-s050)
  - [13.1 为同样的文字表示赋予不同身份](#ch03-s051)
  - [13.2 域是在既有类型上加规则](#ch03-s052)
- [14. 【课程总结PPT重点知识点】权限、角色与授权传播](#ch03-s053)
  - [14.1 让教师能查但不能任意改表](#ch03-s054)
  - [14.2 角色减少重复授权](#ch03-s055)
  - [14.3 WITH GRANT OPTION 与授权图](#ch03-s056)
- [15. 【课程PPT补充知识点】程序怎样安全调用 SQL](#ch03-s057)
  - [15.1 JDBC、ODBC 与结果集](#ch03-s058)
  - [15.2 参数化语句与 SQL 注入](#ch03-s059)
  - [15.3 嵌入式、动态 SQL 与元数据](#ch03-s060)
- [16. 【课程PPT补充知识点，模拟题相关】函数、过程与触发器](#ch03-s061)
  - [16.1 先用不同任务分清调用方式](#ch03-s062)
  - [16.2 触发器需要说清四件事](#ch03-s063)
  - [16.3 表函数与外部例程](#ch03-s064)
- [17. 【课程PPT补充知识点】递归查询：不断沿先修关系往前找](#ch03-s065)
  - [17.1 先说明新的业务与数据](#ch03-s066)
  - [17.2 从一轮到多轮组成表达式](#ch03-s067)
- [18. 【课程PPT补充知识点】多级汇总、窗口与 OLAP](#ch03-s068)
  - [18.1 另一个业务：学校用品销售](#ch03-s069)
  - [18.2 ROLLUP、CUBE 与 GROUPING SETS](#ch03-s070)
  - [18.3 窗口函数不把明细压成一行](#ch03-s071)
  - [18.4 OLAP 的几种动作](#ch03-s072)
- [19. 常见误解与排查顺序](#ch03-s073)
- [20. 本单元模拟题](#ch03-s074)
  - [题目一：`VARCHAR` 与 `CHAR`](#ch03-s075)
  - [题目二：LIKE 查询](#ch03-s076)
    - [先看教学名单与手工匹配](#ch03-s077)
  - [题目三：函数和触发器](#ch03-s078)
  - [题目四：DISTINCT](#ch03-s079)
  - [题目五：用户定义类型和域](#ch03-s080)
  - [题目六：银行数据库综合应用](#ch03-s081)
    - [先读懂银行业务和教学数据](#ch03-s082)
    - [（1）创建表](#ch03-s083)
    - [（2）Brighton 分行存款客户](#ch03-s084)
    - [（3）平均余额小于 5000 元的支行](#ch03-s085)
    - [（4）有贷款但无账户的客户](#ch03-s086)
    - [（5）给高于平均余额的账户增加 3% 利息](#ch03-s087)
- [21. 自拟自测题与逐步答案](#ch03-s088)
  - [21.1 哪些学生选了 C1 但没选 C2？](#ch03-s089)
  - [21.2 找至少两条选课记录的学生](#ch03-s090)
  - [21.3 包含零选课学生，显示选课数](#ch03-s091)
  - [21.4 找全部计算机系开设课程都选过的学生](#ch03-s092)
- [22. 复习路线](#ch03-s093)

<!-- toc:end -->

> 课件来源：`课程ppt/ch3.pdf`、`ch4.pdf`、`ch5.pdf`。重点依据：`课程总结.pptx`；原模拟题来源：`试题模拟.pptx`。本章沿用课程 SQL 标准口径，示例数据均为教学用。

<a id="ch03-s001"></a>

## 怎样阅读本章与语法约定

> 课程定位：课程总结 PPT 中的“第3、4、5章：SQL语句”。**DDL、DML、DCL、集合运算、空值、聚集、HAVING、NOT EXISTS、嵌套查询、视图和完整性约束均为课程重点**。

SQL 是 Structured Query Language，即结构化查询语言。本章先用同一套学校数据学习查询，再学习修改、授权和扩展功能。**DBMS**是管理数据库的软件。SQL 标准规定语言含义，但各 DBMS 支持的版本、类型、大小写比较、返回显示和扩展语法不同；涉及差异处单独标明。未指定产品，不能承诺所有示例在每种软件中原样运行。

**【课程总结PPT重点知识点】**是总结列出的核心范围；**【课程PPT补充知识点】**是课件延伸内容；**【模拟题相关】**表示原模拟题涉及。代码里的分号结束一条语句；单引号表示文字值；括号表示参数、条件分组或子查询；逗号分隔项目。大写关键字是为了好读，不表示所有名称都必须大写。

<a id="ch03-s002"></a>

## 1. 【课程总结PPT重点基础】从学生选课问题建立共同数据

<a id="ch03-s003"></a>

### 1.1 业务背景、字段与约定

学校登记学生、课程与选课成绩。本章教学业务不考虑学期和重修；每位学生对每门课程最多一条选课记录。`student`是学生表；`SID`是学号、`name`是姓名、`dept`是学生所在系。

| SID | name | dept |
| --- | --- | --- |
| S1 | 小林 | 计算机 |
| S2 | 小周 | 数学 |
| S3 | 小陈 | 计算机 |
| S4 | 小吴 | 数学 |

`course`是课程表；`CID`是课程号、`title`是课程名、`dept`是开课系、`credits`是学分。学生系与开课系不是同一事实，跨系选课允许。

| CID | title | dept | credits |
| --- | --- | --- | --- |
| C1 | 数据库 | 计算机 | 3 |
| C2 | 程序设计 | 计算机 | 4 |
| C3 | 高数 | 数学 | 5 |

`takes`是选课表；一行表示某学生选了某课程；`score`是成绩。S4 尚未选课，C3 尚无人选。

| SID | CID | score |
| --- | --- | --- |
| S1 | C1 | 80 |
| S1 | C2 | 90 |
| S2 | C1 | 70 |
| S3 | C2 | 60 |

后面每个查询均从这套原始数据出发；修改、空值或其他业务另有独立数据时，会说明。**结果表没有顺序保证**，除非写 `ORDER BY`；文中排列只是为了讲解。

<a id="ch03-s004"></a>

### 1.2 SQL 各类语句分别解决什么问题

| 类别 | 中文意思与用途 | 本章例子 |
| --- | --- | --- |
| DDL | 数据定义语言，约定表结构 | CREATE TABLE 建表 |
| DML | 数据操纵语言，查询或改变行 | SELECT 查询、INSERT 新增 |
| DCL | 数据控制语言，管理权限 | GRANT 授权 |
| TCL | 事务控制语言，整体提交或撤销 | COMMIT、ROLLBACK |

这是便于学习的常用分类，`SELECT`有时另称查询语言。**声明式**表示你主要写“要什么结果”，具体怎样读取由 DBMS 选择，不必写逐行循环。

<a id="ch03-s005"></a>

## 2. 【课程PPT补充知识点，模拟题相关】先选择合适的数据类型

<a id="ch03-s006"></a>

### 2.1 文字：CHAR 与 VARCHAR

学号 S1 长度稳定；姓名“小林”或“欧阳小明”长度不一。`CHAR(n)`表示固定长度文字，`VARCHAR(n)`表示有最大长度限制的可变长度文字，`n`是长度参数。

例如 `CHAR(5)`保存短文字时通常按固定宽度补空格，`VARCHAR(5)`允许不同实际长度且不超过上限。“固定”不等于只能存一种内容；“可变”不等于无限长。实际存储字节数、尾随空格比较及字符长度计量需按产品核实，不能仅凭类型名算磁盘占用。

<a id="ch03-s007"></a>

### 2.2 数字：整数、精确小数与近似数

- `INTEGER`或 `INT`表示整数，适合人数等没有小数的数量。
- `NUMERIC(p,s)`表示精确小数，`p`为总有效数字位数，`s`为小数位数。例如 `NUMERIC(5,2)`可表示 123.45，总共五位，其中两位小数。
- `REAL`、`FLOAT`等表示近似数，内部可能无法精确表示某些十进制小数。金额通常需要精确小数，不能把近似值当成必然精确的金额。

“精确”指按规定十进制精度表示；超出范围或小数位时怎样报错、舍入，需看产品和设置。

<a id="ch03-s008"></a>

### 2.3 时间与大对象

课程开始日期可用 `DATE`，一天中的时刻可用 `TIME`，日期加时刻可用 `TIMESTAMP`。独立例子 `DATE '2026-09-01'`表示 2026 年 9 月 1 日；前面的 `DATE`指定值类型，引号内为日期文字。时区支持和格式解析存在产品差异。

**大对象**用于很长的数据：`BLOB`是二进制大对象，例如照片文件的字节；`CLOB`是字符大对象，例如长篇文本。不是所有产品都用这两个名称，且大对象不能无条件像普通短文字一样排序、比较或建索引。

<a id="ch03-s009"></a>

## 3. 【课程总结PPT重点知识点】建表与完整性约束

> **本节为课程总结PPT明确列出的重点知识点：DDL 与完整性约束。**

<a id="ch03-s010"></a>

### 3.1 从业务规则写出三张表

先建学生和课程，再建引用它们的选课表：

```sql
CREATE TABLE student (
    SID CHAR(2) PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    dept VARCHAR(20)
);
CREATE TABLE course (
    CID CHAR(2) PRIMARY KEY,
    title VARCHAR(40) NOT NULL,
    dept VARCHAR(20),
    credits INTEGER CHECK (credits > 0)
);
CREATE TABLE takes (
    SID CHAR(2),
    CID CHAR(2),
    score NUMERIC(5,2),
    PRIMARY KEY (SID, CID),
    FOREIGN KEY (SID) REFERENCES student(SID),
    FOREIGN KEY (CID) REFERENCES course(CID),
    CHECK (score >= 0 AND score <= 100)
);
```

`CREATE TABLE`是创建表；每个括号内项目声明一列或一条表级规则。`PRIMARY KEY`叫**主码约束**，要求指定列组合唯一且不为空；`(SID,CID)`表示二者合起来区分一次选课，不是要求各列单独唯一。

`FOREIGN KEY`叫**外码约束**；`REFERENCES`说明必须对应哪张表的哪列。它要求非空的选课学号、课程号分别存在于学生、课程表。`NOT NULL`是非空约束；`CHECK`检查条件；`AND`表示两个条件都需要满足；`>=`、`<=`分别为大于等于、小于等于。

建表只是生成结构，尚未插入第 1 节数据。

<a id="ch03-s011"></a>

### 3.2 逐条判断什么记录可以写入

| 独立试插入记录 | 判断 | 原因 |
| --- | --- | --- |
| S1 C3 88 | 可通过这些约束 | 学生与课程存在，组合未出现，成绩合法 |
| S1 C1 88 | 拒绝 | 原始数据已有 S1 C1，组合主码重复 |
| S9 C1 88 | 拒绝 | 学生 S9 不存在 |
| S2 C2 110 | 拒绝 | 成绩超出 100 |
| S2 C2 NULL | 可通过本例约束 | 成绩尚未知；CHECK 不是非空约束 |

`NULL`表示值缺失或未知，详细逻辑见第 7 节。标准 SQL 的 `CHECK`在条件为假时拒绝，条件未知时并不因此拒绝；如果成绩必须填写，还要给 `score`加 `NOT NULL`。选课学号和课程号虽未另写非空，其主码身份已要求非空。

<a id="ch03-s012"></a>

### 3.3 UNIQUE、默认值与引用动作

**唯一约束** `UNIQUE`用于声明另一组不可重复的身份，例如独立业务中学生邮箱。与主码不同，一张表可有多个唯一约束；空值在唯一约束中的处理有产品和标准选项差异，不应笼统说所有产品只能出现一个空值。

**默认值** `DEFAULT`是在插入时未提供该列的值时采用的值，例如独立建表示例 `credits INTEGER DEFAULT 3`。明确写入 NULL 并不普遍等于请求默认值。

引用动作处理“被引用记录删除或主码更新怎么办”：

- `NO ACTION`表示仍需通过外码检查；约束检查时点影响执行结果。
- `CASCADE`表示级联：父记录删除或键更新会向引用记录传播。
- `SET NULL`表示把外码设为空，前提是该列允许空。
- `SET DEFAULT`表示设为默认值，默认值仍要满足外码规则。

例如 `FOREIGN KEY (CID) REFERENCES course(CID) ON DELETE CASCADE`会在删除一门课时连带删除选课记录。是否允许这样做必须由业务决定；不同 DBMS 对动作支持不完全相同。

<a id="ch03-s013"></a>

### 3.4 ALTER、DROP 与 DELETE 的区别

若增加邮箱列，可写 `ALTER TABLE student ADD email VARCHAR(100);`：`ALTER TABLE`修改结构，`ADD`增加列。`DROP TABLE student;`是移除表对象，`DELETE FROM student;`是移除表中全部行而保留结构。本章仅解释语义，不在真实数据库执行这些操作。外码、权限、DDL 是否可回滚等行为要按产品确认。

<a id="ch03-s014"></a>

## 4. 【课程总结PPT重点基础】SELECT—FROM—WHERE：先筛行，再取列

> **本节属于课程总结PPT“SQL语句”的重点基础。**

<a id="ch03-s015"></a>

### 4.1 查计算机系学生

**目标**：显示计算机系学生的学号和姓名。手工逐行看学生系：S1、S3 符合，S2、S4 不符合，再只拿学号和姓名。

```sql
SELECT SID, name
FROM student
WHERE dept = '计算机';
```

`FROM student`说明从哪里取数据，`WHERE`筛选行，`SELECT`列出要输出的列。逻辑上先找来源、筛行，再计算输出；书写顺序并不是物理执行顺序。

| SID | name |
| --- | --- |
| S1 | 小林 |
| S3 | 小陈 |

`SELECT *`里的星号表示输出全部列；本查询没有修改学生表。

<a id="ch03-s016"></a>

### 4.2 DISTINCT 对整行输出去重

**目标**：知道出现过哪些学生系。取 `dept`得到计算机、数学、计算机、数学，若只想每种系一次：

```sql
SELECT DISTINCT dept FROM student;
```

| dept |
| --- |
| 计算机 |
| 数学 |

`DISTINCT`表示消除输出中的重复行，重复比较针对选择列表的整体。若写 `SELECT DISTINCT SID,dept`，四个不同学号仍产生四行。SQL 默认可保留重复行，这与第 02 章纯关系代数的集合约定不同。

<a id="ch03-s017"></a>

### 4.3 条件、括号与 LIKE

`AND`表示且，`OR`表示或，`NOT`表示否定；`<>`表示不等于。独立条件 `(score>=80 OR CID='C2') AND SID='S1'`的括号要求先判断“高分或 C2”，再要求 S1。不要依赖自己记忆中的优先级写模糊条件。

`BETWEEN 70 AND 90`包含两端，等价于 `>=70 AND <=90`。`IN ('C1','C2')`表示属于给定列表。

**LIKE 场景**：教务员想找姓名中含“小”的学生。
```sql
SELECT SID,name FROM student WHERE name LIKE '%小%';
```
`LIKE`做文字模式匹配；`%`表示任意长度的文字，包括零个字符；`_`表示一个字符。这里四位学生都符合，完整结果如下：

| SID | name |
| --- | --- |
| S1 | 小林 |
| S2 | 小周 |
| S3 | 小陈 |
| S4 | 小吴 |

若要查字面上的百分号，需要使用转义规则，具体规则按产品说明。大小写、中文比较取决于**排序规则**，即系统比较和排序文字的规则。

<a id="ch03-s018"></a>

### 4.4 ORDER BY、别名与计算

**目标**：查看全部成绩，按成绩由高到低。`AS`给输出起临时名称，`DESC`表示降序，`ASC`为升序。

```sql
SELECT SID,CID,score,score+5 AS adjusted_score
FROM takes
ORDER BY score DESC, SID ASC;
```

| SID | CID | score | adjusted_score |
| --- | --- | --- | --- |
| S1 | C2 | 90 | 95 |
| S1 | C1 | 80 | 85 |
| S2 | C1 | 70 | 75 |
| S3 | C2 | 60 | 65 |

`score+5`是计算显示值，不会改成绩。第二个排序项只在前一个相同时打破并列；若仍并列，要再加唯一列才能保证确定顺序。空值默认排前排后以及 `NULLS FIRST/LAST`支持有产品差异。

<a id="ch03-s019"></a>

## 5. 【课程PPT补充知识点，但属于查询基础】连接：按对应编号拼事实

<a id="ch03-s020"></a>

### 5.1 两张表怎样配对

**目标**：查数据库课选课人的姓名和成绩。选课表有学号没有姓名；学生表有姓名。因此先按相同学号匹配，再留下 C1。

对 S1 C1 80，依次检查学生 S1、S2、S3、S4，仅 S1 匹配，拼成 S1 小林 C1 80。对 S2 C1 70，只有 S2 匹配。

```sql
SELECT s.SID,s.name,t.score
FROM student AS s
JOIN takes AS t ON s.SID=t.SID
WHERE t.CID='C1';
```

`s`、`t`是表的**别名**，只在此语句中使用；`s.SID`的点表示“表 s 的 SID 列”。`JOIN`连接两来源，`ON`指定配对条件。两边编号相同的行才进入这种**内连接**结果。

| SID | name | score |
| --- | --- | --- |
| S1 | 小林 | 80 |
| S2 | 小周 | 70 |

S4 没有选课，内连接不为它制造记录；S3 有 C2 记录，但被 C1 筛选排除。

<a id="ch03-s021"></a>

### 5.2 先看四条完整匹配结果，再连课程

**目标**：给每条选课补上学生姓名和课程名称。先 student 与 takes 得到四行；再用课程号匹配 course。没有任何记录缺失对应学生或课程。

```sql
SELECT s.name,c.title,t.score
FROM student AS s
JOIN takes AS t ON s.SID=t.SID
JOIN course AS c ON t.CID=c.CID;
```

| name | title | score |
| --- | --- | --- |
| 小林 | 数据库 | 80 |
| 小林 | 程序设计 | 90 |
| 小周 | 数据库 | 70 |
| 小陈 | 程序设计 | 60 |

不能写 `student NATURAL JOIN takes NATURAL JOIN course`来代替。`NATURAL JOIN`叫**自然连接**，会自动要求所有同名列相等；这里 `dept`同时表示学生系和开课系，会错误排除数学系小周的计算机课程。明确的 `ON`让业务对应关系更清楚。

<a id="ch03-s022"></a>

### 5.3 左、右、全外连接

**目标**：列出每位学生及其选课，没选课的也保留。`LEFT JOIN`叫左外连接：正常匹配，并为左表无匹配的行补一条右侧列为 NULL 的行。

```sql
SELECT s.SID,s.name,t.CID,t.score
FROM student AS s
LEFT JOIN takes AS t ON s.SID=t.SID;
```

| SID | name | CID | score |
| --- | --- | --- | --- |
| S1 | 小林 | C1 | 80 |
| S1 | 小林 | C2 | 90 |
| S2 | 小周 | C1 | 70 |
| S3 | 小陈 | C2 | 60 |
| S4 | 小吴 | NULL | NULL |

`RIGHT JOIN`对称保留右侧，`FULL OUTER JOIN`两侧无匹配者都保留，支持情况需按产品核实。`CROSS JOIN`产生所有两两组合，不设配对条件；本例 4 学生乘 4 选课记录会有 16 行，不等于有效选课对应关系。

**常见错误**：在左连接后写 `WHERE t.score>=80`，S4 的 NULL 比较不为真，会被排除。如果目标是“保留所有学生，只匹配高分记录”，应把 `t.score>=80`放进 `ON`。

<a id="ch03-s023"></a>

## 6. 【课程总结PPT重点知识点】集合查询：合并、求共同与排除

> **本节为课程总结PPT明确列出的重点知识点：集合运算。**

**背景**：把选 C1 的学生看成名单 A，把选 C2 的看成名单 B。A 为 S1、S2；B 为 S1、S3。两边都只输出 SID 一列，所以能按同一结构比较。

| 运算 | 普通语言 | 完整结果 |
| --- | --- | --- |
| UNION | 在任一名单出现 | S1、S2、S3 |
| INTERSECT | 两个名单都出现 | S1 |
| EXCEPT | 在左名单但不在右名单 | S2 |

例如：
```sql
SELECT SID FROM takes WHERE CID='C1'
EXCEPT
SELECT SID FROM takes WHERE CID='C2';
```

`EXCEPT`执行左减右，交换两边会得到 S3。三种运算默认对结果去重；`UNION ALL`保留重复，本例有 S1 两次、S2 一次、S3 一次。`INTERSECT ALL`、`EXCEPT ALL`涉及出现次数，支持并不普遍。

两侧输出列数须相同，对应位置的类型要兼容；相同列名不是唯一判断条件。组合多个集合运算时用括号明确分组，最终排序作用域也需明确。

<a id="ch03-s024"></a>

## 7. 【课程总结PPT重点知识点】NULL 与三值逻辑

> **本节为课程总结PPT明确列出的重点知识点：空值。**

<a id="ch03-s025"></a>

### 7.1 空值不等于零，也不等于空文字

**独立场景**：一份成绩通知 `grade_notice(SID,score)`中，成绩尚未全部公布。它不替换本章原始 takes。

| SID | score |
| --- | --- |
| S1 | 80 |
| S2 | 0 |
| S3 | NULL |

0 表示已知为零分；NULL 表示没有已知成绩；空字符串 `''`是长度为零的文字，是否与 NULL 区分要看产品，标准概念区分二者。

比较 `score>=60`时，S1 为真，S2 为假，S3 为**未知**。SQL 的条件因此有真、假、未知三种值，叫**三值逻辑**。`WHERE`只留下真，所以查询结果只有 S1 80；不会把未知当成“肯定不及格”。

<a id="ch03-s026"></a>

### 7.2 真、假、未知怎样组合

用 U 表示未知，T 表示真，F 表示假。这三个字母是表格缩写，不是 SQL 关键字。

| P | NOT P |
| --- | --- |
| T | F |
| F | T |
| U | U |

| P | Q | P AND Q | P OR Q |
| --- | --- | --- | --- |
| T | T | T | T |
| T | F | F | T |
| T | U | U | T |
| F | F | F | F |
| F | U | F | U |
| U | U | U | U |

`P`、`Q`代表任意两个条件。交换它们不改变 AND、OR 的结果。例如“零分且成绩未知”第一部分若为假，整体一定为假；“确实是 S1 或成绩未知”第一部分为真，整体一定为真。

`score=NULL`不能用来判断缺值，因为普通等号与 NULL 的比较为未知。应写 `score IS NULL`；`IS NOT NULL`表示已知非空。`COALESCE(score,0)`返回第一个非空参数，会在显示时把缺值代成零；这是你做的解释选择，不能声称 S3 真的考了零分。

<a id="ch03-s027"></a>

### 7.3 为什么 NOT IN 会踩坑

**目标**：检查某学生是否不在给定名单中。假设独立名单只有 `S1`和 NULL，NULL 表示一个尚未识别的学号。

判断 `'S2' NOT IN ('S1',NULL)`相当于“不同于 S1，并且不同于那个未知学号”。第一项真，第二项未知，整体未知，WHERE 不保留 S2。

`NOT EXISTS`检查的是“有没有满足明确匹配条件的行”，常能更直接地表达“没有对应记录”，但需写对相关条件；它并不是会替你识别未知学号。第 9 节给完整例子。

<a id="ch03-s028"></a>

## 8. 【课程总结PPT重点知识点】聚集、GROUP BY 与 HAVING

> **本节为课程总结PPT明确列出的重点知识点：聚集函数与 HAVING。**

<a id="ch03-s029"></a>

### 8.1 把几行变成统计值

**聚集函数**把一组行计算成一个统计值。对原始 takes，四个成绩为 80、90、70、60：

| 函数 | 手算 | 结果 |
| --- | --- | --- |
| COUNT(*) | 数全部四行 | 4 |
| COUNT(score) | 数成绩非空的行 | 4 |
| SUM(score) | 80+90+70+60 | 300 |
| AVG(score) | 300÷4 | 75 |
| MIN(score) | 最小成绩 | 60 |
| MAX(score) | 最大成绩 | 90 |

`COUNT`是计数，`SUM`求和，`AVG`平均，`MIN/MAX`最小／最大。除 COUNT(*) 外，这些对某列的聚集通常忽略 NULL。对第 7 节成绩通知，AVG 是 `(80+0)÷2=40`，COUNT(score)=2，COUNT(*)=3，不能除以 3。

若要数实际不同的学生，`COUNT(DISTINCT SID)`先对非空学号去重再数，本例 S1、S2、S3 共 3 人；它与四条选课记录不同。

对没有行的输入，COUNT 返回 0；SUM、AVG、MIN、MAX 通常返回 NULL。若业务希望显示零，可显式 COALESCE，不能把“没有数据”和“已知总额零”默默混淆。

<a id="ch03-s030"></a>

### 8.2 GROUP BY 是先分堆

**目标**：每门已有人选的课程有多少条选课、平均成绩是多少。

手工先按 CID 分堆：C1 堆为 80、70，C2 堆为 90、60；每堆数两行并算平均。

```sql
SELECT CID,COUNT(*) AS n,AVG(score) AS avg_score
FROM takes
GROUP BY CID;
```

`GROUP BY CID`表示 CID 相同的行放同一组。每组只输出一行：

| CID | n | avg_score |
| --- | --- | --- |
| C1 | 2 | 75 |
| C2 | 2 | 75 |

C3 没在 takes 出现，所以没有组。`SELECT SID,CID,AVG(score) GROUP BY CID`是有问题的：一个组里可能有多个 SID，无法唯一决定显示哪个。入门时把非聚集输出列写入 GROUP BY；标准中的函数依赖扩展以及产品放宽规则需另行核实。

<a id="ch03-s031"></a>

### 8.3 WHERE 过滤行，HAVING 过滤组

**目标**：找原始平均成绩大于等于 75 的课程。先按上节分堆、算平均，再检查每堆平均：

```sql
SELECT CID,AVG(score) AS avg_score
FROM takes
GROUP BY CID
HAVING AVG(score)>=75;
```

两组均保留，结果 C1 75、C2 75。`HAVING`在分组计算后筛组。

若先写 `WHERE score>=80`，C1 只剩 80，C2 只剩 90，平均变成 80、90。那回答的是“高分记录的平均”，不是原平均。不要把两个筛选阶段互换。

<a id="ch03-s032"></a>

### 8.4 把零选课课程也数出来

先以 course 为左表，左连接 takes，使 C3 得到一条补 NULL 的行，再计数实际匹配的学号：

```sql
SELECT c.CID,COUNT(t.SID) AS n
FROM course AS c LEFT JOIN takes AS t ON c.CID=t.CID
GROUP BY c.CID;
```

| CID | n |
| --- | --- |
| C1 | 2 |
| C2 | 2 |
| C3 | 0 |

用 `COUNT(*)`会把 C3 的补空行也数成 1；用非空的选课主码列 `t.SID`只数真实匹配记录。

<a id="ch03-s033"></a>

## 9. 【课程总结PPT重点知识点】子查询：先问一个小问题

> **本节为课程总结PPT明确列出的重点知识点：嵌套子查询。**
> **本节为课程总结PPT明确列出的重点知识点**：`NOT EXISTS` 常通过“双重否定”表达全称条件。

<a id="ch03-s034"></a>

### 9.1 IN：把内层结果当名单

**目标**：找选 C1 的学生姓名。内层 `SELECT SID FROM takes WHERE CID='C1'`先得到 S1、S2，外层逐名查名单。

```sql
SELECT SID,name FROM student
WHERE SID IN (SELECT SID FROM takes WHERE CID='C1');
```

| SID | name |
| --- | --- |
| S1 | 小林 |
| S2 | 小周 |

括号里完整 SELECT 是**子查询**；外面的是外层查询。这个子查询不使用外层变量，是非相关子查询。实际执行是否先整体计算由优化器决定，这里说的是理解顺序。

<a id="ch03-s035"></a>

### 9.2 标量子查询、SOME 与 ALL

**标量**意为单个值。查高于全体平均成绩的选课：

```sql
SELECT SID,CID,score FROM takes
WHERE score > (SELECT AVG(score) FROM takes);
```

内层得到 75，外层分别比较 80、90、70、60，完整结果如下：

| SID | CID | score |
| --- | --- | --- |
| S1 | C1 | 80 |
| S1 | C2 | 90 |

标量子查询零行时产生 NULL，多于一行通常报错；聚集且无 GROUP BY 时即使输入空，也产生一个聚集结果行。

`> SOME`表示大于子查询结果中的至少一个值，`SOME`也可写 `ANY`。`> ALL`表示大于每一个值。例如拿 C1 的 80、70 作比较：90 大于 SOME 与 ALL；75 大于 SOME，不大于 ALL；60 都不满足。若有未知比较，仍要用三值逻辑判断。

子查询空集时，ALL 条件为真，因为没有反例；SOME 为假，因为没有满足者。产品对这些语法支持不同。

<a id="ch03-s036"></a>

### 9.3 相关 EXISTS：逐个学生检查有没有

**目标**：找至少选一门课的学生。对外层 S1，内层只找 SID=S1 的选课，有两行；对 S2、S3 有一行；对 S4 无行。

```sql
SELECT s.SID,s.name FROM student AS s
WHERE EXISTS (
    SELECT 1 FROM takes AS t WHERE t.SID=s.SID
);
```

`EXISTS`表示内层有没有任何行。`SELECT 1`里的 1 是常量，只强调我们关心存在性，不是统计行数。`t.SID=s.SID`引用当前外层学生，叫**相关子查询**。

| SID | name |
| --- | --- |
| S1 | 小林 |
| S2 | 小周 |
| S3 | 小陈 |

改成 `NOT EXISTS`得到 S4 小吴。内层若漏写 `t.SID=s.SID`，会变成“整个选课表是否非空”，四个学生都被保留。

<a id="ch03-s037"></a>

### 9.4 双重 NOT EXISTS：把“所有”变成“没有缺项”

**背景**：学校指定必选课 C1、C2，另建教学用表 `required(CID)`，两行分别 C1、C2。目标是找两门都选过的人，不要求只能选这两门。

| 学生 | 是否缺 C1 | 是否缺 C2 | 是否合格 |
| --- | --- | --- | --- |
| S1 | 否 | 否 | 是 |
| S2 | 否 | 是 | 否 |
| S3 | 是 | 否 | 否 |
| S4 | 是 | 是 | 否 |

先说“找不到一门必选课，是这个学生没有选过的”，再写：

```sql
SELECT s.SID,s.name FROM student AS s
WHERE NOT EXISTS (
    SELECT 1 FROM required AS r
    WHERE NOT EXISTS (
        SELECT 1 FROM takes AS t
        WHERE t.SID=s.SID AND t.CID=r.CID
    )
);
```

从最内层读：找当前学生对当前必选课的选课记录；内层 NOT EXISTS 为真表示“这门缺了”；中层列出所有缺课；外层 NOT EXISTS 要求缺课名单为空。最终只有 S1 小林。

如果 required 是空表，每个人都没有缺课，所以四个学生都合格。这与第 02 章直接对 takes 做除法时只从已有选课的学生范围取候选者不同；候选范围必须先讲清。

<a id="ch03-s038"></a>

### 9.5 派生表与 WITH：给中间结果起名

**派生表**是 FROM 中由子查询产生的临时来源。下面先得到各课平均，再筛选：

```sql
SELECT x.CID,x.avg_score
FROM (
    SELECT CID,AVG(score) AS avg_score FROM takes GROUP BY CID
) AS x
WHERE x.avg_score>=75;
```

`x`是临时结果别名，结果仍为 C1 75、C2 75。也可写 **CTE**，即公共表表达式，用 `WITH`给同一语句内的中间结果命名：

```sql
WITH course_average AS (
    SELECT CID,AVG(score) AS avg_score FROM takes GROUP BY CID
)
SELECT CID,avg_score FROM course_average WHERE avg_score>=75;
```

`WITH`不会自动创建永久表，也不承诺物理上只计算一次。

<a id="ch03-s039"></a>

### 9.6 LATERAL 与 UNIQUE 谓词：课件扩展

`LATERAL`允许 FROM 中某个子查询使用其左侧来源的当前行。**场景**：给每个学生统计选课数，可概念性写：

```sql
SELECT s.SID,x.n
FROM student AS s,
LATERAL (SELECT COUNT(*) AS n FROM takes AS t WHERE t.SID=s.SID) AS x;
```

对 S1 算 2，对 S2、S3 算 1，对 S4 算 0，结果如下：

| SID | n |
| --- | --- |
| S1 | 2 |
| S2 | 1 |
| S3 | 1 |
| S4 | 0 |

逗号在这里组合左来源与每行对应的侧向结果；若不允许相关引用，普通 FROM 子查询不能这样写。LATERAL 支持与替代语法取决于产品。

`UNIQUE (子查询)`是课件介绍的“结果是否没有重复”的谓词（用于判断条件是否成立的表达式），用途不同于建表的 UNIQUE 约束。例如查询 takes 的 SID 会出现 S1 两次，因此不能当成无重复名单。该谓词支持有限，空值比较也有标准细节；初学者可先掌握 DISTINCT 和明确的分组检查，不把此谓词当成通用可运行语法。


<a id="ch03-s040"></a>

## 10. 【课程总结PPT重点知识点】INSERT、DELETE、UPDATE 与 CASE

<a id="ch03-s041"></a>

### 10.1 INSERT：添加一条明确事实

**独立操作**：在原始数据上增加学生 S5 小赵，所在系为数学。
```sql
INSERT INTO student(SID,name,dept) VALUES ('S5','小赵','数学');
```
`INSERT INTO`指定目标表与列，`VALUES`后给同顺序的值。成功后学生表完整结果如下，不自动生成选课：

| SID | name | dept |
| --- | --- | --- |
| S1 | 小林 | 计算机 |
| S2 | 小周 | 数学 |
| S3 | 小陈 | 计算机 |
| S4 | 小吴 | 数学 |
| S5 | 小赵 | 数学 |

若 S5 已存在则违反主码。写出列名可以减少误把姓名写到系列的风险。

也可用 `INSERT INTO 目标表(列) SELECT ...`把查询结果逐行插入，输出结构、权限和约束仍须满足。

<a id="ch03-s042"></a>

### 10.2 DELETE：按条件删除行

**独立操作**：取消 S2 的 C1 选课。
```sql
DELETE FROM takes WHERE SID='S2' AND CID='C1';
```
`DELETE FROM`指定删除哪张表的行，WHERE 指定哪条。结果完整选课表如下；学生 S2 仍在学生表：

| SID | CID | score |
| --- | --- | --- |
| S1 | C1 | 80 |
| S1 | C2 | 90 |
| S3 | C2 | 60 |

省略 WHERE 会删除 takes 的全部行。这里讲解的是例题效果，不在真实数据库执行。

<a id="ch03-s043"></a>

### 10.3 UPDATE：改变已有行的值

**独立操作**：把原始数据里 S2 的 C1 成绩更正为 75。
```sql
UPDATE takes SET score=75 WHERE SID='S2' AND CID='C1';
```
`UPDATE`指定目标表，`SET`指定新值，WHERE 选择被改行。完整结果如下：

| SID | CID | score |
| --- | --- | --- |
| S1 | C1 | 80 |
| S1 | C2 | 90 |
| S2 | C1 | 75 |
| S3 | C2 | 60 |

不是新增一次选课，也不更改其他学生。

<a id="ch03-s044"></a>

### 10.4 CASE：逐行选用不同计算规则

**独立场景**：显示原始成绩对应的“达标／待提高”，不改数据。
```sql
SELECT SID,CID,
       CASE WHEN score>=80 THEN '达标'
            ELSE '待提高' END AS status
FROM takes;
```
`CASE`开始条件表达式；`WHEN`后是条件；`THEN`后是条件为真时的值；`ELSE`是其他情况；`END`结束。结果：

| SID | CID | status |
| --- | --- | --- |
| S1 | C1 | 达标 |
| S1 | C2 | 达标 |
| S2 | C1 | 待提高 |
| S3 | C2 | 待提高 |

若另有未知成绩，`score>=80`为未知，会走 ELSE；要区分未知应先写 `WHEN score IS NULL THEN '未公布'`。条件顺序有意义，第一个为真的分支生效。

<a id="ch03-s045"></a>

## 11. 【课程总结PPT重点知识点】视图与视图更新

> **本节为课程总结PPT明确列出的重点知识点：视图与可更新视图。**

<a id="ch03-s046"></a>

### 11.1 给一个查询结果长期起名

**目标**：教务员经常查计算机系学生，希望不用每次重写条件。**视图**是保存了查询定义的命名对象：

```sql
CREATE VIEW cs_student AS
SELECT SID,name,dept FROM student WHERE dept='计算机';
```

`CREATE VIEW`创建视图名称，`AS`后是它的定义。查询 `SELECT SID,name FROM cs_student;`，在原始数据上得到 S1 小林、S3 小陈。普通视图通常不独立存一份完整结果；它跟随基础表的变化。**物化视图**则存储计算结果并需刷新，支持和更新规则按产品确定。

视图可以简化查询、隐藏不需要的列，但访问隔离是否有效还要配合实际权限。

<a id="ch03-s047"></a>

### 11.2 为什么不是所有视图都能直接修改

如果视图只筛选一张基本表，每一行通常能明确对应原表的一行。若视图是 `CID,AVG(score)`，把 C1 的平均改成 85，究竟改小林、改小周还是都改？无法仅凭这个值唯一决定。

这就是**可更新性**问题：修改视图能否确定地转成对基础表的修改。包含聚集、分组、去重、集合组合的视图通常不可按简单规则更新；某些产品支持部分连接视图或专门的触发器机制，需按产品核实。

<a id="ch03-s048"></a>

### 11.3 WITH CHECK OPTION 防止改完跑出视图

给计算机系学生视图加 `WITH CHECK OPTION`，意思是通过视图插入或修改后仍须满足它的筛选条件。否则把 S1 的系改成数学，操作后 S1 会从该视图消失。该选项阻止这种违反视图条件的变更，不代表禁止基础表经其他合法入口修改；嵌套视图的 LOCAL／CASCADED 范围需看定义。

<a id="ch03-s049"></a>

## 12. 【课程PPT补充知识点】SQL 中的事务边界

**事务**是作为整体完成的一组操作。仍用独立银行场景：甲 500、乙 300，转 200，两个修改应一起成功。

```sql
START TRANSACTION;
UPDATE transfer_account SET balance=balance-200 WHERE owner='甲';
UPDATE transfer_account SET balance=balance+200 WHERE owner='乙';
COMMIT;
```

这里另有教学表 `transfer_account(owner,balance)`：`owner`是账户所有者，`balance`是余额，两行分别甲 500、乙 300，不是第 1 节学校数据。

`START TRANSACTION`开始事务，`COMMIT`提交整体结果；失败时 `ROLLBACK`撤销事务。成功后甲 300、乙 500；整体撤销后甲 500、乙 300。应用必须检查账户存在、扣款余额足够及修改行数等，SQL 语句执行成功不等于业务必然正确。

**自动提交**表示某些环境默认每条语句自己构成事务；若此时两条 UPDATE 分别提交，就不能靠后来回滚撤销已提交的第一条。事务开始语法、自动提交设置和 DDL 事务行为需看产品。原理见第 06 章。

<a id="ch03-s050"></a>

## 13. 【课程PPT补充知识点，模拟题相关】用户定义类型与域

<a id="ch03-s051"></a>

### 13.1 为同样的文字表示赋予不同身份

**背景**：学号和课程号都可能是短文字，但把 C1 当学号传入可能是程序错误。**用户定义类型**可以定义具有独立身份的新类型，强调“底层一样也未必允许混用”。

```sql
CREATE TYPE StudentId AS VARCHAR(10) FINAL;
```

这是课程所用标准风格的类型示例：`StudentId`是新类型名，`AS VARCHAR(10)`给出底层表示，`FINAL`在该标准语境中表示不能再作为可继承的父类型。具体产品可能不支持这套语法或采用别的类型体系。

**强类型检查**意思是系统更严格地检查类型身份匹配；不是保证任意程序逻辑正确。

<a id="ch03-s052"></a>

### 13.2 域是在既有类型上加规则

**背景**：多张表都需要合法成绩，想复用 0—100 规则。
```sql
CREATE DOMAIN Score AS NUMERIC(5,2)
CHECK (VALUE>=0 AND VALUE<=100);
```
`DOMAIN`是域，`Score`为域名，`VALUE`代表待检查的值。用作列类型后，110 不符合此范围。未另加非空时，NULL 的 CHECK 仍遵循未知处理。

域侧重已有类型上的约束；独立类型侧重类型身份。参考答案“类型无法定义约束、域弱检查”应限定在课件区分的语境，不能当成所有 DBMS 的通用结论。

<a id="ch03-s053"></a>

## 14. 【课程总结PPT重点知识点】权限、角色与授权传播

<a id="ch03-s054"></a>

### 14.1 让教师能查但不能任意改表

**背景**：教师账号 `teacher_user`需要读 course，不应修改学生身份。
```sql
GRANT SELECT ON course TO teacher_user;
REVOKE SELECT ON course FROM teacher_user;
```
`GRANT`授予权限，`SELECT ON course`表示读这张表，`TO`指明接收者；`REVOKE`撤回，`FROM`指明被撤回者。两条是分别展示的动作，不是要求立即授予再撤回。

权限还可包括 INSERT、UPDATE、DELETE、REFERENCES 等；列级权限用于限制可以修改哪些列。管理员权限、对象所有者权限和普通账号权限需分别管理。

<a id="ch03-s055"></a>

### 14.2 角色减少重复授权

`CREATE ROLE teacher_role;`创建“教师角色”，`GRANT SELECT ON course TO teacher_role;`给角色权限，再把角色授给具体账号。**角色**是一组权限的可命名集合，不等同于一个人。用户可能加入多个角色；实际启用与继承方式按产品确定。

<a id="ch03-s056"></a>

### 14.3 WITH GRANT OPTION 与授权图

**授权选项** `WITH GRANT OPTION`允许接收者再把收到的权限授给他人。设表拥有者 O 授权给甲，甲再授给乙，可画成 `O → 甲 → 乙`；箭头表示授权来源，不是数据流。

若甲的授权来源被撤回，乙从甲得到的权限可能随之级联撤回；若乙还直接从 O 得到同一权限，通常需考虑另一条有效路径。`CASCADE`表示传播撤回，`RESTRICT`表示遇到依赖时阻止撤回，具体可用语法与多路径规则要按产品核实。不能简单认为“撤回甲就必然使乙失去所有同类权限”。

<a id="ch03-s057"></a>

## 15. 【课程PPT补充知识点】程序怎样安全调用 SQL

<a id="ch03-s058"></a>

### 15.1 JDBC、ODBC 与结果集

**背景**：学生在网页输入学号，应用要查询对应姓名。**API**是供程序调用的一组接口。JDBC 是 Java 的数据库连接接口；ODBC 是另一种通用数据库访问接口。**连接**在这里指程序与数据库之间的会话，不是第 5 节拼表的 JOIN。

典型步骤：建立连接，创建或准备语句，绑定学号，执行，读取**结果集**（查询返回的行集合），最后释放资源。结果集本例一行 `S1,小林`；未找到学生时可以是零行。

<a id="ch03-s059"></a>

### 15.2 参数化语句与 SQL 注入

安全的参数化概念形式：
```sql
SELECT SID,name FROM student WHERE SID=?;
```
`?`在 JDBC 预编译语句中是参数占位符，不是 SQL 里可随意直接执行的问号。应用调用绑定方法传入 S1，把它作为值。

**SQL 注入**是把不可信输入直接拼接到语句文本里，使输入中的符号变成 SQL 结构。参数化把语句结构与值分开；不应把“先编译了一次”误认为任意拼接都安全。参数通常不能替代表名、列名；动态选择对象需限定允许的名称。

**预编译语句**是提前准备并反复绑定值执行的语句对象，是否复用执行计划、性能收益多少取决于软件。

<a id="ch03-s060"></a>

### 15.3 嵌入式、动态 SQL 与元数据

**嵌入式 SQL**把 SQL 写在宿主语言源码中，由相关工具处理；**宿主语言**是包围 SQL 的程序语言。**动态 SQL**在程序运行时构造或准备语句，适合查询结构会变化的情况。SQLJ 是课件介绍的 Java 嵌入式 SQL 方案，支持需按环境确认。

**元数据**是描述数据的资料，例如返回列名称、类型和数量。应用可以通过元数据知道结果怎么显示，而不是一律假定查询只有姓名一列。

<a id="ch03-s061"></a>

## 16. 【课程PPT补充知识点，模拟题相关】函数、过程与触发器

<a id="ch03-s062"></a>

### 16.1 先用不同任务分清调用方式

**独立背景**：学校想复用学分换算，并记录每次成绩变更。

- **函数**像可重复调用的计算规则：输入学分 3，返回 `3×16=48` 学时。通常用于表达式，有返回值。
- **过程**封装一段业务动作，例如处理一次成绩更正、检查权限、登记原因；一般由程序显式调用。
- **触发器**绑定数据库事件，例如 takes 的 score 被修改后自动写一条变更记录，无须应用每次显式调用。

三者都可能存放在数据库中，具体调用、返回类型与事务限制有产品差异。“触发器无返回值”在答题中表示它通常不是查询表达式里手工调用取值的函数，不能推广成所有产品都无返回机制。

<a id="ch03-s063"></a>

### 16.2 触发器需要说清四件事

设独立教学审计表 `score_audit(SID,CID,old_score,new_score)`：一行记一次更正，最后两列分别旧成绩、新成绩。把 S2 C1 从 70 改为 75 后，触发器预期写入 `S2,C1,70,75`。

设计需说明：作用表 takes；事件 UPDATE；时机 BEFORE（之前）或 AFTER（之后）；按每行或按整条语句触发。旧行、新行如何引用、触发器完整代码按产品不同，本例用动作说明而不混用某款产品的语法。

能用 CHECK 表达“成绩不得超过 100”的地方优先用约束。触发器适合附加动作，但多个触发器相互引发可能使处理过程难理解。

<a id="ch03-s064"></a>

### 16.3 表函数与外部例程

**标量函数**返回一个值；**表函数**返回行列组成的表，例如返回某学生全部选课，可作为查询来源。

**外部例程**由 Java、C 等 SQL 之外的语言实现，再由数据库调用。它可能完成 SQL 本身不方便表达的任务，也带来类型转换、权限和故障隔离的问题。这里没有指定 DBMS，不提供声称跨产品通用的外部例程部署代码。

<a id="ch03-s065"></a>

## 17. 【课程PPT补充知识点】递归查询：不断沿先修关系往前找

<a id="ch03-s066"></a>

### 17.1 先说明新的业务与数据

这是独立先修课程场景。`prereq(course_id,prereq_id)`每行表示第一门课直接要求先学第二门课；编号 A、B、C 是课程代号，不是学生学号。

| course_id | prereq_id |
| --- | --- |
| A | B |
| B | C |

问题：除了直接先修，还要列出间接先修。手工先知道 A 要 B，B 要 C，因此 A 也间接要 C，最终 A B、B C、A C。

<a id="ch03-s067"></a>

### 17.2 从一轮到多轮组成表达式

```sql
WITH RECURSIVE prereq_path(course_id,prereq_id) AS (
    SELECT course_id,prereq_id FROM prereq
    UNION
    SELECT p.course_id,q.prereq_id
    FROM prereq_path AS p
    JOIN prereq AS q ON p.prereq_id=q.course_id
)
SELECT course_id,prereq_id FROM prereq_path;
```

`RECURSIVE`表明公共表表达式允许引用自身。第一段是**基础项**，产生 A B、B C；第二段是**递归项**，把已知先修继续接到下一门，新增 A C；第三轮没有新配对，结束。`UNION`去重，避免同一配对重复增加。最终：

| course_id | prereq_id |
| --- | --- |
| A | B |
| B | C |
| A | C |

这种把可沿路径到达的配对全部列出的结果叫**传递闭包**，本例表示“直接或间接需要”。若用 UNION ALL 或记录整条路径，遇到环可能不停生成新行，需额外终止或防环规则。递归关键字、限制和环检测支持按产品确定。

<a id="ch03-s068"></a>

## 18. 【课程PPT补充知识点】多级汇总、窗口与 OLAP

<a id="ch03-s069"></a>

### 18.1 另一个业务：学校用品销售

这是独立教学数据 `sales(year,region,amount)`，每行是一笔销售。`year`年份，`region`地区，`amount`金额，均非空。

| year | region | amount |
| --- | --- | --- |
| 2025 | 东区 | 10 |
| 2025 | 西区 | 20 |
| 2026 | 东区 | 30 |

**维度**是分析分类角度，例如年份、地区；**度量**是汇总的数字，例如金额。

<a id="ch03-s070"></a>

### 18.2 ROLLUP、CUBE 与 GROUPING SETS

`GROUP BY ROLLUP(year,region)`依次按“年与地区”“年”“全部”汇总。`ROLLUP`意为沿层次形成小计：

| 年份显示 | 地区显示 | SUM(amount) | 含义 |
| --- | --- | --- | --- |
| 2025 | 东区 | 10 | 明细分组 |
| 2025 | 西区 | 20 | 明细分组 |
| 2026 | 东区 | 30 | 明细分组 |
| 2025 | 全部地区 | 30 | 年小计 |
| 2026 | 全部地区 | 30 | 年小计 |
| 全部年份 | 全部地区 | 60 | 总计 |

真实查询通常在汇总所省略维度处输出 NULL；文中“全部”是解释标签，不是自动返回文字。`GROUPING(列)`可指示这一列是否因汇总被省略，避免把实际 NULL 与汇总标记混淆。

`CUBE(year,region)`还加入“只按地区”两行：东区 40、西区 20，总共八行。`CUBE`考察各维度组合，不只沿一种层次。

`GROUPING SETS ((year,region),(year),())`显式列出所需分组，空括号 `()`表示全体一组，与上面 ROLLUP 的分组集合相同。三种高级语法支持情况按产品确认。

<a id="ch03-s071"></a>

### 18.3 窗口函数不把明细压成一行

**目标**：每条选课旁显示全体平均分与成绩排名，仍保留四条选课。

```sql
SELECT SID,CID,score,
       AVG(score) OVER () AS overall_avg,
       RANK() OVER (ORDER BY score DESC) AS rank_no
FROM takes;
```

`OVER`指定计算窗口，`()`表示以全体作为窗口；`RANK`按给定顺序排名。这里没有并列：

| SID | CID | score | overall_avg | rank_no |
| --- | --- | --- | --- | --- |
| S1 | C2 | 90 | 75 | 1 |
| S1 | C1 | 80 | 75 | 2 |
| S2 | C1 | 70 | 75 | 3 |
| S3 | C2 | 60 | 75 | 4 |

`OVER`里面的排序用于计算名次，并不保证最终显示顺序；需要固定显示顺序仍应在整个查询末尾加 ORDER BY。

`PARTITION BY CID`表示先按课程分区、每区单独计算。**分区**在此指计算范围，不是物理分区表。`RANK`遇并列会跳号，`DENSE_RANK`不跳号；例如独立成绩 90、90、80 分别排 1、1、3 与 1、1、2。

**窗口范围**还可限制到当前行之前的一部分。累计金额可以写 `SUM(amount) OVER (ORDER BY year,region ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`。`ROWS`按行界定，`UNBOUNDED PRECEDING`是从最前一行，`CURRENT ROW`是到当前行。销售例按所示顺序累计为 10、30、60；若排序列不唯一，需补唯一编号才能确定逐行累计顺序。

<a id="ch03-s072"></a>

### 18.4 OLAP 的几种动作

OLAP 是联机分析处理，侧重从不同维度观察大量数据。以销售例解释：

- **切片**：只看 2025，剩东区 10、西区 20。
- **切块**：限定多个维度的范围，例如只看 2025—2026 且只看东区，剩 10、30。
- **上卷**：从各地区明细汇到全年金额，2025 为 30、2026 为 30。
- **下钻**：从全年金额展开到地区明细。

这些是分析操作的含义，不是四个在每个 DBMS 都同名的 SQL 关键字。

<a id="ch03-s073"></a>

## 19. 常见误解与排查顺序

| 现象 | 先检查什么 | 本章对应例子 |
| --- | --- | --- |
| 连接少了一条跨系选课 | 是否自然连接误用了 dept | 小周的 C1 |
| 平均分变高 | WHERE 是否先去掉低分 | 75 被算成 80／90 |
| 没选课的人不见了 | 外连接后的 WHERE 是否筛掉 NULL | S4 |
| NOT IN 什么也查不到 | 内层是否含 NULL | 未识别学号 |
| 分组显示随意一个姓名 | 非聚集列是否由组唯一决定 | 同课多人 |
| 更新结果有歧义 | 视图行能否映射到基础行 | 平均成绩视图 |
| 程序输入改变查询结构 | 是否把输入直接拼进 SQL | 参数化查询 |


<a id="ch03-s074"></a>

## 20. 本单元模拟题

<a id="ch03-s075"></a>

### 题目一：`VARCHAR` 与 `CHAR`

**原题**

> 简述 varchar 与 char 的区别。

**PPT 参考答案**

> char 是一种固定长度的字符类型，varchar 则是一种可变长度的字符类型。

**规范答案与解析**

`CHAR(n)` 表示固定长度字符串，短值通常以空格补足到 `n`；`VARCHAR(n)` 表示最大长度为 `n` 的可变长度字符串，只保存实际长度及必要的长度信息。固定格式、长度稳定的数据可考虑 `CHAR`，长度差异较大的文本通常使用 `VARCHAR`。具体存储和比较细节因 DBMS 而异。

<a id="ch03-s076"></a>

### 题目二：LIKE 查询

<a id="ch03-s077"></a>

#### 先看教学名单与手工匹配

原题列名是 `ID`，本章主例列名是 `SID`，作答保留原题 ID。为观察匹配效果，另设**教学用**名单：`ID`为学号，`name`为英文姓名，一行一位学生。

| ID | name |
| --- | --- |
| U1 | Wang |
| U2 | Li |
| U3 | Zhang |

手工找字符 g，Wang 与 Zhang 有，Li 无；`'%g%'`允许 g 两边任意文字。原题查询的完整结果：

| ID | name |
| --- | --- |
| U1 | Wang |
| U3 | Zhang |

本例只用小写 g，不据此推断数据库对 G 的大小写比较规则。


**原题**

> 在大学数据库中，用 SQL 语句查询名字中包含“g”的学生的学号、姓名。

**PPT 参考答案**

```sql
Select ID, name from student where name like '%g%';
```

**规范答案**

```sql
SELECT ID, name
FROM student
WHERE name LIKE '%g%';
```

两个 `%` 分别允许 `g` 前后出现任意长度字符串。大小写是否敏感取决于数据库及排序规则。

<a id="ch03-s078"></a>

### 题目三：函数和触发器

**原题**

> 简述函数和触发器之间的异同。

**PPT 参考答案**

> 函数和触发器都是存储在数据库当中的一段代码。差别是函数需要显式调用，有返回值；触发器需要有触发事件，系统自动调用，无返回值。

**校正与补充**

共同点是两者都可由数据库保存和执行，能够访问数据并封装逻辑。函数通常由查询、过程或应用显式调用，并返回标量或表。触发器绑定表、视图或数据库事件，由系统自动触发，通常不作为表达式返回值使用。不同 DBMS 对返回方式和触发器功能的细节不同，因此“触发器绝对没有任何返回机制”不宜理解为跨系统的完整定义。

<a id="ch03-s079"></a>

### 题目四：DISTINCT

**原题**

> distinct 的作用是什么？

**PPT 参考答案**

> 删除查询结果中的重复记录。

**规范答案与解析**

`DISTINCT` 在 `SELECT` 结果上消除重复行。它不会删除基本表中的数据，只影响当前查询结果，并对整个选择列表的组合去重。

<a id="ch03-s080"></a>

### 题目五：用户定义类型和域

**原题**

> 简述用户自定义的类型和域之间的差别。

**PPT 参考答案**

> 类型是强类型检查，无法定义约束；域是弱类型检查，可以定义约束。

**校正与补充**

用户定义类型通常具有独立的类型身份，不同类型即使底层表示相同，也不能随意比较或赋值，因此强调强类型检查。域建立在已有类型上，可附加默认值和约束，通常与基础类型更容易互操作。PPT 的表述反映课件所用 SQL 标准语境；具体 DBMS 是否支持类型约束以及隐式转换规则可能不同。

<a id="ch03-s081"></a>

### 题目六：银行数据库综合应用

<a id="ch03-s082"></a>

#### 先读懂银行业务和教学数据

银行有多个分行；一个分行管理多个账户与贷款；客户可有多个账户，一个账户也可由多个客户共同持有。贷款也可有多名借款人。因此 depositor 与 borrower 分别记录“谁持有哪个账户”“谁借哪笔贷款”，不能只在账户或贷款表中放一个姓名。

下表逐个解释原题字段。原题采用连字符；代码改用下划线，含义不变。“主码”是唯一且非空的行标识，“外码”是指向另一表行的列。转成文字后原题下划线标记不完整，以下采用与课件参考结构及关联一致的通常设计：分行名、客户名、贷款号、账户号各唯一，两张对应表用组合主码。

| 表 | 每行代表什么 | 各字段含义 |
| --- | --- | --- |
| branch | 一个分行 | branch_name 分行名；branch_city 所在城市；assets 资产总额 |
| customer | 一位客户 | customer_name 姓名；customer_street 街道；customer_city 居住城市 |
| loan | 一笔贷款 | loan_number 贷款号；branch_name 所属分行；amount 贷款金额 |
| borrower | 一位客户借一笔贷款 | customer_name 客户姓名；loan_number 贷款号 |
| account | 一个存款账户 | account_number 账户号；branch_name 所属分行；balance 账户余额 |
| depositor | 一位客户持有一个账户 | customer_name 客户姓名；account_number 账户号 |

以下**教学用数据**与第 02 章相同，金额均已知非空；客户姓名唯一是原题假设，真实系统通常采用客户编号。

| branch_name | branch_city | assets |
| --- | --- | --- |
| Brighton | 海城 | 1000000 |
| Riverside | 河城 | 2000000 |

| customer_name | customer_street | customer_city |
| --- | --- | --- |
| 张三 | 松林路 | 海城 |
| 李四 | 校园路 | 海城 |
| 王五 | 河滨路 | 河城 |
| 赵六 | 花园路 | 河城 |

| loan_number | branch_name | amount |
| --- | --- | --- |
| L1 | Brighton | 2000 |
| L2 | Riverside | 5000 |

| customer_name | loan_number |
| --- | --- |
| 张三 | L1 |
| 王五 | L2 |
| 赵六 | L2 |

| account_number | branch_name | balance |
| --- | --- | --- |
| A1 | Brighton | 1000 |
| A2 | Brighton | 3000 |
| A3 | Riverside | 8000 |

| customer_name | account_number |
| --- | --- |
| 张三 | A1 |
| 李四 | A2 |
| 张三 | A3 |
| 李四 | A3 |

A3 是共同账户；它的余额不能因为有两位持有人就算两遍。各小问都从这套原始数据独立出发。


**原题**

> 已知银行企业的数据库由以下表组成：  
> ①分行表 `branch(branch-name, branch-city, assets)`  
> ②客户表 `customer(customer-name, customer-street, customer-city)`  
> ③贷款明细表 `loan(loan-number, branch-name, amount)`  
> ④客户贷款表 `borrower(customer-name, loan-number)`  
> ⑤存款明细表 `account(account-number, branch-name, balance)`  
> ⑥客户存款表 `depositor(customer-name, account-number)`  
> 注：带下划线的属性为主码，假设客户的名字不相同。  
> （1）用 SQL 语句创建表。  
> （2）使用关系代数和 SQL 语句找出在 Brighton 银行中有存款的所有客户的姓名、存款号和存款额。  
> （3）使用关系代数和 SQL 语句找出账户平均余额小于 5000 元的支行，显示支行名称及账户平均余额。  
> （4）使用关系代数和 SQL 语句找出所有在银行中有贷款但无账户的客户。  
> （5）使用关系代数和 SQL 语句对所有存款余额大于平均存款额的账户付 3% 的利息。

本单元讲解建表与 SQL 部分；关系代数部分见《第2单元 关系模型与关系代数》。

**原题所给关系**

```text
branch(branch-name, branch-city, assets)
customer(customer-name, customer-street, customer-city)
loan(loan-number, branch-name, amount)
borrower(customer-name, loan-number)
account(account-number, branch-name, balance)
depositor(customer-name, account-number)
```

下文将连字符改为下划线，因为未加引号的 `branch-name` 会被许多 DBMS 解释为减法表达式。

<a id="ch03-s083"></a>

#### （1）创建表

**先手工推导**

先建 branch、customer，再建引用 branch 的 loan、account，再建同时引用客户和业务记录的 borrower、depositor。否则某些 DBMS 会在建外码时发现被引用表尚不存在。

原答案的 `NUMERIC(16,2)`表示金额最多 16 位数字，其中两位小数；长度 15、20、40 等是参考设计选择，不是题面证明的业务上限。`PRIMARY KEY(customer_name,account_number)`允许张三拥有 A1、A3，也允许李四持有 A3，但同一“张三 A3”不能重复登记。

**再对照 SQL 表达**

**PPT 参考答案节选**

```sql
create table branch (
   branch-name char(15) primary key,
   branch-city char(30),
   assets numeric(16,2),
   primary key(branch-name)
);
```

**问题说明**：主码重复声明，且带连字符的标识符未引用。PPT 还只创建了六张表中的一张。

**规范答案**

```sql
CREATE TABLE branch (
    branch_name VARCHAR(15) PRIMARY KEY,
    branch_city VARCHAR(30),
    assets      NUMERIC(16, 2)
);

CREATE TABLE customer (
    customer_name   VARCHAR(40) PRIMARY KEY,
    customer_street VARCHAR(60),
    customer_city   VARCHAR(30)
);

CREATE TABLE loan (
    loan_number VARCHAR(20) PRIMARY KEY,
    branch_name VARCHAR(15) NOT NULL,
    amount      NUMERIC(16, 2) CHECK (amount >= 0),
    FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
);

CREATE TABLE borrower (
    customer_name VARCHAR(40),
    loan_number   VARCHAR(20),
    PRIMARY KEY (customer_name, loan_number),
    FOREIGN KEY (customer_name) REFERENCES customer(customer_name),
    FOREIGN KEY (loan_number) REFERENCES loan(loan_number)
);

CREATE TABLE account (
    account_number VARCHAR(20) PRIMARY KEY,
    branch_name    VARCHAR(15) NOT NULL,
    balance        NUMERIC(16, 2) NOT NULL,
    FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
);

CREATE TABLE depositor (
    customer_name  VARCHAR(40),
    account_number VARCHAR(20),
    PRIMARY KEY (customer_name, account_number),
    FOREIGN KEY (customer_name) REFERENCES customer(customer_name),
    FOREIGN KEY (account_number) REFERENCES account(account_number)
);
```

题目明确假设客户姓名不相同，所以可按题意把 `customer_name` 作为主码；实际系统更适合使用稳定的客户编号。

<a id="ch03-s084"></a>

#### （2）Brighton 分行存款客户

**先手工推导**

把 depositor 与 account 按账户号匹配的完整中间结果：

| customer_name | account_number | branch_name | balance |
| --- | --- | --- | --- |
| 张三 | A1 | Brighton | 1000 |
| 李四 | A2 | Brighton | 3000 |
| 张三 | A3 | Riverside | 8000 |
| 李四 | A3 | Riverside | 8000 |

`d`指 depositor，`a`指 account，`ON a.account_number=d.account_number`要求同一账户。WHERE 只留下 Brighton，SELECT 去掉分行列：

| customer_name | account_number | balance |
| --- | --- | --- |
| 张三 | A1 | 1000 |
| 李四 | A2 | 3000 |

**再对照 SQL 表达**

**PPT 参考答案（格式规范化）**

```sql
SELECT customer_name, depositor.account_number, balance
FROM depositor, account
WHERE depositor.account_number = account.account_number
  AND branch_name = 'Brighton';
```

**推荐写法**

```sql
SELECT d.customer_name, a.account_number, a.balance
FROM depositor AS d
JOIN account AS a ON a.account_number = d.account_number
WHERE a.branch_name = 'Brighton';
```

<a id="ch03-s085"></a>

#### （3）平均余额小于 5000 元的支行

**先手工推导**

先只对 account 分堆：Brighton 是 1000、3000，均值 2000；Riverside 是 8000，均值 8000。中间结果：

| branch_name | avg_balance |
| --- | --- |
| Brighton | 2000 |
| Riverside | 8000 |

HAVING 检查均值是否小于 5000，最终结果如下：

| branch_name | avg_balance |
| --- | --- |
| Brighton | 2000 |

不能先连接 depositor 再按分行求平均，共同账户会重复进入统计。本题不含没有账户的分行；若要列它们，应另用外连接并说明无账户时平均为 NULL。

**再对照 SQL 表达**

```sql
SELECT branch_name, AVG(balance) AS avg_balance
FROM account
GROUP BY branch_name
HAVING AVG(balance) < 5000;
```

PPT 此题答案正确。`HAVING` 筛选的是分组后的平均值。

<a id="ch03-s086"></a>

#### （4）有贷款但无账户的客户

**先手工推导**

| 借款人 | depositor 中是否有对应姓名 | NOT EXISTS 是否为真 |
| --- | --- | --- |
| 张三 | 有 | 否 |
| 王五 | 无 | 是 |
| 赵六 | 无 | 是 |

`b`为当前借款人，内层 `d.customer_name=b.customer_name`检查是否有同名存款关系。最终结果如下：

| customer_name |
| --- |
| 王五 |
| 赵六 |

DISTINCT 防止一个人借多笔贷款时输出多次；无账户不意味着余额恰好为零。

**再对照 SQL 表达**

**PPT 参考答案**

```sql
SELECT DISTINCT customer_name
FROM borrower
WHERE customer_name NOT IN (
    SELECT customer_name FROM depositor
);
```

**更稳健的写法**

```sql
SELECT DISTINCT b.customer_name
FROM borrower AS b
WHERE NOT EXISTS (
    SELECT 1
    FROM depositor AS d
    WHERE d.customer_name = b.customer_name
);
```

按题设 `customer_name` 为主码且非空时，PPT 写法可得到正确结果。`NOT EXISTS` 不受子查询结果含空值的陷阱影响，语义也更直接。

<a id="ch03-s087"></a>

#### （5）给高于平均余额的账户增加 3% 利息

**先手工推导**

原始账户均值 `(1000+3000+8000)÷3=4000`。比较原余额，只有 A3 大于 4000。3% 是每 100 元增加 3 元，故新余额为 `8000+8000×0.03=8240`。

| account_number | 原 balance | 是否加息 | 新 balance |
| --- | --- | --- | --- |
| A1 | 1000 | 否 | 1000 |
| A2 | 3000 | 否 | 3000 |
| A3 | 8000 | 是 | 8240 |

`SET balance=balance*1.03`右边用当前行原余额计算，左边指定要改的列。这里采用“按更新开始前原始均值判断”的题意，不在每改一行后重新决定阈值。

课程给出的目标表子查询写法表达这层意图。真实产品可能限制这类语法；CTE／派生表是否能合法固定结果需按具体 DBMS 核实。若应用先单独查出平均再更新，还必须用合适事务隔离避免其他事务夹入修改，不能把“两条 SQL”自动视为同一快照。

**再对照 SQL 表达**

```sql
UPDATE account
SET balance = balance * 1.03
WHERE balance > (SELECT AVG(balance) FROM account);
```

PPT 答案的核心逻辑正确。若 DBMS 限制更新目标表同时出现在子查询中，可先用 CTE 或派生表固定平均值；具体写法取决于数据库产品。



<a id="ch03-s088"></a>

## 21. 自拟自测题与逐步答案

以下四题为自拟题，每题均从第 1 节原始学校数据独立计算。

<a id="ch03-s089"></a>

### 21.1 哪些学生选了 C1 但没选 C2？

**思路**：C1 名单 S1、S2，C2 名单 S1、S3，左减右得 S2。要姓名再查 student。

```sql
SELECT s.SID,s.name FROM student AS s
WHERE EXISTS (SELECT 1 FROM takes AS t WHERE t.SID=s.SID AND t.CID='C1')
  AND NOT EXISTS (SELECT 1 FROM takes AS t WHERE t.SID=s.SID AND t.CID='C2');
```

第一个 EXISTS 保留 S1、S2；第二个排除 S1，最终一行 **S2 小周**。两个内层 t 分别属于各自子查询，不共用某一条选课行。

<a id="ch03-s090"></a>

### 21.2 找至少两条选课记录的学生

**手工**：S1 有两条，S2、S3 各一条，S4 零条。先按 SID 分组，再筛组计数。

```sql
SELECT SID,COUNT(*) AS n FROM takes
GROUP BY SID HAVING COUNT(*)>=2;
```

中间是 S1 2、S2 1、S3 1；最终 **S1 2**。WHERE COUNT(*)>=2 写在分组前没有这组统计值，不能这样替换。

<a id="ch03-s091"></a>

### 21.3 包含零选课学生，显示选课数

**步骤**：student 左连接 takes，S4 得一条补空行；按学生分组；只数真实 t.CID。

```sql
SELECT s.SID,s.name,COUNT(t.CID) AS n
FROM student AS s LEFT JOIN takes AS t ON s.SID=t.SID
GROUP BY s.SID,s.name;
```

| SID | name | n |
| --- | --- | --- |
| S1 | 小林 | 2 |
| S2 | 小周 | 1 |
| S3 | 小陈 | 1 |
| S4 | 小吴 | 0 |

COUNT(*) 会把 S4 的补空行算作 1，因此不符合本题目标。

<a id="ch03-s092"></a>

### 21.4 找全部计算机系开设课程都选过的学生

**背景**：这里“计算机系课程”指 course.dept，不指学生所在系。C1、C2 均为必检查范围。直接逐人查是否缺课，S1 无缺项，S2 缺 C2，S3 缺 C1，S4 都缺。

```sql
SELECT s.SID,s.name FROM student AS s
WHERE NOT EXISTS (
    SELECT 1 FROM course AS c WHERE c.dept='计算机'
      AND NOT EXISTS (
          SELECT 1 FROM takes AS t
          WHERE t.SID=s.SID AND t.CID=c.CID
      )
);
```

内层判断一门课缺不缺，外层要求没有缺的计算机课程。最终 **S1 小林**。若学校没有任何计算机课程，四个学生都满足这个“没有缺课”的条件；若业务要求至少选一门，还要额外写存在性条件。

<a id="ch03-s093"></a>

## 22. 复习路线

- [ ] 能从字段含义判断应该按什么列连接。
- [ ] 能逐行算 NULL 条件、NOT IN 与 NOT EXISTS。
- [ ] 能画出 GROUP BY 的每堆，分别使用 WHERE、HAVING。
- [ ] 能从内到外解释相关子查询与双重 NOT EXISTS。
- [ ] 能解释修改、视图、事务、授权的作用和边界。
- [ ] 能说清课件扩展语法的用途及产品差异。

表结构从何而来，继续读[第 04 章](04_ER模型与关系模式转换.md)；表为什么要拆分，读[第 05 章](05_关系数据库规范化.md)。

