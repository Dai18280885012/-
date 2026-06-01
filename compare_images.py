import os
import cv2
import numpy as np
from PIL import Image
import imagehash
from skimage.metrics import structural_similarity as ssim
import json

class ImageComparator:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.images = {}
        self.hashes = {}
        self.load_images()
    
    def load_images(self):
        """Load all images"""
        print("🖼️  加载图片中...")
        for img_name in os.listdir(self.image_folder):
            img_path = os.path.join(self.image_folder, img_name)
            if img_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                try:
                    self.images[img_name] = cv2.imread(img_path)
                    self.hashes[img_name] = imagehash.average_hash(Image.open(img_path))
                except Exception as e:
                    print(f"✗ 无法加载: {img_name} - {e}")
        print(f"✅ 已加载 {len(self.images)} 张图片\n")
    
    def hash_similarity(self, hash1, hash2):
        """Calculate perceptual hash similarity"""
        distance = hash1 - hash2
        return max(0, 1 - distance / 64)
    
    def ssim_similarity(self, img1, img2):
        """Calculate SSIM similarity"""
        try:
            if len(img1.shape) == 3:
                img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            if len(img2.shape) == 3:
                img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            
            if img1.shape != img2.shape:
                img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
            
            score, _ = ssim(img1, img2, full=True)
            return score
        except:
            return 0
    
    def orb_similarity(self, img1, img2):
        """Calculate ORB feature matching similarity"""
        try:
            if len(img1.shape) == 3:
                img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            if len(img2.shape) == 3:
                img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            
            orb = cv2.ORB_create(nfeatures=500)
            kp1, des1 = orb.detectAndCompute(img1, None)
            kp2, des2 = orb.detectAndCompute(img2, None)
            
            if des1 is None or des2 is None:
                return 0
            
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1, des2)
            
            if min(len(kp1), len(kp2)) == 0:
                return 0
            
            return len(matches) / max(len(kp1), len(kp2))
        except:
            return 0
    
    def compare_all(self, threshold=0.8, method='hash'):
        """Compare all images and return similar pairs"""
        print(f"🔄 使用 {method} 方法比较图片相似度...\n")
        
        img_names = list(self.images.keys())
        similar_groups = {}
        compared = set()
        
        for i, img1_name in enumerate(img_names):
            for img2_name in img_names[i+1:]:
                if (img1_name, img2_name) in compared:
                    continue
                
                img1 = self.images[img1_name]
                img2 = self.images[img2_name]
                
                if method == 'hash':
                    similarity = self.hash_similarity(self.hashes[img1_name], self.hashes[img2_name])
                elif method == 'ssim':
                    similarity = self.ssim_similarity(img1, img2)
                elif method == 'orb':
                    similarity = self.orb_similarity(img1, img2)
                else:
                    similarity = 0
                
                compared.add((img1_name, img2_name))
                
                if similarity >= threshold:
                    key = f"{img1_name} <-> {img2_name}"
                    similar_groups[key] = round(similarity, 4)
                    print(f"✓ {similarity:.2%}: {img1_name}")
                    print(f"  ↔️ {img2_name}")
        
        return similar_groups
    
    def save_report(self, results, output_file="similarity_report.json"):
        """Save comparison report"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n💾 报告已保存: {output_file}")

def main():
    import sys
    
    image_folder = sys.argv[1] if len(sys.argv) > 1 else "extracted_images"
    output_report = sys.argv[2] if len(sys.argv) > 2 else "similarity_report.json"
    method = sys.argv[3] if len(sys.argv) > 3 else "hash"
    threshold = float(sys.argv[4]) if len(sys.argv) > 4 else 0.8
    
    print("="*50)
    print("📊 图片相似度对比工具")
    print("="*50 + "\n")
    
    comparator = ImageComparator(image_folder)
    results = comparator.compare_all(threshold=threshold, method=method)
    
    if results:
        print(f"\n📌 找到 {len(results)} 对相似图片:\n")
        for pair, similarity in sorted(results.items(), key=lambda x: x[1], reverse=True):
            print(f"  {similarity:.2%} - {pair}")
    else:
        print("\n⊘ 未找到相似图片")
    
    comparator.save_report(results, output_report)

if __name__ == "__main__":
    main()
