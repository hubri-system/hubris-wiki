from frontmatter import load, dump, Post
import os
import re
import wikitextparser as wtp


def delete_key(data: Post, *keys: str) -> Post:
    for key in keys:
        if data.metadata.get(key):
            del data.metadata[key]
    return data


for root, dirs, files in os.walk("Character Options/Classes"):
    for file in [os.path.join(root, f) for f in files]:
        data = load(file)
        if data.get("Properties"):
            del data["Properties"]

            # data["tags"] = data.get("Properties")
        # data = delete_key(data, "tags", "Tags", "tag", "Tag")
        # tags = data.metadata.get("tags") or data.metadata.get("Tags")
        # data.metadata["Tag(s)"] = [f"[[{t}|{t.split("/")[-1]}]]" for t in tags]
        # dump(data, file)
        # data = delete_key(data, "tags", "Tags", "tag", "Tag")
        dump(data, file)
        # if data.metadata.get("Tags") or data.metadata.get("tags"):
        #     data.metadata["Tag(s)"] = data.metadata.get

        # if data.metadata.get("Path"):
        #     data.metadata["tags"] = f'Paths/{(
        #         wtp.parse(data.metadata.get("Path")[0])
        #         .wikilinks[0]
        #         .title.split("/")[-1]
        #         .replace("\\", "")
        #     )}'
        #     del data.metadata["Path"]
        #     dump(data, file)


#         data = load(file)
#         data = delete_key(data, "Template", "Description", "Tree", "Required For")
#         data.content = data.content.replace("==", "")
#         # if data.metadata.get("tags"):
#         #     data.metadata["tags"] = [d.replace("[[", '').replace("]]", '') for d in data.metadata["tags"]]
#         dump(data, file)


# yams = frontmatter.load("Core Rules/Classes/Barbarian.md")
# print(yams.metadata)
