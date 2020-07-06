import glob
import argparse
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    "--from-path",
    required=True,
    help="From Path(string, example: E:/from)",
)

parser.add_argument(
    "--dest-path",
    required=True,
    help="Destination Path(string, example: E:/dst)",
)

parser.add_argument(
    "--search-file",
    required=False,
    default="*",
    help="Search File(string, example: *.mp4)",
)




args = parser.parse_args()
import os
import shutil
import filecmp
print("Start: drive_recorder_mover")
search_path = args.from_path + "/"+args.search_file
print("glob path: {}".format(search_path))
cnt = 0
files = glob.glob(search_path)
max_cnt = len(files)
for val in files:
    cnt+=1
    show = "{}/{}".format(cnt,max_cnt)
    print(show,val)
    val_raw = val
    val = val.replace(args.from_path,args.dest_path)
    if not os.path.exists(os.path.dirname(val)):
        os.makedirs(os.path.dirname(val))
    elif os.path.exists(val):
            if filecmp.cmp(val_raw,val):
                print("同一のファイルのため削除してスキップします")
                os.remove(val_raw)
                continue
    shutil.copy(val_raw,val)
print("End: drive_recorder_mover")