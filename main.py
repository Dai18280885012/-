#!/usr/bin/env python3
"""
Interactive main program for image extraction and similarity comparison
"""
import os
import sys
from extract_images import batch_extract_images
from compare_images import ImageComparator

def main():
    print("="*60)
    print("🎯 批量图片提取 & 相似度对比工具")
    print("="*60)
    
    # Step 1: Extract images
    input_folder = input("请输入文件夹路径 (包含 DOCX/XLSX/PDF): ").strip()
    
    if not os.path.exists(input_folder):
        print("✗ 文件夹不存在!")
        return
    
    output_folder = "extracted_images"
    print(f"\n📦 第一步: 提取图片...\n")
    batch_extract_images(input_folder, output_folder)
    
    # Step 2: Compare similarity
    print(f"\n📊 第二步: 对比图片相似度...\n")
    print("选择对比方法:")
    print("  1. hash (快速, 推荐用于去重)")
    print("  2. ssim (中等精度)")
    print("  3. orb (特征匹配, 最精确)")
    
    method_choice = input("请选择 (1-3): ").strip()
    method_map = {'1': 'hash', '2': 'ssim', '3': 'orb'}
    method = method_map.get(method_choice, 'hash')
    
    threshold = input("相似度阈值 (0-1, 默认 0.8): ").strip()
    threshold = float(threshold) if threshold else 0.8
    
    comparator = ImageComparator(output_folder)
    results = comparator.compare_all(threshold=threshold, method=method)
    
    print("\n✅ 全部完成!")
    print(f"📁 提取的图片位置: {output_folder}")
    print(f"📄 相似度报告: similarity_report.json")

if __name__ == "__main__":
    main()
