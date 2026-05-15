import webbrowser
from Automation.web_data import website


def openweb(webname):
    website_name = webname.lower().split()
    counts = {}

    for name in website_name:
        counts[name] = counts.get(name, 0) + 1

    urls_to_open = []

    for name, count in counts.items():
        if name in website:
            urls_to_open.extend([website[name]] * count)

    for url in urls_to_open:
        webbrowser.open(url)

    if urls_to_open:
        print("Opening...")
    else:
        print("Website not found")
        
# if __name__ == "__main__":
#     while True:
#         web_input = input("web name: ")
#         openweb(web_input)