import os
import sys
from docx import Document
from openpyxl import load_workbook
import fitz  # PyMuPDF
from PIL import Image
import io

def extract_images_from_docx(docx_path, output_folder):
    """从DOCX文件提取图片"""
    try:
        doc = Document(docx_path)
        rels = doc.part.rels
        count = 0
        for rel_id in rels:
            rel = rels[rel_id]
            if "image" in rel.target_ref:
                img_data = rel.target_part.blob
                img_name = rel.target_ref.split("/")[-1]
                output_path = os.path.join(output_folder, f"docx_{os.path.basename(docx_path).replace('.docx', '')}_{img_name}")
                with open(output_path, "wb") as f:
                    f.write(img_data)
                count += 1
                print(f"✓ 已提取: {output_path}")
        return count
    except Exception as e:
        print(f"✗ 提取 DOCX 失败: {e}")
        return 0

def extract_images_from_xlsx(xlsx_path, output_folder):
    """从XLSX文件提取图片"""
    try:
        wb = load_workbook(xlsx_path)
        count = 0
        for ws in wb.worksheets:
            for image in ws._images:
                img_data = image.image.blob
                img_name = f"{ws.title}_{image.anchor}.png"
                output_path = os.path.join(output_folder, f"xlsx_{os.path.basename(xlsx_path).replace('.xlsx', '')}_{img_name}")
                with open(output_path, "wb") as f:
                    f.write(img_data)
                count += 1
                print(f"✓ 已提取: {output_path}")
        return count
    except Exception as e:
        print(f"✗ 提取 XLSX 失败: {e}")
        return 0

def extract_images_from_pdf(pdf_path, output_folder):
    """从PDF文件提取图片"""
    try:
        doc = fitz.open(pdf_path)
        count = 0
        for page_num in range(len(doc)):
            page = doc[page_num]
            images = page.get_images(full=True)
            for img_index, img_data in enumerate(images):
                xref = img_data[0]
                pix = fitz.Pixmap(doc, xref)
                
                # 确保是RGB
                if pix.n - pix.alpha < 4:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                
                output_path = os.path.join(output_folder, 
                    f"pdf_{os.path.basename(pdf_path).replace('.pdf', '')}_page{page_num+1}_img{img_index}.png")
                pix.save(output_path)
                count += 1
                print(f"✓ 已提取: {output_path}")
        doc.close()
        return count
    except Exception as e:
        print(f"✗ 提取 PDF 失败: {e}")
        return 0

def batch_extract_images(input_folder, output_folder):
    """批量提取所有文件中的图片"""
    os.makedirs(output_folder, exist_ok=True)
    total_count = 0
    
    print(f"🔍 开始扫描文件夹: {input_folder}\n")
    
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        
        if not os.path.isfile(file_path):
            continue
        
        print(f"\n📄 处理文件: {file_name}")
        
        if file_name.endswith('.docx'):
            count = extract_images_from_docx(file_path, output_folder)
            total_count += count
        elif file_name.endswith('.xlsx'):
            count = extract_images_from_xlsx(file_path, output_folder)
            total_count += count
        elif file_name.endswith('.pdf'):
            count = extract_images_from_pdf(file_path, output_folder)
            total_count += count
        else:
            print(f"⊘ 不支持的文件类型: {file_name}")
    
    print(f"\n✅ 完成! 共提取 {total_count} 张图片\n保存位置: {output_folder}")
    return total_count

if __name__ == "__main__":
    input_folder = sys.argv[1] if len(sys.argv) > 1 else "input_folder"
    output_folder = sys.argv[2] if len(sys.argv) > 2 else "extracted_images"
    batch_extract_images(input_folder, output_folder)
