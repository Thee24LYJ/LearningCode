# -*- coding: utf-8 -*-#
"""
    @project: convert2pdf
    @Author：lyj
    @file： ppt2pdf.py
    @date：2023/5/25 21:48
    @blogs: 
    @description: 将ppt转换为pdf
"""
import os
import pathlib
import win32com.client
import docx2pdf

"""
convert_ppt_to_pdf函数使用win32com库打开PPT文件并将其保存为PDF文件
batch_convert_types_to_pdf函数列出PPT文件夹中的所有PPT文件，并为每个文件调用convert_ppt_to_pdf`函数
"""


def convert_ppt_to_pdf(ppt_path, pdf_path):
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    powerpoint.Visible = 1
    ppt = powerpoint.Presentations.Open(ppt_path)
    ppt.SaveAs(pdf_path, 32)  # 32表示PDF格式
    ppt.Close()
    powerpoint.Quit()


# 该函数实现还存在问题
def convert_docx_to_pdf(docx_path, pdf_path):
    # 调用convert函数将Word文档转换为PDF
    docx2pdf.convert(docx_path, pdf_path)


def batch_convert_types_to_pdf(file_path, pdf_folder):
    if pathlib.Path(file_path).exists():
        path = file_path
        if os.path.isdir(file_path):  # 文件夹
            if not file_path.endswith("\\"):
                path = file_path + '\\'
            print(path)
            file_folder = path
            files = os.listdir(file_folder)
            print("-------------begin to convert file to pdf-------------\n")
            for file in files:
                if file.endswith(".ppt") or file.endswith(".pptx"):
                    ppt_path = os.path.join(file_folder, file)
                    pdf_path = os.path.join(pdf_folder, file.replace(".pptx", ".pdf").replace(".ppt", ".pdf"))
                    convert_ppt_to_pdf(ppt_path, pdf_path)
                    print(f"{ppt_path} convert finished...")
                elif file_path.endswith(".doc") or file_path.endswith(".docx"):
                    docx_path = os.path.join(file_folder, file)
                    pdf_path = os.path.join(pdf_folder, file.replace(".pptx", ".pdf").replace(".ppt", ".pdf"))
                    convert_docx_to_pdf(docx_path, pdf_path)
                    print(f"{docx_path} convert finished...")
            print("\n-------------end to convert file to pdf-------------")
        else:  # 文件
            file = path
            file_folder = os.path.dirname(file)
            if file.endswith(".ppt") or file.endswith(".pptx"):
                ppt_path = os.path.join(file_folder, file)
                pdf_path = os.path.join(pdf_folder, file.replace(".pptx", ".pdf").replace(".ppt", ".pdf"))
                convert_ppt_to_pdf(ppt_path, pdf_path)
                print(f"{ppt_path} convert finished...")
            elif file_path.endswith(".doc") or file_path.endswith(".docx"):
                docx_path = os.path.join(file_folder, file)
                pdf_path = os.path.join(pdf_folder, file.replace(".pptx", ".pdf").replace(".ppt", ".pdf"))
                convert_docx_to_pdf(docx_path, pdf_path)
                print(f"{docx_path} convert finished...")
    else:
        print("the input path dose not exist!!!")


# 示例用法
if __name__ == '__main__':
    while True:
        src_path = input("please input the ppt(x) or doc(x) file or folder path:").strip('"')
        dest_folder = os.path.dirname(src_path)
        batch_convert_types_to_pdf(src_path, dest_folder)
