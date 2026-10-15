import shutil
import os

src = '/Users/cloudiaozeir/Library/Mobile Documents/com~apple~CloudDocs/Documents/OCU LAW/SBA/IPLS/Website Info/Headshots/2026'
dst = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'images', 'headshots')

mapping = {
    'Cloudia Ozeir Headshot - PRESIDENT.jpeg': ['headshot-cloudia.jpg', 'Cloudia Ozeir Headshot - PRESIDENT.jpeg'],
    'Jacob Beckham Headshot - PRESIDENT.jpeg': ['headshot-jacob.jpg', 'Jacob Beckham Headshot - PRESIDENT.jpeg'],
    'Helene Bergmann-Busby - VICE PRESIDENT.jpeg': ['headshot-helene.jpg', 'Helene Bergmann-Busby - VICE PRESIDENT.jpeg'],
    'Dani Headshot - TREASURER.jpeg': ['headshot-dani.jpg', 'Dani Headshot - TREASURER.jpeg'],
    'Kristyn Hart Headshot - SECRETARY.jpg': ['headshot-kristyn.jpg', 'Kristyn Hart Headshot - SECRETARY.jpg'],
    'Douglas Sorocco - FACULTY ADVISOR.jpg': ['headshot-douglas.jpg', 'Douglas Sorocco - FACULTY ADVISOR.jpg']
}

for src_name, dst_names in mapping.items():
    s_path = os.path.join(src, src_name)
    if os.path.exists(s_path):
        for d_name in dst_names:
            d_path = os.path.join(dst, d_name)
            shutil.copyfile(s_path, d_path)
            print(f"Copied {src_name} -> {d_name} ({os.path.getsize(d_path)} bytes)")
