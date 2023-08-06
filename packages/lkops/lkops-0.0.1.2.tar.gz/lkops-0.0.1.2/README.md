# lk_ops
ticoAg
19990523ONLY

## statement

- The implementation of some open source **operators**, **modules** and **losses** is based on the principle of out of the box. 

- Each implementation should be attached with **application examples**, **sources** and **general principle descriptions**.

## structure

- conn
  - _redis.py: redis连接池示例
  - _mysql.py: 
    1. mysql单连接，查询，插入，更新，执行
    2. mysql连接池 执行
  - _neo4j.py: neo4j连接，执行cypher
- encode
  - relative_position_representation.py: torch相对位置编码
- tools
  - _threadpool.py: 线程池，异步机制
  - _count_neo4j.py: 图谱数据统计
  - _ecg_api_count.py: ecg调用统计
  - _export_kg_data_to_yml.py:: 导出图谱食材食谱数据到yml
  - modules.py: 计时装饰器, json number Encoder
- utils
  - Logger.py: devops logger配置


## Records
- 2022.11.07 14:03 update Logger.py
- 2022.11.09 17:52 定时任务