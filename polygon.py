import json
import os
import glob

JSON_DIR = "dataset/val/json"
SAVE_DIR = "dataset/val/labels"

os.makedirs(SAVE_DIR, exist_ok=True)

for js in glob.glob(os.path.join(JSON_DIR, "*.json")):
    with open(js) as f:
        data = json.load(f)

    img_w = data["imageWidth"]
    img_h = data["imageHeight"]

    label_txt = os.path.join(
        SAVE_DIR,
        os.path.splitext(os.path.basename(js))[0] + ".txt"
    )

    lines = []
    for shape in data["shapes"]:
        if shape["shape_type"] != "polygon":
            continue

        if shape["label"].strip().lower() != "c line":
            continue

        seg = []
        for x, y in shape["points"]:
            seg.append(x / img_w)
            seg.append(y / img_h)

        if len(seg) >= 6:
            lines.append("0 " + " ".join(f"{v:.6f}" for v in seg))

    if lines:
        with open(label_txt, "w") as f:
            f.write("\n".join(lines))

