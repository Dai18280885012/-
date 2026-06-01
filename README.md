# 📸 批量图片提取 & 相似度对比工具

一个强大的 Python 工具，可以从多种文档格式（DOCX、XLSX、PDF）中批量提取图片，并进行相似度对比和重复检测。

## ✨ 功能特性

### 1. 📦 图片提取
- ✅ **DOCX** (Word 文档) - 提取所有嵌入的图片
- ✅ **XLSX** (Excel 电子表格) - 提取所有工作表中的图片
- ✅ **PDF** (PDF 文档) - 提取所有页面中的图片
- 批量处理整个文件夹
- 自动重命名以避免冲突

### 2. 🔍 相似度对比
三种对比算法可选：

| 方法 | 说明 | 优点 | 缺点 |
|------|------|------|------|
| **hash** | 感知哈希 | 快速、内存占用少 | 精度一般 |
| **ssim** | 结构相似度 | 精度中等 | 速度中等 |
| **orb** | 特征匹配 | 精度最高 | 速度慢 |

### 3. 📊 输出报告
- JSON 格式的相似度报告
- 按相似度排序
- 清晰的图片配对信息

---

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 使用方法

#### 方法 1: 交互式运行

```bash
python main.py
```

#### 方法 2: 命令行直接运行

```bash
# 提取图片
python extract_images.py /path/to/documents extracted_images

# 对比相似度
python compare_images.py extracted_images similarity_report.json hash 0.8
```

---

## 📋 参数说明

### extract_images.py

```bash
python extract_images.py <input_folder> <output_folder>
```

### compare_images.py

```bash
python compare_images.py <image_folder> <output_report> <method> <threshold>
```

**方法**: hash (推荐), ssim, orb  
**阈值**: 0-1, 默认 0.8

---

## 🎯 使用场景

1. **去重检测** - 找出文件夹中的重复图片
2. **相似图片分类** - 对相似但不完全相同的图片分组
3. **文档管理** - 提取报告中的所有图表
4. **质量检查** - 识别文档中重复使用的图片

---

## ⚙️ 系统要求

- Python 3.7+
- Windows、macOS、Linux

---

## 📝 常见问题

**Q: 哪种对比方法最好?**  
A: hash (快速去重), ssim (平衡), orb (最精确)

**Q: 相似度阈值应该设置多少?**  
A: 0.9 (严格), 0.8 (推荐), 0.7 (中等), 0.5 (宽松)

---

## 📄 许可证

MIT License
