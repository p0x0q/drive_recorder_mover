import glob
import argparse
parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    "--drive-path",
    required=True,
    help="Drive Path(numeric, example: E:)",
)
parser.add_argument(
    "--move-to-path",
    required=True,
    help="Drive Path(numeric, example: E:)",
)



args = parser.parse_args()
import os
import shutil
import filecmp
for val in glob.glob(args.drive_path + "/**/*.mp4"):
    print(val)
    val_raw = val
    val = val.replace(args.drive_path,args.move_to_path)
    if not os.path.exists(os.path.dirname(val)):
        os.makedirs(os.path.dirname(val))
    elif os.path.exists(val):
            if filecmp.cmp(val_raw,val):
                print("同一のファイルのため削除してスキップします")
                os.remove(val_raw)
                continue
    shutil.copy(val_raw,val)
