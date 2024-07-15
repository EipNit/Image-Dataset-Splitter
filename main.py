import os
from collections import defaultdict

global remaining_categories

# 设置JPEGImages目录的相对路径
images_dir = 'images'

# 获取所有JPEG图片的文件名（不含扩展名）
image_files = [file for file in sorted(os.listdir(images_dir)) if file.endswith('.jpg')]

# 提取类别并统计每个类别的图片数量
categories = defaultdict(list)
for file in image_files:
    category = '_'.join(file.split('_')[:3])
    categories[category].append(file)

# 打印每个类别及其图片数量
print("每个类别及其图片数量:")
total_images = 0
for category, files in categories.items():
    print(f"{category}: {len(files)}")
    total_images += len(files)
print(f"\n图片总数: {total_images}")

# 全局变量，保存剩余未选择的类别
remaining_categories = set(categories.keys())

def print_remaining_categories():
    remaining_images = 0
    for category in remaining_categories:
        print(f"{category}: {len(categories[category])}")
        remaining_images += len(categories[category])
    print(f"\n剩余图片总数: {remaining_images}")

def input_categories(label):
    selected_categories = []
    selected_images = 0

    while True:
        input_categories = input(f"请输入{label}类别 (用逗号分隔): ").split(',')
        input_categories = [category.strip() for category in input_categories]

        for category in input_categories:
            if category in categories and category not in selected_categories:
                selected_categories.append(category)
                selected_images += len(categories[category])
                remaining_categories.discard(category)

        print(f"\n当前选择的类别:")
        print(f"{label}:", selected_categories)
        print(f"已选择图片总数: {selected_images}")

        print("\n剩余未选择的类别:")
        print_remaining_categories()

        continue_selection = input(f"是否继续选择{label}? (y/n): ").strip().lower()
        if continue_selection == 'n':
            break

    return selected_categories, selected_images

# 选择训练集类别
selected_train_categories, selected_train_images = input_categories("训练集")
train_ids = []
for category in selected_train_categories:
    train_ids.extend(categories[category])

# 选择验证集类别
selected_val_categories, selected_val_images = input_categories("验证集")
val_ids = []
for category in selected_val_categories:
    val_ids.extend(categories[category])

# 选择测试集类别
selected_val_categories, selected_val_images = input_categories("测试集")
test_ids = []
for category in selected_val_categories:
    test_ids.extend(categories[category])

# 写入分配结果到相应的文件，并为图像路径添加前缀
def write_ids_to_file(ids, filename, prefix='./images/'):
    with open(filename, 'w') as f:
        for image_id in ids:
            f.write(f'{prefix}{image_id}\n')

write_ids_to_file(train_ids, 'train.txt')
write_ids_to_file(val_ids, 'val.txt')
write_ids_to_file(test_ids, 'test.txt')

print(f"\nTraining set: {len(train_ids)} images")
print(f"Validation set: {len(val_ids)} images")
print(f"Testing set: {len(test_ids)} images")