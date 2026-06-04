# 技术职业发展学习项目清单

> 一份为 IT审计师 和 数据分析师 设计的职业升级指南  
> 帮助你学习实战项目，为跳槽薪资更高的公司做准备

**最后更新**: 2026-06-04  
**作者**: GitHub Copilot

---

## 📋 目录

- [IT审计师学习路线](#it审计师学习路线)
- [数据分析师学习路线](#数据分析师学习路线)
- [快速开始](#快速开始)
- [薪资提升预期](#薪资提升预期)

---

# IT审计师学习路线

## 核心价值

IT审计师需要掌握的能力：
- 🔒 系统安全审计与合规性检查
- 📊 日志管理与审计
- 🔐 访问控制与权限管理
- ☁️ 云安全审计
- 🚨 安全监控与告警

---

## 第一层：AI驱动的代码与安全审计（推荐从这里开始）

### 1. DeepAudit - AI代码安全审计平台 ⭐⭐⭐

| 项目 | DeepAudit |
|------|-----------|
| GitHub | https://github.com/lintsinghua/DeepAudit |
| Star | 2000+ |
| 语言 | Python |

**核心功能**：
- 自动发现CVE漏洞（已发现49个CVE）
- 生成合规报告
- 多Agent协作审计
- 沙箱验证

---

### 2. XCodeReviewer - AI代码审计工具 ⭐⭐⭐

| 项目 | XCodeReviewer |
|------|---------------|
| GitHub | https://github.com/lintsinghua/XCodeReviewer |
| Star | 1500+ |

---

### 3. Ai_SATS-tools - 代码安全分析平台 ⭐⭐

| 项目 | Ai_SATS-tools |
|------|----------------|
| GitHub | https://github.com/qwert419/Ai_SATS-tools |

---

## 第二层：日志审计与安全监控（核心审计能力）

### 4. Wazuh - 企业级安全监控平台 ⭐⭐⭐ 必学

| 项目 | Wazuh |
|------|-------|
| GitHub | https://github.com/wazuh/wazuh |
| 官网 | https://wazuh.com/ |
| Star | 7000+ |

**快速开始**：
```bash
docker run -d --name=wazuh -p 1514:1514 -p 1515:1515 -p 514:514/udp -p 55000:55000 wazuh/wazuh:latest
```

---

### 5. ELK Stack - 日志采集分析平台 ⭐⭐⭐ 业界标准

| 项目 | ELK Stack |
|------|-----------|
| GitHub | https://github.com/elastic/elasticsearch |
| 官网 | https://www.elastic.co/elastic-stack |

---

### 6. Graylog - 日志管理与实时分析 ⭐⭐

| 项目 | Graylog |
|------|---------|
| GitHub | https://github.com/Graylog2/graylog2-server |

---

### 7. Linux auditd - 系统审计工具 ⭐⭐⭐

| 项目 | auditd |
|------|--------|
| GitHub | https://github.com/linux-audit/audit-userspace |

---

## 第三层：访问控制与身份管理（权限审计）

### 8. Keycloak - IAM身份与访问管理 ⭐⭐⭐

| 项目 | Keycloak |
|------|----------|
| GitHub | https://github.com/keycloak/keycloak |
| Star | 20000+ |

---

### 9. Open Policy Agent (OPA) - 策略引擎 ⭐⭐

| 项目 | OPA |
|------|-----|
| GitHub | https://github.com/open-policy-agent/opa |

---

### 10. GitHub-Audit - GitHub组织审计 ⭐⭐

| 项目 | GitHub-Audit |
|------|--------------|
| GitHub | https://github.com/MozillaServices/github-audit |

---

## 第四层：云安全审计（高薪方向）

### 11. CloudQuery - 多云资源审计 ⭐⭐⭐

| 项目 | CloudQuery |
|------|-----------|
| GitHub | https://github.com/cloudquery/cloudquery |

---

### 12. StreamAlert - 实时安全分析框架 ⭐⭐

| 项目 | StreamAlert |
|------|-------------|
| GitHub | https://github.com/airbnb/streamalert |

---

### 13. Falco - 容器运行时安全 ⭐⭐

| 项目 | Falco |
|------|-------|
| GitHub | https://github.com/falcosecurity/falco |

---

## 📅 IT审计师学习路线图

### 第1阶段（1-2个月）：基础审计能力

**学习顺序**：
1. Linux auditd
2. ELK Stack
3. Graylog
4. Wazuh

### 第2阶段（2-3个月）：代码与合规审计

**学习顺序**：
1. SonarQube
2. DeepAudit
3. XCodeReviewer

### 第3阶段（3-4个月）：权限与身份审计

**学习顺序**：
1. Keycloak
2. OPA
3. GitHub-Audit

### 第4阶段（4-6个月）：云安全审计

**学习顺序**：
1. CloudQuery
2. StreamAlert
3. Wazuh多云配置

---

# 数据分析师学习路线

## 核心价值

数据分析师需要掌握的能力：
- 📊 数据可视化与BI工具
- 🐼 数据处理与清洗
- 🤖 机器学习与数据挖掘
- 🏗️ 大数据处理平台
- 🔄 数据集成与ETL

---

## 第一层：数据可视化与BI工具（入门必学）

### 1. DataEase - 开源BI工具 ⭐⭐⭐ 强烈推荐

| 项目 | DataEase |
|------|----------|
| GitHub | https://github.com/dataease/dataease |
| 官网 | https://dataease.io/ |
| Star | 20000+ |

**快速开始**：
```bash
docker run -d --name dataease -p 8081:8081 dataease/dataease:latest
# 访问 http://localhost:8081
```

---

### 2. Apache Superset - 企业级BI平台 ⭐⭐⭐

| 项目 | Superset |
|------|----------|
| GitHub | https://github.com/apache/superset |
| Star | 60000+ |

---

### 3. Metabase - 易用数据分析工具 ⭐⭐

| 项目 | Metabase |
|------|----------|
| GitHub | https://github.com/metabase/metabase |
| Star | 37000+ |

---

### 4. Grafana - 时间序列可视化 ⭐⭐

| 项目 | Grafana |
|------|---------|
| GitHub | https://github.com/grafana/grafana |
| Star | 62000+ |

---

## 第二层：数据处理与分析（核心技能提升）

### 5. Pandas - 数据分析基础库 ⭐⭐⭐ 必学

| 项目 | Pandas |
|------|--------|
| GitHub | https://github.com/pandas-dev/pandas |
| 官网 | https://pandas.pydata.org/ |

**快速开始**：
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.head()
df.info()
df.groupby('category').sum()
```

---

### 6. Scikit-learn - 机器学习库 ⭐⭐⭐ 必学

| 项目 | Scikit-learn |
|------|--------------|
| GitHub | https://github.com/scikit-learn/scikit-learn |
| Star | 58000+ |

**快速开始**：
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)
```

---

### 7. PyCaret - 自动化ML库 ⭐⭐

| 项目 | PyCaret |
|------|---------|
| GitHub | https://github.com/pycaret/pycaret |

---

### 8. Yellowbrick - ML可视化 ⭐

| 项目 | Yellowbrick |
|------|-------------|
| GitHub | https://github.com/DistrictDataLabs/yellowbrick |

---

## 第三层：大数据处理（薪资跳升）

### 9. Apache Spark - 大数据引擎 ⭐⭐⭐ 高薪必学

| 项目 | Spark |
|------|-------|
| GitHub | https://github.com/apache/spark |
| 官网 | https://spark.apache.org/ |
| Star | 39000+ |

**快速开始**：
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("demo").getOrCreate()
df = spark.read.csv("data.csv", header=True)
df.groupBy("category").sum().show()
```

---

### 10. Apache Hadoop - 分布式系统 ⭐⭐

| 项目 | Hadoop |
|------|--------|
| GitHub | https://github.com/apache/hadoop |

---

### 11. ClickHouse - OLAP数据库 ⭐⭐⭐

| 项目 | ClickHouse |
|------|-----------|
| GitHub | https://github.com/ClickHouse/ClickHouse |
| Star | 33000+ |

---

### 12. Delta Lake - 数据湖存储 ⭐⭐

| 项目 | Delta Lake |
|------|-----------|
| GitHub | https://github.com/delta-io/delta |

---

## 第四层：数据集成与ETL

### 13. Airbyte - 数据集成平台 ⭐⭐⭐

| 项目 | Airbyte |
|------|---------|
| GitHub | https://github.com/airbytehq/airbyte |
| Star | 14000+ |

---

### 14. Apache NiFi - 数据流平台 ⭐⭐

| 项目 | NiFi |
|------|------|
| GitHub | https://github.com/apache/nifi |

---

### 15. SQLFlow - SQL+ML ⭐

| 项目 | SQLFlow |
|------|---------|
| GitHub | https://github.com/sql-machine-learning/sqlflow |

---

## 数据分析师学习路线图

### 第1阶段（0-2个月）：BI + Python基础

1. DataEase 或 Metabase
2. Pandas
3. Scikit-learn 基础

### 第2阶段（2-4个月）：数据挖掘升级

1. Scikit-learn 进阶
2. PyCaret
3. Yellowbrick
4. Kaggle竞赛

### 第3阶段（4-6个月）：大数据跳升

1. Apache Spark
2. ClickHouse
3. Delta Lake

### 第4阶段（6-9个月）：完整数据平台

1. Airbyte
2. Apache Superset
3. SQLFlow

---

## 📈 薪资提升预期

| 技能等级 | 掌握项目 | 薪资增长 | 工作年限 |
|---------|--------|--------|--------|
| 初级 | DataEase + Pandas | 基础 | 0-1年 |
| 中级 | + Scikit-learn | +20-30% | 1-2年 |
| 高级 | + Spark + ClickHouse | +50-100% | 2-4年 |
| 资深 | + 完整平台 | +100%+ | 4年+ |

---

# 🚀 快速开始

## IT审计师

```bash
# 快速部署Wazuh
docker run -d --name=wazuh -p 1514:1514 -p 1515:1515 -p 514:514/udp -p 55000:55000 wazuh/wazuh:latest
```

## 数据分析师

```bash
# 快速部署DataEase
docker run -d --name dataease -p 8081:8081 dataease/dataease:latest
```

---

## 推荐资源

- **Coursera**: https://www.coursera.org
- **Kaggle**: https://www.kaggle.com
- **Awesome Python**: https://github.com/vinta/awesome-python

---

**祝你学习进展顺利！💪**

**更新时间**: 2026-06-04
