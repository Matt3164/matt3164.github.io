import yaml

if __name__ == '__main__':

    with open("snippets_user.yaml", "r") as f:
        snippet_map = yaml.load(f)


    with open("snippets.md", "w") as f:

        f.write("# Snippets \n")

        for key, val in snippet_map.items():

            f.write(f"## {key.replace('_', ' ')} \n")

            for _key, _val in val.items():
                f.write(f"- [{_key.replace('_', ' ')}]({str(_val)}) \n")


