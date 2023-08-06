from gnutools.fs import load_config as _load_config, parent
import os
from tqdm import tqdm
from gnutools import fs


def load_config():
    # Priority is on global variable
    try:
        filename = os.environ["red_CONFIG"]
        cfg = _load_config(filename)
    # Then default path
    except:
        filename = f"{parent(__file__)}/config.yml"
        cfg = _load_config(filename)
    return cfg


import re


def split_bucket_name(root):
    path = root.split("miniofs://")[1]
    splits = path.split("/")
    bucket, prefix = splits[0], "/".join(splits[1:])
    return bucket, prefix


def listfiles(root, patterns=[]):
    from miniofs import client

    bucket, prefix = split_bucket_name(root)
    files = [
        f"miniofs://{bucket}/{obj.object_name}"
        for obj in client.list_objects(bucket, recursive=True, prefix=prefix)
    ]
    if len(patterns) > 0:
        results = []
        for p in patterns:
            results += [f for f in files if len(re.split(p, f)) > 1]
    else:
        results = files
    return results


def download_file(file, filestore="/FileStore"):
    from miniofs import client

    bucket, object_name = split_bucket_name(file)
    output_file = os.path.join(f"{filestore}/{bucket}", object_name)
    os.makedirs(parent(output_file), exist_ok=True)
    client.fget_object(
        bucket,
        object_name,
        output_file,
    )


def download_files(root, patterns=[], filestore="/FileStore"):
    files = listfiles(root, patterns)
    for file in tqdm(
        files, total=len(files), desc=f"Downloading objects to {filestore}"
    ):
        download_file(file, filestore=filestore)


def split_object_name(file, filestore="/FileStore"):
    splits = file.split(filestore)[1].split("/")[1:]
    bucket = splits[0]
    object_name = "/".join(splits[1:])
    return bucket, object_name


def upload_file(file, filestore="/FileStore"):
    from miniofs import client

    bucket, object_name = split_object_name(file, filestore=filestore)
    client.fput_object(
        bucket,
        object_name,
        file,
    )

def exists(file, filestore="/FileStore"):
    bucket, object_name = split_object_name(file, filestore=filestore)
    return len(listfiles(f"miniofs://{bucket}/{object_name}")) > 0


def upload_files(files, filestore="/FileStore", overwrite=True):
    for file in tqdm(
        files, total=len(files), desc=f"Uploading objects from {filestore}"
    ):
        if overwrite:
            upload_file(file, filestore=filestore)
        elif not exists(file, filestore=filestore):
            upload_file(file, filestore=filestore)


if __name__ == "__main__":
    # print(listfiles("miniofs://msranker/bronze/tar_mini", ["dataset"]))
    # download_files("miniofs://msranker/bronze/tar_mini", ["dataset"])
    upload_files(
        fs.listfiles("/FileStore/msranker/landing/json_mini", [".json"]),
        filestore="/FileStore",
        overwrite=False,
    )
