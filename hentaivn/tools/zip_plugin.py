import zipfile
import os

def zip_plugin():
    target = 'd:/AT/github/vbook-project/my-vbook-repo/hentaivn/plugin.zip'
    base_dir = 'd:/AT/github/vbook-project/my-vbook-repo/hentaivn'
    
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(os.path.join(base_dir, 'plugin.json'), 'plugin.json')
        
        src_dir = os.path.join(base_dir, 'src')
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                if file.endswith('.js'):
                    filepath = os.path.join(root, file)
                    arcname = os.path.relpath(filepath, base_dir)
                    # wait, vbook expects plugin.json and scripts as per plugin.json
                    # in plugin.json we wrote "home.js" without "src/", so vbook unzips and finds home.js at the same level as plugin.json
                    # So we should put them at the root of the zip.
                    arcname = file # just the filename
                    zipf.write(filepath, arcname)
    print(f"Created {target}")

if __name__ == '__main__':
    zip_plugin()
