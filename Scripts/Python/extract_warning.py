import os
import re
import argparse
from collections import defaultdict

# This script extracts warnings from compiler log files. 
# It supports both brief and detailed warning logs, and can handle multiple directories and file extensions.
# The output is organized by warning type and includes the original compiler log file for reference.

def get_full_warning(lines, idx):
    warning = ""
    for i in range(idx, len(lines)):
        if lines[i].replace(" ", "") != "\n":
            warning += lines[i]
        else:
            break
    return warning + "\n"

def parse_warning(args):
    file_list = []
    # {file, warn_dict}
    warnings_dict = {}
    for dir in args.work_dir:
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.lower().endswith(args.file_ext.lower()):
                    if os.path.join(root, file) not in file_list:
                        file_list.append(os.path.join(root, file))
    for f in file_list:
        with open(f, encoding="utf-8", mode="r") as rf:
            lines = rf.readlines()
            # {warning_type, [warning_content]}
            warn_dict = defaultdict(list)
            for idx in range(len(lines)):
                ma = re.search("^Warning", lines[idx])
                if ma:
                    w = get_full_warning(lines, idx)
                    if w not in warn_dict[lines[idx].strip()]:
                        warn_dict[lines[idx].strip()].append(w)
            warnings_dict[f] = warn_dict
    if os.path.exists(args.output_dir):
        for root, dirs, files in os.walk(args.output_dir):
            for file in files:
                if file.startswith("Warning_"):
                    os.remove(os.path.join(root, file))
    else:
        os.makedirs(args.output_dir)
    for f, dt in warnings_dict.items():
        for t, wl in dt.items():
            with open(args.output_dir + "/" + t.split()[0].replace("-[", "_").replace("]", "") + ".log", encoding="utf-8", mode="a") as af:
                af.write(f"compiler log: {f}\n\n")
                af.writelines(wl)
                af.write("\n")
                    

def parse_warning_abs(args):
    tmp_file = "/tmp/compiler_warning.log"
    file_list = []
    warnings_dict = {}
    for root, dirs, files in os.walk(args.work_dir):
        for file in files:
            if file.lower().endswith(args.file_ext.lower()):
                file_list.append(os.path.join(root, file))
    for f in file_list:
        os.system(f"grep '^Warning {f} | sort | uniq -c > {tmp_file}")
        with open(tmp_file, encoding="utf-8", mode="r") as rf:
            lines = rf.readlines()
            warnings_dict[f] = lines
    os.system(f"rm {tmp_file}")
    if not os.path.exists(args.output_dir):
        os.makedirs(args.outputJ_dir)
    with open(args.output_dir + "/extract_warning.log", encoding="utf-8", mode="w") as wf:
        for w,l in warnings_dict.items():
            if len(l) > 0 :
                wf.write("compiler log: " + w + "\n")
                wf.writelines(l)
                wf.write("\n\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-work_dir", type=str, nargs="+", help='log dir name(support recursive and multiple dirs), default is ["./"]', default=["./"])
    parser.add_argument("-file_ext", type=str, help="file ext(support full name), default is compiler.log", default="compiler.log")
    parser.add_argument("-brief", type=str, help="gen brief warning log, default is no", default="no")
    parser.add_argument("-detail", type=str, help="gen detail warning log, default is yes", default="yes")
    parser.add_argument("-output_dir", type=str, help="parse warning output dir, default is ./compiler_warnings/", default="./compiler_warning")
    args = parser.parse_args()

    if args.detail.lower() == "yes" or args.detail.lower() == "y":
        parse_warning(args=args)
    if args.brief.lower() == "yes" or args.brief.lower() == "y":
        parse_warning_abs(args=args)