from pathlib import Path

repo_path = input("Enter the path: ")

repo_object = Path(repo_path)

linecountpy = 0
linecountjson = 0
linecounttxt = 0
linecountmd = 0

if not repo_object.exists():
    print("Path does not exist")
    exit()

fcpy = 0
fcjson = 0
fctxt = 0
fcmd = 0

largest_file = ""
largest_lines = 0

for item in repo_object.rglob("*"):

    if item.is_file():

        try:
            with open(item, "r", encoding="utf-8") as f:
                file_lines = len(f.readlines())
        except:
            continue

        # Largest file check
        if file_lines > largest_lines:
            largest_lines = file_lines
            largest_file = item.name

        if item.suffix == ".py":
            fcpy += 1
            linecountpy += file_lines

        elif item.suffix == ".json":
            fcjson += 1
            linecountjson += file_lines

        elif item.suffix == ".txt":
            fctxt += 1
            linecounttxt += file_lines

        elif item.suffix == ".md":
            fcmd += 1
            linecountmd += file_lines

total_files = fcpy + fcjson + fctxt + fcmd

total_lines = (
    linecountpy
    + linecountjson
    + linecounttxt
    + linecountmd
)

print("\n" + "=" * 40)
print("REPOSITORY ANALYSIS REPORT")
print("=" * 40)

print("\nTotal Files:", total_files)

print("\nFile Statistics")
print("Python Files   :", fcpy, "| Lines:", linecountpy)
print("JSON Files     :", fcjson, "| Lines:", linecountjson)
print("Text Files     :", fctxt, "| Lines:", linecounttxt)
print("Markdown Files :", fcmd, "| Lines:", linecountmd)

print("\nTotal Lines:", total_lines)

print("\nLargest File:")
print(largest_file, "-", largest_lines, "lines")

print("\n" + "=" * 40)