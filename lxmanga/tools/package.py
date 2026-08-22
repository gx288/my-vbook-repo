import zipfile
import os

def create_plugin_zip():
    plugin_dir = r"d:\AT\github\vbook-project\my-vbook-repo\lxmanga"
    zip_path = os.path.join(plugin_dir, "plugin.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add plugin.json
        plugin_json_path = os.path.join(plugin_dir, "plugin.json")
        zipf.write(plugin_json_path, arcname="plugin.json")
        
        # Add src files
        src_dir = os.path.join(plugin_dir, "src")
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.join("src", os.path.relpath(file_path, src_dir))
                zipf.write(file_path, arcname=arcname)
                
    print(f"Successfully created {zip_path}")

if __name__ == "__main__":
    create_plugin_zip()
